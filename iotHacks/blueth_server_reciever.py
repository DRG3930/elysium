import bluetooth

def start_bluetooth_server():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", bluetooth.PORT_ANY))
    server_socket.listen(1)

    port = server_socket.getsockname()[1]
    bluetooth.advertise_service(server_socket, "SampleServer",
                                service_id=bluetooth.SERIAL_PORT_PROFILE,
                                service_classes=[bluetooth.SERIAL_PORT_PROFILE])

    print(f"Waiting for connection on RFCOMM channel {port}")

    client_socket, client_info = server_socket.accept()
    print(f"Accepted connection from {client_info}")

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            client_socket.send(b"Hello Bluetooth Client!")
    except OSError:
        pass

    client_socket.close()
    server_socket.close()

start_bluetooth_server()
