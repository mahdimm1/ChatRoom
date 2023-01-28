
import socket
import threading

# Global vars
from settings import SOCKET_PORT, SOCKET_ADDRESS

clients = []
users = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except Exception as e:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            user = users[index]
            broadcast('User {} exited!!'.format(user).encode('ascii'))
            users.remove(user)
            break


def receive_msg():
    while True:
        client, address = server.accept()
        client.send('NAME'.encode('ascii'))
        user = client.recv(1024).decode('ascii')
        users.append(user)
        clients.append(client)

        print(f'{user} is connected: {str(address)}')
        broadcast('Welcome {}!'.format(user).encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == '__main__':
    # Bind port
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SOCKET_ADDRESS, SOCKET_PORT))
    server.listen()

    print(f'Chat Server: {SOCKET_ADDRESS}:{SOCKET_PORT}')
    receive_msg()

