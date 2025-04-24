import socket

def basic_socket_info():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(f"Socket created: {s}")
    print(f"Socket family: {s.family}")
    print(f"Socket type: {s.type}")
    print(f"Socket protocol: {s.proto}")
    
    # Get the local machine name and IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"Hostname: {hostname}")
    print(f"Local IP: {local_ip}")
    
    # Close the socket
    s.close()

if __name__ == "__main__":
    basic_socket_info()

"""
This script introduces basic socket concepts:
1. Creating a socket object
2. Understanding socket properties (family, type, protocol)
3. Getting local machine information

Key points:
- socket.AF_INET: IPv4 address family
- socket.SOCK_STREAM: TCP socket type

Applications:
1. Network programming fundamentals
2. Understanding the basics of client-server communication
3. Preparing for more advanced socket operations
"""