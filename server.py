import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "localhost" #socket.gethostbyname(socket.gethostname()) #get IP address by name
# print(socket.gethostname())



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
server.bind(ADDR)


def handle_client(conn, addr):
    print(addr, " connected.")
    connected = True
    while connected:
        #determining message length
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)

            msg = conn.recv(msg_length).decode(FORMAT)
            print(addr," said: ",msg)

            #handling disconnection cleanly
            if msg==DISCONNECT_MESSAGE:
                connected = False
            conn.send("Msg Received".encode(FORMAT))


def start():
    server.listen()
    print("Server is listening on ", SERVER)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("Acting connections: {}".format(threading.active_count()-1))

print("Starting server...")
start()
