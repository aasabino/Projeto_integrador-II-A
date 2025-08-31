from socket import *

# Configuração do cliente
HOST = 'localhost'
PORTA = 2000

while True:

    #Estabelecendo conexão
    cliente = socket(AF_INET, SOCK_STREAM)
    cliente.connect((HOST, PORTA))

    #Envia dados
    login = input('Digite seu login:')
    senha = input('Digite sua senha:')
    
    #Use a função encode para enviar os dados codificados
    cliente.send(login.encode())
    cliente.send(senha.encode())

    #Recebendo dados e decodificando para string novamente
    resposta = cliente.recv(1024).decode()
    print(resposta)

    cliente.close()

    if resposta == 'Bem vindo Andrey':
        break
