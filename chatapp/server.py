import socket
import threading
from encryption import encrypt_message

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()
print("Server is running on port 9999... Waiting for clients...")


clients = []

def broadcast(message):
    encrypted = encrypt_message(message)
    for client in clients:
        client.send(encrypted)

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            broadcast(msg)
        except:
            clients.remove(client)
            client.close()
            break

while True:
    client, addr = server.accept()
    clients.append(client)
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()
