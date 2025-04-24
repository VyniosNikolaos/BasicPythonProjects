import socket

def start_tcp_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to {host}:{port}")
        
        while True:
            message = input("Enter message (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break
            
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received: {data.decode()}")

if __name__ == "__main__":
    start_tcp_client()

"""
This script implements a basic TCP client:
1. Creating a socket and connecting to a server
2. Sending user input to the server
3. Receiving and displaying the server's response

Key points:
- s.connect(): Establishes a connection to a remote socket
- s.sendall(): Sends data to the connected socket
- s.recv(): Receives data from the socket

Applications:
1. Interacting with network services
2. Building client-side applications for custom protocols
3. Testing server implementations
"""