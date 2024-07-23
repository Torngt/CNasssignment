## TCP Connection Establishment

TCP (Transmission Control Protocol) is connection-oriented, which means it establishes a connection before transmitting data. This process is known as the TCP three-way handshake.

### TCP Three-Way Handshake

1. **SYN (Synchronize)**:
   - The client sends a TCP segment with the SYN flag set to the server to initiate a connection.
   - This segment includes an initial sequence number (ISN).

2. **SYN-ACK (Synchronize-Acknowledge)**:
   - The server responds with a TCP segment that has both the SYN and ACK flags set.
   - The SYN flag indicates the server's initial sequence number, and the ACK flag acknowledges the client's ISN (client's ISN + 1).

3. **ACK (Acknowledge)**:
   - The client responds with a TCP segment that has the ACK flag set.
   - This segment acknowledges the server's ISN (server's ISN + 1).

   ## TCP Connection Termination

TCP connections are terminated using a four-step process:

1. **FIN (Finish)**: The client sends a FIN segment to indicate it has finished sending data.
2. **ACK (Acknowledge)**: The server acknowledges the client's FIN segment.
3. **FIN (Finish)**: The server sends a FIN segment to indicate it has finished sending data.
4. **ACK (Acknowledge)**: The client acknowledges the server's FIN segment.
