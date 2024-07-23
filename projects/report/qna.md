 # What happens when you type facebook.com and enter in your browser?
When you type facebook.com and press Enter, here is a detailed step-by-step explanation of what happens:

### 1. Application Layer
- **URL Parsing**: The browser parses the URL "www.facebook.com" to identify the protocol (HTTP/HTTPS), the domain name (facebook.com), and the resource path.
- **DNS Resolution**: The browser checks its cache to see if it has a recent DNS record for "www.facebook.com". If not, it queries the local DNS resolver configured on your machine (often your ISP's DNS server).

### 2. DNS Layer

### DNS Query Process


   - When you enter "www.facebook.com" in your browser, the browser first checks its own cache to see if it has a recent DNS record for "www.facebook.com". If not, it queries the operating system's DNS resolver cache.
   - If the DNS resolver cache does not have the record, it forwards the query to the local DNS resolver (usually provided by your ISP).
   - The local DNS resolver checks its own cache for the DNS record. If the record is found, it is returned to the client (your computer).
   - If the record is not found in the cache, the local DNS resolver proceeds with a recursive DNS query.
   - The local DNS resolver sends a query to one of the root DNS servers. The root DNS servers do not know the IP address of "www.facebook.com" but can direct the query to the appropriate Top-Level Domain (TLD) DNS servers.
   - The root DNS servers return a referral to the .com TLD DNS servers.
   - The local DNS resolver then sends the query to one of the .com TLD DNS servers. These servers also do not have the exact IP address but can direct the query to the authoritative DNS servers for "facebook.com".
   - The .com TLD DNS servers return a referral to the authoritative DNS servers for "facebook.com".
   - The local DNS resolver finally sends the query to the authoritative DNS servers for "facebook.com".
   - The authoritative DNS servers have the DNS records for "facebook.com" and respond with the IP address associated with "www.facebook.com".

  **Response Back to Client**:
   - The local DNS resolver receives the response from the authoritative DNS servers and caches the DNS record for future queries.
   - The local DNS resolver then returns the IP address to the client.
   - The browser receives the IP address from the local DNS resolver and uses this IP address to establish a connection to the Facebook server.

### 3. Transport Layer
- **TCP Handshake**: The browser initiates a TCP connection to the IP address returned by the DNS query. This involves a three-step process known as the TCP three-way handshake:
  1. **SYN**: The client sends a TCP SYN (synchronize) packet to the server.
  2. **SYN-ACK**: The server responds with a SYN-ACK (synchronize-acknowledge) packet.
  3. **ACK**: The client sends an ACK (acknowledge) packet back to the server, establishing the connection.

### 4. Network Layer 
- **IP Routing**: The IP packets containing the TCP handshake are routed across the internet from the client to the server. This involves traversing multiple routers and networks.

### 5. Data Link Layer and Physical Layer 
  - **Encapsulation**: The data from the network layer (IP packet) is encapsulated into a data link layer frame. The frame includes a header with information such as source and destination MAC addresses.
  - **Physical Transmission**: The frames are transmitted as electrical signals, light pulses, or radio waves, depending on the physical medium (e.g., copper wire, fiber optics, wireless).

When you send a request from your device, the data follows these steps:(say our device is connected to wi-fi)
1. **Wireless Transmission**: The data is transmitted wirelessly to your router.
2. **Router Processing**: The router decapsulates the data frame, reads the necessary information like IP addresses, and then re-encapsulates the data and sends it to next hop.
3. **Intermediate Hops**: This process of decapsulation and re-encapsulation continues at each hop (e.g., routers and switches) along the path, with the data being adapted for the respective physical media and protocols.
4. **Destination**: The data finally reaches its destination (e.g., Facebook's server), where it is fully processed.

Each hop involves reading the packet's information and preparing it for the next segment of its journey, ensuring that the data is correctly formatted and transmitted across various network segments and devices until it reaches the intended recipient.


### 6. Router Processing and Hops
- **Router Reception**: The first router (gateway) receives the frame.
  - **MAC Address Check**: The router checks the destination MAC address to verify that it is the intended recipient.
  - **Frame Decapsulation**: The router decapsulates the frame to extract the IP packet.
- **IP Routing**: The router examines the destination IP address and consults its routing table to determine the next hop.
  - **Routing Table Lookup**: The routing table contains information about which direction (interface) to forward the packet to reach its destination.
- **Frame Re-encapsulation and Transmission**: The router encapsulates the IP packet in a new frame with appropriate MAC addresses for the next hop and transmitted until it reaches the destination.


### 7. Server-Side Processes
- **Destination Router**: The last router in the chain (close to the Facebook data center) forwards the packet to Facebook's server.
  - **Server Reception**: The server receives the frame, decapsulates it to retrieve the IP packet and then the TCP segment, and finally processes the HTTP request.

### 8. Application Layer(server side)
- When the server receives an HTTP request for the Facebook homepage, it first uses load balancing to direct the request to one of its servers. The server then manages user sessions to ensure the request is associated with the correct user profile. It queries databases to retrieve user-specific content, processes this data, and generates the necessary HTML, CSS, JavaScript, and other resources. Finally, it assembles and sends the complete web page back to the client for rendering in the browser.

### 9. Response Transmission
- **HTTP Response**: The server sends an HTTP response containing the requested resources (HTML, CSS, JavaScript, images) back to the client.
- **TCP Transmission**: The response data is sent over the established TCP connection, broken down into packets.

   When data is sent over a TCP connection, it is broken down into smaller units called **packets**.

    ### **1. Data Segmentation**

    - **Large Data Transfer**: For efficiency and to handle large amounts of data, TCP breaks down the data into smaller, manageable pieces called segments or packets.
   - **Segment Size**: Each segment has a maximum size defined by the Maximum Segment Size (MSS), which is negotiated during the TCP handshake. The MSS is influenced by the Maximum Transmission Unit (MTU) of the network path.

   ### **2. TCP Packet Construction**

   - **TCP Header**: Each segment includes a TCP header with essential information such as:
  - **Sequence Number**: Indicates the position of the segment’s data in the overall message.
  - **Acknowledgment Number**: Used to confirm receipt of segments.
  - **Flags**: Control bits like SYN, ACK, FIN that manage the connection state.
  - **Window Size**: Controls the flow of data to prevent overwhelming the receiver.
  
  - **Payload**: The actual data portion of the segment, which is part of the original data stream.

  ### **3. Transmission**

  - **Encapsulation**: The TCP segment is encapsulated in an IP packet, which includes its own header with source and destination IP addresses.
  - **Data Link Layer**: The IP packet is then encapsulated in a frame for transmission over the network, with headers appropriate for the local network technology (e.g., Ethernet).



### 10. Client-Side Rendering
- **Data Link and Physical Layer**: The response packets travel back through the internet, following the reverse path through routers and networks.
- **Network and Transport Layer**: The server collects incoming packets in a buffer. The client's network stack reassembles the TCP packets into the original HTTP response.TCP reconstructs the data stream based on sequence numbers, ensuring that the data is ordered correctly and reassembled into the complete message.
 - **Acknowledgment**: As packets are received, the server sends acknowledgments to the sender to confirm receipt and request retransmission if any packets are missing or corrupted.
- **Application Layer**: The browser processes the HTTP response, parsing the HTML and making additional requests for resources like images, CSS files, and JavaScript files.

### 11. User Interaction
- **JavaScript Execution**: The browser executes any JavaScript code, enabling dynamic content and interactivity.
- **User Input**: The user can now interact with the webpage, triggering further requests and updates as needed.

Hence, typing "www.facebook.com" and pressing Enter initiates a complex series of steps across multiple layers of the network, involving DNS resolution, TCP/IP communication, routing through multiple hops, and final rendering of the webpage in your browser. Each layer and step is crucial for successfully delivering the requested content to your device.