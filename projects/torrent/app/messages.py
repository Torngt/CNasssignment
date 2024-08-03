from dataclasses import dataclass
from typing import Tuple
import struct

import logging
LOG = logging.getLogger(__name__)

PSTR = b'BitTorrent protocol'
PSTRLEN = len(PSTR)


class HasStructMixin:
    _format: str

    def pack(self, *data) -> bytes:
        return struct.pack(f'>{self._format}', *data)

    @classmethod
    def unpack(cls, data: bytes) -> Tuple:
        return struct.unpack(f'>{cls._format}', data)

    @classmethod
    def size(cls) -> int:
        return struct.calcsize(cls._format)


class Message:
    def serialize(self) -> bytes:
        return b''

    @classmethod
    def unserialize(cls, data: bytes):
        return cls()


class TypedMessage(Message):
    _type: int

    def to_bytes(self) -> bytes:
        return b''

    def serialize(self) -> bytes:
        message_payload = self.to_bytes()

        return struct.pack('>IB', 1 + len(message_payload), self._type) + message_payload


@dataclass
class HandshakeMessage(HasStructMixin, Message):
    info_hash: bytes
    peer_id: bytes
    reserved: bytes = b'\x00' * 8

    _format: str = f'B{PSTRLEN}s8s20s20s'

    def serialize(self) -> bytes:
        return self.pack(
            PSTRLEN,
            PSTR,
            self.reserved,
            self.info_hash,
            self.peer_id
        )

    @classmethod
    def unserialize(cls, data: bytes):
        pstrlen, pstr, reserved, info_hash, peer_id = cls.unpack(data)

        if pstrlen != PSTRLEN or pstr != PSTR:
            raise ValueError()

        return cls(info_hash=info_hash, peer_id=peer_id, reserved=reserved)


class KeepAliveMessage(Message):
    pass


class ChokeMessage(TypedMessage):
    _type: int = 0


class UnchokeMessage(TypedMessage):
    _type: int = 1


class InterestedMessage(TypedMessage):
    _type: int = 2


class NotInterestedMessage(TypedMessage):
    _type: int = 3


@dataclass
class HaveMessage(HasStructMixin, TypedMessage):
    piece_index: int

    _format = 'I'
    _type: int = 4

    def to_bytes(self) -> bytes:
        return self.pack(
            self.piece_index
        )

    @classmethod
    def unserialize(cls, data: bytes):
        piece_index, = cls.unpack(data)

        return cls(piece_index=piece_index)


@dataclass
class BitfieldMessage(TypedMessage):
    bits: bytes

    _type: int = 5

    def to_bytes(self) -> bytes:
        return self.bits

    @classmethod
    def unserialize(cls, data: bytes):
        return cls(bits=data)

    @staticmethod
    def bytes_to_bits(b: bytes) -> str:
        return format(int.from_bytes(b, byteorder='big'), '08b')

    @staticmethod
    def bits_to_bytes(b: str) -> bytes:
        return int(b, 2).to_bytes(4, byteorder='big')


@dataclass
class RequestMessage(HasStructMixin, TypedMessage):
    index: int
    begin: int
    length: int

    _format = 'III'
    _type: int = 6

    def to_bytes(self) -> bytes:
        return self.pack(
            self.index,
            self.begin,
            self.length
        )

    @classmethod
    def unserialize(cls, data: bytes):
        index, begin, length = cls.unpack(data)

        return cls(index=index, begin=begin, length=length)


@dataclass
class PieceMessage(HasStructMixin, TypedMessage):
    index: int
    begin: int
    block: bytes

    _format = 'II'
    _type: int = 7

    def to_bytes(self) -> bytes:
        return self.pack(
            self.index,
            self.begin
        ) + self.block

    @classmethod
    def unserialize(cls, data: bytes):
        index, begin = cls.unpack(data[:8])

        return cls(index=index, begin=begin, block=data[8:])


@dataclass
class CancelMessage(HasStructMixin, TypedMessage):
    index: int
    begin: int
    length: int

    _format = 'III'
    _type: int = 8

    def to_bytes(self) -> bytes:
        return self.pack(
            self.index,
            self.begin,
            self.length
        )

    @classmethod
    def unserialize(cls, data: bytes):
        index, begin, length = cls.unpack(data)

        return cls(index=index, begin=begin, length=length)


MESSAGES_BY_ID = {
    msg_class._type: msg_class for msg_class in (ChokeMessage, UnchokeMessage, InterestedMessage, NotInterestedMessage, HaveMessage,
                                  BitfieldMessage, RequestMessage, PieceMessage, CancelMessage)
}


def from_bytes(data: bytes):
    if not data:
        LOG.error("Empty message received.")
        raise ValueError("Empty message received.")

    message_type = data[0]
    message_payload = data[1:] if len(data) > 1 else b''

    class_ = MESSAGES_BY_ID.get(message_type)

    if not class_:
        LOG.error(f'Unknown message type: {message_type}')
        LOG.error(f'Data: {data}')
        raise ValueError(f'Unknown message type: {message_type}, data: {data}')

    return class_.unserialize(message_payload)
