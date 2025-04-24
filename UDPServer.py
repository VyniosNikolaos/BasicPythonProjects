import socket

def start_udp_server(host='127.0.0.1', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"UDP server listening on {host}:{port}")
        
        while True:
            data, addr = s.recvfrom(1024)
            print(f"Received message from {addr}: {data.decode()}")
            
            response = data.upper()
            s.sendto(response, addr)

if __name__ == "__main__":
    start_udp_server()

"""
This script demonstrates a basic UDP server:
1. Creating a UDP socket and binding it to an address
2. Receiving datagrams from clients
3. Sending responses back to clients

Key points:
- socket.SOCK_DGRAM: Specifies a UDP socket
- s.recvfrom(): Receives a datagram and the address of the sender
- s.sendto(): Sends a datagram to a specific address

Applications:
1. Implementing lightweight, connectionless protocols
2. Building real-time applications (e.g., online gaming, VoIP)
3. Creating services where packet loss is acceptable
"""