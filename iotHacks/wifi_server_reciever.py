import socket

def start_wifi_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Use your local IP address
    server_socket.listen(1)
    print("Waiting for a connection...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")
        conn.sendall(b'Hello Client!')

    conn.close()
    server_socket.close()

start_wifi_server()
