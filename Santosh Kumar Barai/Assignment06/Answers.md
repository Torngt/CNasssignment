## 1. How long is the IPv6 Header?

The IPv6 header is always **40 bytes** long. This fixed size ensures a consistent overhead across all IPv6 packets.

## 2. What are the different fields in the IPv6 Header?

The IPv6 header consists of the following fields:

- **Version (4 bits)**
- **Traffic Class (8 bits)**
- **Flow Label (20 bits)**
- **Payload Length (16 bits)**
- **Next Header (8 bits)**
- **Hop Limit (8 bits)**
- **Source Address (128 bits)**
- **Destination Address (128 bits)**

## 3. What are the purposes of the different header fields?

- **Version (4 bits)**:
  - Indicates the IP version. For IPv6, this value is 6.

- **Traffic Class (8 bits)**:
  - Used for differentiated services and specifies the priority and type of service for the packet. This is similar to the Type of Service (ToS) field in IPv4.

- **Flow Label (20 bits)**:
  - Used to label sequences of packets that require special handling by the routers, such as real-time data flows. It helps in managing and optimizing packet flow.

- **Payload Length (16 bits)**:
  - Specifies the length of the payload (the data part) following the IPv6 header. The length is expressed in bytes.

- **Next Header (8 bits)**:
  - Indicates the type of header immediately following the IPv6 header. It specifies the protocol used (e.g., TCP, UDP) or an extension header (e.g., Hop-by-Hop Options, Destination Options).

- **Hop Limit (8 bits)**:
  - Limits the number of hops (or routers) that the packet can pass through. Each router decrements this value by one, and the packet is discarded if it reaches zero. It is similar to the Time-to-Live (TTL) field in IPv4.

- **Source Address (128 bits)**:
  - The IPv6 address of the sender of the packet.

- **Destination Address (128 bits)**:
  - The IPv6 address of the intended recipient of the packet.
