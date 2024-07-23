# IPv4 Header Fields

## Version (4 bits)
Indicates the IP version. For IPv4, this value is always 4 (0100) and for IPv6 the value is 6 (0110).
Here, In this case the value is 0100 i.e 4 hence the ip address is IPv4

## IHL (Internet Header Length) (4 bits)
Specifies the length of the IP header in 32-bit words. The minimum value is `5(0101)` (indicating a 20-byte header), and the maximum value is `15(1111)` (indicating a 60-byte header).

Here in this case it is '0101(5)' which is 20 bytes

## Type of Service (ToS) / Differentiated Services (DS) (8 bits)
Specifies the quality of service and priority of the packet. This field includes sub-fields such as the Differentiated Services Code Point (DSCP) and Explicit Congestion Notification (ECN).

## Total Length (16 bits)
Specifies the total length of the IP packet (header + data) in bytes. The minimum value is 20 bytes (header only), and the maximum value is 65,535 bytes.
Here, In this case it is 40 byte and header length is 20 byte. The length of data is 20 bytes.

## Identification (16 bits)
Used for uniquely identifying the group of fragments of a single IP datagram. Each fragment of a datagram has the same identification value.

## Flags (3 bits)
Controls fragmentation. The three bits are:
- Reserved bit (always set to 0)
- Don't Fragment (DF) bit
- More Fragments (MF) bit  

Here, the don't fragment bit is set '1'
## Fragment Offset (13 bits)
Indicates the position of the fragment's data relative to the beginning of the original unfragmented datagram. Measured in 8-byte blocks.  

Here it is 0 means the data is not fragmented.

## Time to Live (TTL) (8 bits)
Specifies the maximum number of hops (routers) the packet can traverse. Each router decreases the TTL by 1. When TTL reaches 0, the packet is discarded. Typical values are 64, 128, or 255.

Here, it is 128.

## Protocol (8 bits)
Indicates the next-level protocol used in the data portion of the IP datagram. Common values include:
- `1` for ICMP
- `6` for TCP
- `17` for UDP

Here, the value is 17 indicating the next protocol is TCP.

## Header Checksum (16 bits)
Used for error-checking the IP header. Routers recalculate the checksum whenever the header is modified.

## Source Address (32 bits)
Specifies the IPv4 address of the sender.

Here, in this case it is 192.168.16.102 which my ip address.

## Destination Address (32 bits)
Specifies the IPv4 address of the receiver.

Here, it is 103.10.30.34 which ip adress of abuse@vianet.com.np
