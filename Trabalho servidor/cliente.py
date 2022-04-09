import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("192.168.0.1", 80))
server.send(str.encode("Hello World!!!"))
Servidor = server.recv(2048)
print("Mensagem recebida!!!", Servidor.decode())