import socket
HOST = '127.0.0.1'
PORT = 5000
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((HOST , PORT))
    s.listen(1)

    print(f'[+] Server is listening on {HOST}:{PORT}')

    conn , addr = s.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            print("Client disconnected.")
            break


        print("Received:" , data.decode())

    conn.close()
    server.close()


