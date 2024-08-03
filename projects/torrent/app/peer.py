from typing import Tuple, Optional, Union
from torrent import Torrent
import messages as messages
import socket 
import logging
LOG = logging.getLogger(__name__)


class Peer:
    my_peer_id: bytes
    torrent: Torrent
    address: Tuple[str, int]
    socket: socket.socket

    def __init__(self, my_peer_id: bytes, torrent: Torrent, address: Tuple[str, int]):
        self.my_peer_id = my_peer_id
        self.torrent = torrent
        self.address = address

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(2)

    def download_piece(self, piece_index: int) -> Union[bytearray, bool]:
        if not self.handshake():
            return False

        message = self.receive()

        if not isinstance(message, messages.BitfieldMessage):
            return False

        self.send(messages.InterestedMessage())

        message = self.receive()

        if not isinstance(message, messages.UnchokeMessage):
            return False

        piece_length = self.torrent.compute_piece_length(piece_index) # compute piece length
        piece_data = bytearray(piece_length) # create a bytearray to store the piece data

        # iterate over the blocks of the piece
        for block_begin, block_length in self.torrent.iter_blocks(piece_length):
            self.send(messages.RequestMessage(index=piece_index, begin=block_begin, length=block_length))

            message = self.receive()

            if not isinstance(message, messages.PieceMessage):
                return False

            if message.index != piece_index:
                continue

            piece_data[message.begin:len(message.block)] = message.block

        return piece_data

    def receive(self) -> Optional[messages.Message]:
        try:
            message_length = int.from_bytes(self.socket.recv(4), byteorder='big')
            if message_length is None:
                return None
            if message_length == 0:
                return messages.KeepAliveMessage()

            LOG.debug(f'Receiving message of length {message_length}')
            raw_data = self.socket.recv(message_length)
            LOG.debug(f'Received raw data: {raw_data}')
            return messages.from_bytes(raw_data)
        except Exception as e:
            LOG.error(f'Error receiving message: {e}')
            return None

    def send(self, message: messages.Message) -> None:
        self.socket.sendall(message.serialize())

    def handshake(self) -> Optional[messages.HandshakeMessage]:
        self.socket.sendall(messages.HandshakeMessage(
            info_hash=self.torrent.info_hash.digest(),
            peer_id=self.my_peer_id
        ).serialize())

        response = messages.HandshakeMessage.unserialize(
            self.socket.recv(messages.HandshakeMessage.size())
        )

        if not isinstance(response, messages.HandshakeMessage):
            return None

        return response

    def connect(self) -> None:
        self.socket.connect(self.address)

    def disconnect(self) -> None:
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def __enter__(self):
        self.connect()

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.disconnect()
