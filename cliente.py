#!usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORTA = 50000


socketAberto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketAberto.connect((HOST, PORTA))

string = str.encode("Olá servidor")

socketAberto.sendall(string)
dados_recebidos = socketAberto.recv(1024)

print("\n\nMensagem enviada pelo servidor: \n\n", dados_recebidos.decode())

