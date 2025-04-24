import socket
import select

def non_blocking_server(host='127.0.0.1', port=65434):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    server_socket.setblocking(False)

    inputs = [server_socket]
    outputs = []
    message_queues = {}

    print(f"Non-blocking server listening on {host}:{port}")

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        
        for s in readable:
            if s is server_socket:
                connection, client_address = s.accept()
                print(f"New connection from {client_address}")
                connection.setblocking(False)
                inputs.append(connection)
                message_queues[connection] = []
            else:
                data = s.recv(1024)
                if data:
                    print(f"Received '{data.decode()}' from {s.getpeername()}")
                    message_queues[s].append(data)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    print(f"Closing {s.getpeername()}")
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                    del message_queues[s]

        for s in writable:
            try:
                next_msg = message_queues[s].pop(0)
            except IndexError:
                outputs.remove(s)
            else:
                s.send(next_msg.upper())

        for s in exceptional:
            print(f"Handling exceptional condition for {s.getpeername()}")
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_queues[s]

if __name__ == "__main__":
    non_blocking_server()

"""
This script demonstrates non-blocking socket operations:
1. Setting up a non-blocking server socket
2. Using select to manage multiple connections
3. Handling I/O operations asynchronously

Key points:
- s.setblocking(False): Sets the socket to non-blocking mode
- select.select(): Monitors multiple socket objects for I/O events
- Separate lists for input, output, and exceptional conditions

Applications:
1. Building high-performance network servers
2. Handling multiple client connections simultaneously
3. Implementing event-driven network programming
4. Creating responsive network applications
"""