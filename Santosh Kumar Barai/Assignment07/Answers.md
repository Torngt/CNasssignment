## Value of Prefix in Link Local Address Format
In IPv6, link-local addresses are used for communication within a single network segment. The prefix for link-local addresses is FE80::/10. This means the first 10 bits of a link-local address are fixed as 1111 1110 10, which translates to FE80 in hexadecimal. The typical format of a link-local address is written as FE80::/64, where the remaining bits are used for the interface identifier.

## TCP Header

The TCP (Transmission Control Protocol) header is used to ensure reliable communication between devices over a network. The header is at least 20 bytes long, but it can be longer if options are included.

### TCP Header Fields

1. **Source Port (16 bits)**: The port number of the sending application.
2. **Destination Port (16 bits)**: The port number of the receiving application.
3. **Sequence Number (32 bits)**: The sequence number of the first byte in the segment.
4. **Acknowledgment Number (32 bits)**: The next sequence number that the sender of the segment is expecting to receive.
5. **Data Offset (4 bits)**: The size of the TCP header in 32-bit words. Indicates where the data begins.
6. **Reserved (3 bits)**: Reserved for future use and should be set to zero.
7. **Flags (9 bits)**: Control flags that include:
   - **URG**: Urgent Pointer field significant
   - **ACK**: Acknowledgment field significant
   - **PSH**: Push Function
   - **RST**: Reset the connection
   - **SYN**: Synchronize sequence numbers
   - **FIN**: No more data from sender
8. **Window Size (16 bits)**: The size of the receive window, which specifies the number of bytes the sender is willing to receive.
9. **Checksum (16 bits)**: Used for error-checking the header and data.
10. **Urgent Pointer (16 bits)**: If the URG flag is set, this field indicates the offset from the sequence number where the urgent data ends.
11. **Options (variable length)**: Optional fields that may be used for various purposes, such as window scaling and timestamps.


## UDP Header

The UDP (User Datagram Protocol) header is simpler and shorter than the TCP header. It is 8 bytes (64 bits) in size.

### UDP Header Fields

1. **Source Port (16 bits)**: The port number of the sending application.
2. **Destination Port (16 bits)**: The port number of the receiving application.
3. **Length (16 bits)**: The length of the UDP header and the encapsulated data.
4. **Checksum (16 bits)**: Used for error-checking the header and data.


