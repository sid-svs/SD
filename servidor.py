#! /usr/bin/env python3

import socket
import codecs

#esta função concatena a mensagem enviada pelo cliente com uma mensagem a ser enviada na resposta

def msg_resposta(msg): 
	msgString = codecs.decode(msg,'UTF-8') #converte os bytes recebidos em string
	resposta = 'Mensagem recebida do cliente: ' + msgString #concatena a string com a mensagem enviada, criando uma nova mensagem a ser enviada
	msg_servidor = bytes(resposta,'UTF-8') #converte a nova mensagem em bytes para ser enviada ao cliente
	return msg_servidor #retorna os bites usados
	
	
HOST = '127.0.0.1'
PORTA = 50000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST,PORTA))
socket.listen()
print(("\n\nAguardando conexão de um cliente..."))
conexao, endereco = socket.accept()

print("\n\nConexão recebida de: ", endereco)

while True:
	dados = conexao.recv(1024)
	resposta = msg_resposta(dados)
	
	if not dados:
		print("\n\nSem mais dados. echando conexão.\n\n")
		conexao.close()
		break
	
	print("\n\n Mensagem recebida do cliente: ", codecs.decode(dados,'UTF-8'))
	
	conexao.sendall(resposta)
	

	
	

