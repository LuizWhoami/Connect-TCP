import socket

host = '127.0.0.1'
port = 9998

#criar um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectar  o cliente
client.connect((host,port))

#enviar alguns dados
client.send("ABC")

# receber alguns dados
resposta = client.recv(4096)

print(resposta.decode())
client.close()