
# DHCP

## DHCP Discover:
- **Source Address:** 0.0.0.0
  - **Explanation:** The client uses this address because it does not yet have an IP address. 0.0.0.0 is a placeholder indicating the absence of an assigned IP.
- **Destination Address:** 255.255.255.255
  - **Explanation:** This is a broadcast address used to reach all devices in the local network. The client uses it to ensure that any available DHCP servers will receive the Discover message.

## DHCP Offer:
- **Source Address:** 192.168.16.1
  - **Explanation:** This is the IP address of the DHCP server making the offer.
- **Destination Address:** 255.255.255.255
  - **Explanation:** The DHCP server uses the broadcast address to ensure the client, which may not yet have an IP address, receives the offer.

## DHCP Request:
- **Source Address:** 0.0.0.0
  - **Explanation:** The client is still using 0.0.0.0 because it has not yet been assigned an IP address.
- **Destination Address:** 255.255.255.255
  - **Explanation:** The request is broadcasted to ensure that the DHCP server receives it.

## DHCP Acknowledge (ACK):
- **Source Address:** 192.168.16.1
  - **Explanation:** This is the IP address of the DHCP server acknowledging the client's request.
- **Destination Address:** 192.168.16.102
  - **Explanation:** The DHCP server sends the ACK directly to the client using the newly assigned IP address, confirming that the client can use this IP.

## Why These Addresses Are Used:

### Broadcast Address (255.255.255.255):
- Used for Discover and Offer messages to ensure that all devices, especially those without an IP address, can receive the message. This is essential for clients to find and communicate with DHCP servers.

### Source Address (0.0.0.0):
- Used by clients before they have been assigned an IP address. It indicates that the client has no IP address yet.

### DHCP Server Address (192.168.16.1):
- The specific address of the DHCP server in the network. It is used as the source address in Offer and ACK messages to identify the server to the client.

### Client's Assigned Address (192.168.16.102):
- The IP address assigned to the client by the DHCP server. It is used as the destination in the ACK message to confirm the lease.
