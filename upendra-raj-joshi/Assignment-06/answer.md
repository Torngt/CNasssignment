
## IPv4 Header Structure

The IPv4 header is typically 20 bytes in size, though it can be larger if options are used. Here are the main fields in an IPv4 header along with explanations of their values:

1. **Version (4 bits)**: Indicates the IP version (4 for IPv4).
2. **Header Length (4 bits)**: Specifies the size of the header in 32-bit words. A typical value is 5 (for a 20-byte header).
3. **Type of Service (ToS) (8 bits)**: Specifies the priority and handling of the packet. Common values include 0x00 (normal priority).
4. **Total Length (16 bits)**: The entire packet size, including header and data, in bytes. For example, a value of 60 indicates the packet is 60 bytes long.
5. **Identification (16 bits)**: Used for uniquely identifying the group of fragments of a single IP datagram.
6. **Flags (3 bits)**: Control or identify fragments.
   - **Reserved**: Must be zero.
   - **Don't Fragment (DF)**: Prohibits fragmentation. A value of 1 means fragmentation is not allowed.
   - **More Fragments (MF)**: Indicates more fragments will follow. A value of 0 means this is the last fragment.
7. **Fragment Offset (13 bits)**: Specifies the position of the fragment in the original datagram. A value of 0 means this is the first fragment.
8. **Time to Live (TTL) (8 bits)**: Limits the lifespan of the packet, decrementing by 1 at each hop. A value of 64 is typical and provides a maximum of 64 hops.
9. **Protocol (8 bits)**: Indicates the protocol used in the data portion (e.g., TCP, UDP). A value of 6 indicates TCP.
10. **Header Checksum (16 bits)**: Error-checking the header. A correct checksum ensures the header has no errors. For example, 0xb1e6 (correct).
11. **Source IP Address (32 bits)**: The IP address of the sender. For example, 192.168.1.2.
12. **Destination IP Address (32 bits)**: The IP address of the receiver. For example, 192.168.1.1.
13. **Options (variable)**: Additional options, such as security settings or route info. These are not always present.
