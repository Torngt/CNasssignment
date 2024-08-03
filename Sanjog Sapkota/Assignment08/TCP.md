TCP (Transmission Control Protocol) ensures reliable, ordered, and error-checked delivery of data between applications running on hosts communicating over an IP network. Here's a clear breakdown of the three main phases of a TCP connection: initialization, maintenance, and termination.

### 1. Connection Initialization

This process is often referred to as the **TCP handshake**. It involves three steps to establish a connection between a client and a server:

- **SYN (Synchronize)**: The client initiates the connection by sending a TCP segment with the SYN flag set. This segment includes an initial sequence number (ISN) that the client will use to start counting bytes in the data it sends.

- **SYN-ACK (Synchronize-Acknowledge)**: The server responds with a segment that has both the SYN and ACK flags set. This segment acknowledges the client’s SYN segment (by including an acknowledgment number) and includes the server’s own initial sequence number.


- **ACK (Acknowledge)**: The client sends a final segment with the ACK flag set to acknowledge the server's SYN-ACK segment. At this point, the connection is established, and data can begin to be exchanged.
![connection initialization](/Sanjog%20Sapkota/Assignment08/photos/connection_int.png)

### 2. Connection Maintenance

Once the connection is established, it needs to be maintained to ensure reliable communication. This involves:

- **Data Transmission**: Data is sent in segments, each with a sequence number. The receiver acknowledges receipt of these segments with ACK segments. This ensures that data is received correctly and in the right order.

- **Flow Control**: TCP uses a flow control mechanism (via the window size) to ensure that the sender does not overwhelm the receiver with too much data too quickly.

- **Error Checking**: Each segment includes a checksum to verify the integrity of the data. If a segment is lost or corrupted, it is retransmitted.

- **Congestion Control**: TCP adjusts the rate of data transmission based on network congestion to avoid overloading the network. This is done using algorithms like slow start, congestion avoidance, and fast recovery.
![connection initialization](/Sanjog%20Sapkota/Assignment08/photos/conn_maint.png)

### 3. Connection Termination

When the communication is done, the connection is terminated gracefully to ensure all data is transmitted and acknowledged. This process involves:

- **FIN (Finish)**: One side (either client or server) sends a segment with the FIN flag set to indicate it has finished sending data. This starts the connection termination process.

- **ACK**: The receiving side acknowledges the FIN segment with an ACK segment. 

- **FIN from Receiver**: The receiver, once it has finished sending all its data, sends its own FIN segment to indicate it’s also done.

- **Final ACK**: The original sender acknowledges the receiver’s FIN segment with a final ACK segment. At this point, the connection is fully closed.
![connection initialization](/Sanjog%20Sapkota/Assignment08/photos/conn_term.png)

Each side of the connection goes through a **four-way handshake** to close the connection, ensuring that all data has been transmitted and acknowledged before the connection is terminated.