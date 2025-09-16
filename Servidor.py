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
    if login == '1152025100441' and senha == '123456':
        conexao.send('Bem vindo Andrey'.encode())
        saldo = 1000.00

        while True:
            opcao = conexao.recv(1024).decode()
            if opcao == '1':
                conexao.send(str(saldo).encode())
            elif opcao == '2':
                valor_saque = float(conexao.recv(1024).decode())
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    conexao.send('Saque realizado com sucesso. Novo saldo: R$ {:.2f}' .format(saldo).encode())
                else:
                    conexao.send('Saldo insuficiente para saque.'.encode())
            elif opcao == '3':
                valor_deposito = float(conexao.recv(1024).decode())
                saldo += valor_deposito
                conexao.send('Depósito realizado com sucesso. Novo saldo: R$ {:.2f}' .format(saldo).encode())
            elif opcao == '4':
                print('Cliente saiu.')
                conexao.close()
                break
    else:
        conexao.send('loguin ou senha incorretos'.encode())
        conexao.close()
