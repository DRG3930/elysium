import socket

def start_wifi_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('your_server_ip_address', 12345))  # Replace with server IP address

    client_socket.sendall(b'Hello Server!')
    data = client_socket.recv(1024)
    print(f"Received: {data.decode('utf-8')}")

    client_socket.close()

start_wifi_client()
