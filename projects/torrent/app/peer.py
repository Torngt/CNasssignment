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
    socket: socket.socket # type: ignore

    def __init__(self, my_peer_id: bytes, torrent: Torrent, address: Tuple[str, int]):
        self.my_peer_id = my_peer_id
        self.torrent = torrent
        self.address = address

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(2)

    def download_piece(self, piece_index: int, output_file: str ='sample.txt') -> Union[bytearray, bool]:
        if not self.handshake():
            return False

        message = self.receive()

        if not isinstance(message, messages.BitfieldMessage):
            return False

        self.send(messages.InterestedMessage())

        message = self.receive()

        if not isinstance(message, messages.UnchokeMessage):
            return False

        piece_length = self.torrent.compute_piece_length(piece_index)  # compute piece length

        # open file in binary write mode
        with open(output_file, 'wb') as f:
            # iterate over the blocks of the piece
            for block_begin, block_length in self.torrent.iter_blocks(piece_length):
                self.send(messages.RequestMessage(index=piece_index, begin=block_begin, length=block_length))

                while True:
                    message = self.receive()

                    if isinstance(message, messages.PieceMessage) and message.index == piece_index:
                        f.write(message.block)
                        break
                    elif isinstance(message, messages.CancelMessage):
                        # Handle cancellation message
                        LOG.warning(f'CancelMessage received: {message}')
                        return False
                    elif message is None:
                        # Handle case where no message is received
                        LOG.error('No message received')
                        return False
                LOG.info(f'Piece {piece_index} downloaded to {output_file}')
        return True

    def receive(self) -> Optional[messages.Message]:
        try:
            # Read the length prefix
            length_prefix = self._recv_all(4)
            if not length_prefix:
                return None
            message_length = int.from_bytes(length_prefix, byteorder='big')
            if message_length == 0:
                return messages.KeepAliveMessage()

            # Read the actual message data
            raw_data = self._recv_all(message_length)
            if not raw_data:
                return None

            LOG.debug(f'Received raw data: {raw_data}')
            return messages.from_bytes(raw_data)
        except Exception as e:
            LOG.error(f'Error receiving message: {e}')
            return None

    def _recv_all(self, length: int) -> bytes:
        """Receive the specified number of bytes from the socket, handling partial reads."""
        data = b""
        while len(data) < length:
            chunk = self.socket.recv(length - len(data))
            if not chunk:
                raise Exception("Socket connection broken")
            data += chunk
        return data

    def send(self, message: messages.Message) -> None:
        self.socket.sendall(message.serialize())

    def handshake(self) -> Optional[messages.HandshakeMessage]:
        self.socket.sendall(messages.HandshakeMessage(
            info_hash=self.torrent.info_hash.digest(),
            peer_id=self.my_peer_id
        ).serialize())

        response = messages.HandshakeMessage.unserialize(
            self._recv_all(messages.HandshakeMessage.size())
        )

        if not isinstance(response, messages.HandshakeMessage):
            return None

        return response

    def connect(self) -> None:
        try:
            self.socket.connect(self.address)
            LOG.info(f'Connected to {self.address}')
        except Exception as e:
            LOG.error(f'Error connecting to {self.address}: {e}')    

    def disconnect(self) -> None:
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.disconnect()
