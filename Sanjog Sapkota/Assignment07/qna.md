## Questions
 # What is the value of prefix in link local address format?
  - a link local address is used for communication within a single network segment. The prefix for a link-local address is always fe80::/10. This means that the first 10 bits of the address are fixed as 1111 1110 10, and the rest of the address is used for interface identification.

# What is the size of UDP header? What are the different fields? Describe its fields.
  - The UDP  header is  8 bytes (64 bits) long.
      - **Source Port (2 bytes)**: Identifies the port at the source of the datagram.
      - **Destination Port (2 bytes)**: Identifies the port at the destination of the datagram.
      - **Length (2 bytes)**: Specifies the length of the UDP header and data in bytes.
      - **Checksum (2 bytes)**: Used for error-checking the header and data.It is used to detect errors that may have occurred during transmission. If the checksum calculation does not match the checksum field, the datagram is considered corrupted.


# What is the size of TCP header, What are the different fields?Describe its fields.
  - The TCP (Transmission Control Protocol) header has a minimum size of 20 bytes and maximum of 60 bytes.
    - **Source Port (2 bytes)**: Identifies the port number of the sender.
    - **Destination Port (2 bytes)**: Identifies the port number of the receiver.
    - **Sequence Number (4 bytes)**: Used for data ordering and reliability; specifies the position of the first byte of data in the segment.
    - **Acknowledgment Number (4 bytes)**: Indicates the next expected byte from the receiver; used for acknowledging received data.
    - **Data Offset (4 bits)**: Also known as the Header Length field, this specifies the length of the TCP header in 32-bit words. The minimum value is 5, which means the header is 20 bytes long.
    - **Reserved (3 bits)**: Reserved for future use and should be set to zero.
    - **Flags (9 bits)**: Contains control flags, such as SYN, ACK, FIN, RST, URG, and PSH.
    - **Window Size (2 bytes)**: Specifies the size of the sender's receive window (the amount of data the sender is willing to receive).
    - **Checksum (2 bytes)**: Provides error-checking information for the TCP header and data.
    - **Urgent Pointer (2 bytes)**: Points to the sequence number of the byte following urgent data, if the URG flag is set.

    The other 40 bytes includes Maximum Segment Size (MSS), Window Scale, Timestamps, and others. The length of the options field is determined by the Data Offset field.

# Locate a UDP packet in wireshark and relate the values with the fields.
   - **Source Port (2 bytes)**:"be ef" (48879) which is the port number of source.
   - **Destination Port (2 bytes)**: "01 bb" (443) which is the port number of destination.
   - **Length (2 bytes)**: "00 29"  (41) which is the length of UDP header and data in bytes.
   - **Checksum (2 bytes)**:"eb 72" i.e. 0xeb72 Used for error-checking the header and data.
# Locate a TCP package in wireshark and explain why the field have the value that they have.
   - **Source Port (2 bytes)**: "01 bb"(443) source port number.
   - **Destination Port (2 bytes)**:"8f ec"(36844) destination port number.
   - **Sequence Number (4 bytes)**: "45 a9 0c 03" (1168706563) specifies the position of the first byte of data in the segment.
   - **Acknowledgment Number (4 bytes)**: "0a f1 9f be" (183607230) Indicates the next expected byte from the receiver; used for acknowledging received data.
   - **Data Offset (4 bits)**: value = 8  Also known as the Header Length field, this specifies the length of the TCP header in 32-bit words. The minimum value is 5, which means the header is 20 bytes long.
   - **Reserved (3 bits)**:value= 0x000 Reserved for future use and should be set to zero.
   - **Flags (9 bits)**:0x10(0b001000) i.e. The segment is acknowledging the receipt of previously sent data. This indicates that the Acknowledgment Number field in the TCP header contains a valid acknowledgment value. 
   - **Window Size (2 bytes)**: "00 08" (8)i.e. size of the sender's receive window is  8 bytes (the amount of data the sender is willing to receive).
   - **Checksum (2 bytes)**:"b1 dd" 0xb1dd Provides error-checking information for the TCP header and data.
   - **Urgent Pointer (2 bytes)**: "00 00"it means the segment does not require special handling for urgent data.

**options**
 - **No-operation(2 bytes)**:"01 01"
 - **time stamp option(1 byte)**: "08"
 - **length(1 byte)**: "0a" (10)
 - **timestamp value(4 bytes)**:"b2 0s 91 cb"(2986709451)
 - **timestamp echo reply(4 bytes)**:"e7 d8 1a fa"(3889699578)