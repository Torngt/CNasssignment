from collections import OrderedDict
from urllib import request, parse
from torrent import Torrent
from typing import Optional, List
from socket import inet_ntoa
import bencode
from io import BytesIO
import struct


class Tracker:
    my_peer_id: bytes
    torrent: Torrent

    def __init__(self, my_peer_id: bytes, torrent: Torrent):
        self.my_peer_id = my_peer_id
        self.torrent = torrent

    def request(self, left: Optional[int] = None, uploaded: int = 0, downloaded: int = 0) -> OrderedDict:
        parameters = {
            'info_hash': self.torrent.info_hash.digest(),
            'peer_id': self.my_peer_id,
            'port': 6881,
            'uploaded': uploaded,
            'downloaded': downloaded,
            'left': left or self.torrent.length,
            'compact': 1,
        }

        response = request.urlopen(f'{self.torrent.tracker_url}?{parse.urlencode(parameters)}')

        with BytesIO(response.read()) as f:
            response_unpacked = bencode.unpack(f)

        if 'peers' in response_unpacked:
            response_unpacked['peers'] = Tracker.parse_peers(response_unpacked['peers'])

        return response_unpacked

    @staticmethod
    def parse_peers(peers: bytes) -> List:
        ret = []

        for i in range(0, len(peers), 6):
            ip, port = struct.unpack('>4sH', peers[i:i + 6])

            ret.append((inet_ntoa(ip), port))

        return ret
