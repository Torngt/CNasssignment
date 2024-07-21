# TCP Layer in Wireshark

## TCP Header Structure

The TCP header is typically 20 bytes in size, though it can be larger if options are used. Here are the main fields in a TCP header:

1. **Source Port (16 bits)**: The port number of the sending application.
2. **Destination Port (16 bits)**: The port number of the receiving application.
3. **Sequence Number (32 bits)**: Used to keep track of the order of data segments.
4. **Acknowledgment Number (32 bits)**: If the ACK flag is set, this field contains the next sequence number that the sender of the segment is expecting to receive.
5. **Data Offset (4 bits)**: Indicates where the data begins. It specifies the size of the TCP header in 32-bit words.
6. **Reserved (3 bits)**: Reserved for future use and should be set to zero.
7. **Flags (9 bits)**: Control flags used for managing the state of the connection. The most common flags are:
   - **URG (Urgent)**: Indicates that the Urgent pointer field is significant.
   - **ACK (Acknowledgment)**: Indicates that the Acknowledgment field is significant.
   - **PSH (Push Function)**: Asks to push the buffered data to the receiving application.
   - **RST (Reset)**: Resets the connection.
   - **SYN (Synchronize)**: Initiates a connection.
   - **FIN (Finish)**: Indicates that the sender has finished sending data.
8. **Window Size (16 bits)**: The size of the receive window, which specifies the number of bytes the sender is willing to receive.
9. **Checksum (16 bits)**: Used for error-checking the header and data.
10. **Urgent Pointer (16 bits)**: If the URG flag is set, this field is used to indicate a priority segment of data.
11. **Options (variable)**: May contain various options, such as Maximum Segment Size (MSS), Window Scaling, and Timestamp.

## TCP Flags

- **URG (1 bit)**: Urgent pointer field significant.
- **ACK (1 bit)**: Acknowledgment field significant.
- **PSH (1 bit)**: Push function.
- **RST (1 bit)**: Reset the connection.
- **SYN (1 bit)**: Synchronize sequence numbers.
- **FIN (1 bit)**: No more data from sender.

## TCP Connection Establishment and Termination

TCP uses a three-way handshake to establish a connection:
1. **SYN**: The client sends a SYN packet to the server.
2. **SYN-ACK**: The server responds with a SYN-ACK packet.
3. **ACK**: The client sends an ACK packet, and the connection is established.

To terminate a connection, a four-step process is typically used:
1. **FIN**: The client sends a FIN packet.
2. **ACK**: The server acknowledges with an ACK.
3. **FIN**: The server sends a FIN packet.
4. **ACK**: The client responds with an ACK.

## Data Transmission and Acknowledgment

- **Sequence Numbers**: Used to ensure data is delivered in order and to detect missing segments.
- **Acknowledgment Numbers**: Used to confirm receipt of data and indicate the next expected byte.
- **Window Size**: Controls the flow of data and helps in congestion control.

## Error Detection and Handling

- **Checksum**: Ensures the integrity of the header and data.
- **Retransmissions**: Lost or corrupted segments are retransmitted based on acknowledgment and timeout mechanisms.

## TCP Options

- **Maximum Segment Size (MSS)**: Specifies the largest segment that can be received.
- **Window Scaling**: Allows for larger window sizes.
- **Selective Acknowledgment (SACK)**: Allows the receiver to acknowledge non-contiguous blocks of data.
- **Timestamps**: Used for round-trip time measurement and protection against wrapped sequence numbers.

