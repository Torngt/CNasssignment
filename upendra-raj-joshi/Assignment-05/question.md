### Capture the dns packet


## DNS Packet Structure

DNS (Domain Name System) packets are used for translating domain names into IP addresses and vice versa. A DNS packet contains both a header and one or more questions, answers, authority, and additional records. Here are the main fields in a DNS packet along with explanations of their values:

### DNS Header

1. **Transaction ID (16 bits)**: A unique identifier for the DNS query. This helps match responses to the corresponding queries.
2. **Flags (16 bits)**: Control bits that specify the type of query and response.
   - **QR (1 bit)**: Query (0) or Response (1).
   - **Opcode (4 bits)**: Type of query (standard, inverse, or status).
   - **AA (1 bit)**: Authoritative Answer - this bit is valid in responses, and specifies that the responding name server is an authority for the domain name in question.
   - **TC (1 bit)**: Truncation - specifies that this message was truncated due to length greater than that permitted on the transmission channel.
   - **RD (1 bit)**: Recursion Desired - this bit may be set in a query and is copied into the response.
   - **RA (1 bit)**: Recursion Available - this bit is set or cleared in a response, and denotes whether recursive query support is available in the name server.
   - **Z (3 bits)**: Reserved for future use and must be zero.
   - **RCode (4 bits)**: Response code - indicates the status of the response (e.g., No error, Format error, Server failure).
3. **Questions (16 bits)**: The number of questions in the query.
4. **Answer RRs (16 bits)**: The number of answer resource records in the response.
5. **Authority RRs (16 bits)**: The number of authority resource records in the response.
6. **Additional RRs (16 bits)**: The number of additional resource records in the response.

### DNS Question Section

Each question in the question section of a DNS packet has the following fields:
1. **QName**: The domain name being queried.
2. **QType (16 bits)**: The type of the query (e.g., A, AAAA, MX).
3. **QClass (16 bits)**: The class of the query (usually IN for internet).