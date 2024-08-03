from tracker import Tracker
from torrent import Torrent
from peer import Peer
import bencode
from io import BytesIO
import argparse
import random
import json

MY_PEER_ID = b'github.com/upendra10'


def _bytes_to_str(obj) -> str:
    if isinstance(obj, bytes):
        return obj.decode()

    raise TypeError()


def main() -> None:
    arg_parser = argparse.ArgumentParser()

    command_arg_parser = arg_parser.add_subparsers(dest='command', required=True)

    decode_arg_parser = command_arg_parser.add_parser('decode')
    decode_arg_parser.add_argument('data')

    info_arg_parser = command_arg_parser.add_parser('info')
    info_arg_parser.add_argument('filename')

    peers_arg_parser = command_arg_parser.add_parser('peers')
    peers_arg_parser.add_argument('filename')

    handshake_arg_parser = command_arg_parser.add_parser('handshake')
    handshake_arg_parser.add_argument('filename')
    handshake_arg_parser.add_argument('address')

    download_piece_arg_parser = command_arg_parser.add_parser('download_piece')
    download_piece_arg_parser.add_argument('filename')
    download_piece_arg_parser.add_argument('piece_index', type=int)
    download_piece_arg_parser.add_argument('-o', '--output')

    args = arg_parser.parse_args()

    if args.command == 'decode':
        with BytesIO(args.data.encode()) as f:
            print(json.dumps(bencode.unpack(f), default=_bytes_to_str))
    elif args.command == 'info':
        with open(args.filename, 'rb') as f:
            torrent = Torrent.load(f)

        print(f'Tracker URL: {torrent.tracker_url}')
        print(f'Length: {torrent.length}')
        print(f'Info Hash: {torrent.info_hash.hexdigest()}')
        print(f'Piece Length: {torrent.piece_length}')
        print(f'Piece Hashes:')

        for piece_hash in torrent.piece_hashes:
            print(piece_hash)
    elif args.command == 'peers':
        with open(args.filename, 'rb') as f:
            torrent = Torrent.load(f)

        tracker = Tracker(MY_PEER_ID, torrent)

        for peer in tracker.request()['peers']:
            ip, port = peer

            print(f'{ip}:{port}')
    elif args.command == 'handshake':
        with open(args.filename, 'rb') as f:
            torrent = Torrent.load(f)

        ip, port = args.address.split(':', maxsplit=2)
        address = (ip, int(port))

        with Peer(MY_PEER_ID, torrent, address) as peer:
            handshake = peer.handshake()

        if handshake:
            print(f'Peer ID: {handshake.peer_id.hex()}')
    elif args.command == 'download_piece':
        with open(args.filename, 'rb') as f:
            torrent = Torrent.load(f)

        tracker = Tracker(MY_PEER_ID, torrent)

        address = random.choice(tracker.request()['peers'])

        with Peer(MY_PEER_ID, torrent, address) as peer:
            piece_data = peer.download_piece(args.piece_index)

        if isinstance(piece_data, bytearray):
            hex_data = piece_data.hex()
            with open(args.output, 'wb') as f:
                f.write(hex_data)

            print(f'Piece {args.piece_index} downloaded to {args.output}.')


if __name__ == '__main__':
    main()
