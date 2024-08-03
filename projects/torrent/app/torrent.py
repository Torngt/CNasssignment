from typing import BinaryIO, OrderedDict, List, Any, Tuple, Generator
from hashlib import sha1
import bencode
from io import BytesIO

BLOCK_LENGTH = 16 * 1024


class Torrent:
    tracker_url: str
    length: int
    piece_length: int
    piece_hashes: List[str]
    info_hash: Any

    def __init__(self, tracker_url: str, length: int, piece_length: int, piece_hashes: List[str], info_hash: Any):
        self.tracker_url = tracker_url
        self.length = length
        self.piece_length = piece_length
        self.piece_hashes = piece_hashes
        self.info_hash = info_hash

    def compute_piece_length(self, piece_index: int) -> int:
        if piece_index > len(self.piece_hashes) - 1:
            raise ValueError('Invalid piece_index')

        pieces_length = (piece_index + 1) * self.piece_length

        if pieces_length > self.length:
            piece_length = self.piece_length - (pieces_length - self.length)
        else:
            piece_length = self.piece_length

        return piece_length

    def iter_blocks(self, piece_length: int) -> Generator[Tuple[int, int], None, None]:
        for block_index, block_begin in enumerate(range(0, piece_length, BLOCK_LENGTH)):
            blocks_length = (block_index + 1) * BLOCK_LENGTH

            if blocks_length > piece_length:
                block_length = BLOCK_LENGTH - (blocks_length - piece_length)
            else:
                block_length = BLOCK_LENGTH

            yield block_begin, block_length

    @classmethod
    def load(cls, f: BinaryIO):
        data = bencode.unpack(f)

        return cls(
            tracker_url=data['announce'].decode(),
            length=data['info']['length'],
            piece_length=data['info']['piece length'],
            piece_hashes=Torrent.parse_piece_hashes(data['info']['pieces']),
            info_hash=Torrent.generate_info_hash(data['info'])
        )

    @staticmethod
    def parse_piece_hashes(pieces: bytes) -> List:
        return [
            pieces[i:i + 20].hex() for i in range(0, len(pieces), 20)
        ]

    @staticmethod
    def generate_info_hash(info: OrderedDict) -> Any:
        with BytesIO() as f:
            bencode.pack(f, info)

            f.seek(0)

            return sha1(f.read())
