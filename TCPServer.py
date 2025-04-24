import socket

def start_tcp_server(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                conn.sendall(data.upper())  # Echo back in uppercase

if __name__ == "__main__":
    # Note: Run this server script in a separate terminal or process.
    start_tcp_server()

"""
This script demonstrates a basic TCP server:
1. Creating a socket and binding it to an address
2. Listening for incoming connections
3. Accepting a client connection
4. Receiving and sending data

Key points:
- s.bind(): Associates the socket with a specific network interface and port
- s.listen(): Enables the server to accept connections
- s.accept(): Waits for an incoming connection

Applications:
1. Building network services
2. Implementing custom protocols
3. Creating multi-client chat servers (with additional logic)
"""