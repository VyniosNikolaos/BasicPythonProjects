import socket

def start_udp_client(host='127.0.0.1', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print(f"UDP client ready to send to {host}:{port}")
        
        while True:
            message = input("Enter message (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break
            
            s.sendto(message.encode(), (host, port))
            data, server = s.recvfrom(1024)
            print(f"Received from {server}: {data.decode()}")

if __name__ == "__main__":
    # Note: Run this client script in a separate terminal or process after starting the UDP server.
    start_udp_client()

"""
This script implements a basic UDP client:
1. Creating a UDP socket
2. Sending datagrams to a server
3. Receiving responses from the server

Key points:
- No explicit connection is established in UDP
- s.sendto(): Sends a datagram to a specific address
- s.recvfrom(): Receives a datagram and the address of the sender

Applications:
1. Implementing clients for UDP-based services
2. Building lightweight network utilities
3. Creating applications where low latency is crucial
"""