# UDP Layer in Wireshark

## UDP Header Structure

The UDP header is much simpler than the TCP header and is typically 8 bytes in size. Here are the main fields in a UDP header:

1. **Source Port (16 bits)**: The port number of the sending application.
2. **Destination Port (16 bits)**: The port number of the receiving application.
3. **Length (16 bits)**: The length of the UDP header and data in bytes.
4. **Checksum (16 bits)**: Used for error-checking the header and data.

## UDP Packet Structure

UDP packets consist of the UDP header and the payload data. The payload can be any data from the application layer, such as DNS queries, DHCP messages, etc.
