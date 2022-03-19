#! /usr/bin/env python3

import socket
import codecs

def msg_resposta(msg):
	aux = codecs.decode(msg,'UTF-8')
	resposta = 'A mensagem enviada pelo cliente é: ' + aux
	msg_servidor = bytes(resposta,'UTF-8')
	return msg_servidor
	
	
HOST = '127.0.0.1'
PORTA = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORTA))
s.listen()
print ("\n\nAguardando conexão de um cliente...")
conexao, endereco = s.accept()

print("\n\nConectado em: ", endereco)

while True:
	dados = conexao.recv(1024)
	resposta = msg_resposta(dados)
	
	if not dados:
		print("\n\nSem mais dados. Fechando conexão.\n\n")
		conexao.close()
		break
	
	print("\n\n Mensagem recevida do cliente: ", codecs.decode(dados,'UTF-8'))
	
	conexao.sendall(resposta)
	

	
	

