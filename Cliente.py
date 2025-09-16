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

    if resposta == 'Bem vindo Andrey':
        while True:
            print('\nEscolha uma opção:')
            print('1 - Consultar saldo')
            print('2 - Sacar')
            print('3 - Depositar')
            print('4 - Sair')
            opcao = input('Opção: ')

            cliente.send(opcao.encode())

            if opcao == '1':
                saldo = cliente.recv(1024).decode()
                print('Seu saldo é: R$ {}' .format(saldo))
            elif opcao == '2':
                valor_saque = input('Digite o valor a ser sacado: R$ ')
                cliente.send(valor_saque.encode())
                resposta_saque = cliente.recv(1024).decode()
                print(resposta_saque)
            elif opcao == '3':
                valor_deposito = input('Digite o valor a ser depositado: R$ ')
                cliente.send(valor_deposito.encode())
                resposta_deposito = cliente.recv(1024).decode()
                print(resposta_deposito)
            elif opcao == '4':
                print('Saindo...')
                cliente.close()
                break
            else:
                print('Opção inválida. Tente novamente.')
                cliente.close()
                break
    else:
        print('Tente novamente.')
