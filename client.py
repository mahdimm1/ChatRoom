import socket
import threading

from settings import SOCKET_PORT, SOCKET_ADDRESS


def receive_msg():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NAME':
                client.send(name.encode('ascii'))
            else:
                print(f'--------{message}')
        except Exception as e:
            print(e)
            client.close()
            break


def send_msg():
    while True:
        message = '[{}]: {}'.format(name, input(''))
        client.send(message.encode('ascii'))


if __name__ == '__main__':
    name = input('Name: ')

    # Connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SOCKET_ADDRESS, SOCKET_PORT))

    # Receiver thread
    receive_thread = threading.Thread(target=receive_msg)
    receive_thread.start()

    # Sender thread
    write_thread = threading.Thread(target=send_msg)
    write_thread.start()