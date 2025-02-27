import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print('[*] Ouvindo IP:{}:{}'.format(IP, PORT))
    while True:
        client, address = server.accept()
        print(f'[*] Conexão aceita do {address[0]}:{address[1]}')
        client_handle = threading.Thread(target=handle_client, args=(client,))
        client_handle.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(4096)
        print(f'[*] Recebido: {request.decode("utf-8")}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()