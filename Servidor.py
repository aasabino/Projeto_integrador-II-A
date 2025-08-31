from socket import *

#Configurando o servidor
HOST = 'localhost'
PORTA = 2000

while True:
    #Estabelecendo conexão
    servidor = socket(AF_INET, SOCK_STREAM)
    servidor.bind((HOST, PORTA))
    servidor.listen(1)
    print('sevidor conectado em {} na porta {}' .format(HOST, PORTA))


    #Aceitando conexões
    conexao, endereco = servidor.accept()
    print('Conexão estabelecida')

    #recebendo dados e decodificando para string novamente
    login = conexao.recv(1024).decode()
    senha = conexao.recv(1024).decode()
    
    #Envia uma reposta codificada
    if login == 'admin' and senha == 'admin':
        conexao.send('Bem vindo admin'.encode())
        conexao.close()
        break #sai do loop se o login for correto
    else:
        conexao.send('loguin ou senha incorretos'.encode())
        conexao.close()
