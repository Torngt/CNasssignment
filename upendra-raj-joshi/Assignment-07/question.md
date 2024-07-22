## Capture IPv6 packet in wireshark then Explain its values


## IPv6 Header Structure

The IPv6 header is simpler than the IPv4 header and is always 40 bytes in size. Here are the main fields in an IPv6 header along with explanations of their values:

1. **Version (4 bits)**: Indicates the IP version (6 for IPv6).
2. **Traffic Class (8 bits)**: Similar to the Type of Service field in IPv4, it specifies the priority and handling of the packet.
3. **Flow Label (20 bits)**: Used to identify flows of packets that require special handling.
4. **Payload Length (16 bits)**: The length of the payload in bytes, excluding the IPv6 header.
5. **Next Header (8 bits)**: Indicates the type of header immediately following the IPv6 header. Common values include 6 (TCP), 17 (UDP), and 58 (ICMPv6).
6. **Hop Limit (8 bits)**: Similar to the TTL field in IPv4, it limits the lifespan of the packet, decrementing by 1 at each hop.
7. **Source Address (128 bits)**: The IPv6 address of the sender.
8. **Destination Address (128 bits)**: The IPv6 address of the receiver.

## IPv6 Packet Structure

An IPv6 packet consists of the IPv6 header and the payload data. The payload can include optional extension headers and the data from the transport layer, such as TCP or UDP segments.
