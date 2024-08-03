## connection initialization, connection maintenance, and connection termination.

### 1. **Connection Initialization**

This is the process where a TCP connection is established between a client and a server. It involves a handshake procedure known as the **three-way handshake**.

**Packets Involved:**
- **SYN Packet**: The client (my computer 172.30.184.101) initiates the connection by sending a SYN packet to the server(20.37.198.118 which microsoft visual studio server for temporary hosting my webserver). This packet has the SYN flag set.
  - `50944 → 443 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM TSval=2148248622 TSecr=0 WS=128`

- **SYN-ACK Packet**: The server responds with a SYN-ACK packet, acknowledging the SYN request and sending its own SYN to the client.
  - `443 -> 50944 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1440 WS=256 SACK_PERM TSval=907484393`

- **ACK Packet**: The client acknowledges the server’s response with an ACK packet.
  - `50944 → 443 [ACK] Seq=1 Ack=1 Win=64256 Len=0 TSval=2148248906 TSecr=907484393`

### 2. **Connection Maintenance**

Once the connection is established, data can be transferred between the client and server. This phase includes sending and receiving data packets, maintaining the connection’s state.

**Packets Involved:**
- **TLS Handshake Messages**: During this phase, encrypted communication is established using TLS/SSL. Messages include `Client Hello`, `Server Hello`, and other TLS handshake messages.
  - `Client Hello  to dc.services.visualstudio.com)`
- `443 -> 50944 server sends acknowledgemet`
  - `Server Hello to client my computer`
  - `Change Cipher Spec`
  - `Finished`
  The protocol inside TLS running is HTTP for my webserver.

- **Application Data**: This phase contains the actual data being transferred once after TLS maintainance is finished, marked as `Application Data`
Here:
  - `443 → 50944 [PSH, ACK] Seq=4384 Ack=844 Win=4194560 Len=124 `
  meaning that server sends acknownledgement and instruction to send the data immediately.
  - `50944 ->443 [ACK] Seq=844 Ack=4508 Win=64128 Len=0`
  The Client sends acknowledgement in respond that i got you now i will send you data.
  And here in case i am uploading file so it goes from my ip to server i.e. 172.30.184.101 to 20.37.198.118 in form of application data.
  Since, the server actually is running into my computer 127.0.0.1(server ip) at port 5000 it comes back to my computer lwhich was stored the data  `here in my case is png file` i uploaded to the server.  

### 3. **Connection Termination**

When the data transfer is complete, the connection is closed gracefully using a termination procedure known as the **four-way handshake**.

**Packets Involved:**
- **FIN Packet**: One side initiates the connection termination by sending a FIN (Finish) packet.
  - `50944-> 443 [FIN, ACK] Seq=1517 Ack=5064 Win=64128 Len=0`

- **ACK Packet**: The other side acknowledges the FIN packet with an ACK.
  - `443 → 50944 [ACK] Seq=5064 Ack=1518 Win=4195328 Len=0`

- **FIN Packet**: The other side sends its own FIN packet to complete the termination process.
  - `443 → 50944 [FIN, ACK] Seq=5064 Ack=1518 Win=4195328 Len=0`

- **ACK Packet**: The initial side acknowledges the final FIN packet.
  - `50944 → 443 [ACK] Seq=1517 Ack=5064 Win=64128 Len=0`

The above last 2 packets would have there here i stoped capturing before wireshark could capture all the termination packets. 