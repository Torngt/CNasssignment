
# Torrent Client

This project is a simple BitTorrent client implemented in Python. It includes components for handling torrents, communicating with trackers, and interacting with peers to download pieces of files. The client supports operations such as decoding torrent files, retrieving torrent information, getting peers from a tracker, performing handshakes, and downloading pieces.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [License](#license)

## Features
- Decode bencoded data from torrent files
- Retrieve and display torrent metadata
- Communicate with a tracker to get a list of peers
- Perform handshakes with peers
- Download pieces of the torrent from peers

## Installation
1. Clone the repository:
   \`\`\`
   git clone https://github.com/yourusername/torrent-client.git
   cd torrent-client
   \`\`\`
2. Install the dependencies:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

## Usage
You can use the provided command-line interface to interact with the torrent client. The available commands are:

- `decode`: Decode bencoded data from a torrent file.
- `info`: Retrieve and display torrent metadata.
- `peers`: Communicate with a tracker to get a list of peers.
- `handshake`: Perform a handshake with a peer.
- `download_piece`: Download a piece of the torrent from a peer.

### Examples
1. Decode a torrent file:
   \`\`\`
   python main.py decode "d8:announce13:http://...e"
   \`\`\`

2. Get torrent info:
   \`\`\`
   python main.py info example.torrent
   \`\`\`

3. Get peers from tracker:
   \`\`\`
   python main.py peers example.torrent
   \`\`\`

4. Perform a handshake with a peer:
   \`\`\`
   python main.py handshake example.torrent 127.0.0.1:6881
   \`\`\`

5. Download a piece from a peer:
   \`\`\`
   python main.py download_piece example.torrent 0 -o piece_0.dat
   \`\`\`

## Code Overview

### Torrent Class
The `Torrent` class handles loading and parsing torrent files. It includes methods for computing piece lengths and iterating over blocks within a piece.

### Tracker Class
The `Tracker` class communicates with the tracker specified in the torrent file to obtain a list of peers. It sends HTTP requests to the tracker and parses the response.

### Peer Class
The `Peer` class manages the connection to a peer, including the handshake process and downloading pieces. The `handshake` method is particularly important, as it establishes the connection and verifies the peer.

#### Handshake Message
The handshake message is a crucial part of the BitTorrent protocol. It is the first message sent by both parties and includes the protocol identifier, reserved bytes, the info hash of the torrent, and the peer ID. Here’s the detailed structure:
- `PSTR`: The protocol identifier (`BitTorrent protocol`).
- `reserved`: Eight reserved bytes.
- `info_hash`: The SHA-1 hash of the torrent’s info dictionary.
- `peer_id`: A unique identifier for the peer.

### Messages Module
This module defines various message types used in the BitTorrent protocol, such as `ChokeMessage`, `UnchokeMessage`, `InterestedMessage`, `PieceMessage`, etc. The `HandshakeMessage` is especially important for initiating communication between peers.

## License
This project is licensed under the MIT License.


