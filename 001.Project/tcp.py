import threading
import socket
HOST = '127.0.0.1'
PORT = 5000
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    s.bind((HOST , PORT))
    s.listen(5)
    print(f"[+] Server running on {HOST}:{PORT}")


    clients = []

    def broadcasr(msg , sender):
        for client in clients:
            if client != sender:
                try:
                    client.send(msg)
                except:
                    client.close()
                    clients.remove(client)
    def handle_client(conn , addr):
         print(f"[NEW CONNECTION] {addr} connected. ")
         conn.send("Welcome t the chatroom!\n".encode())

         while True:
             try:
                 msg = conn.recv(1024)
                 if not msg :
                     break
                 print(f"[{addr}] {msg.decode().strip()}")
             except:
                 break
         print(f"[DISCONNECTED] {addr}")
         conn.close()
         if conn in  clients:
             clients.remove(conn)
             

    while True:
        conn , addr = s.accept()
        print(f"[CONNECTED] {addr} joined the chat.")
        clients.append(conn)
        thread = threading.Thread(target=handle_client , args=(conn , addr))
        thread.daemon = True
        thread.start()

