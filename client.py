import socket
import random

HOST = '127.0.0.1'
PORT = 5000

opcoesJogadas = ['Pedra', 'Papel', 'Tesoura']

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM identificação do TCP

sock.connect((HOST, PORT)) # Parênteses duplo pq o connect tem apenas um parâmetro (Realiza conexão com o servidor)

while True:

    opcao1 = int(input("\n* Escolha uma opção:\n 1- Palpite aleatório\n 2- Informar um palpite\n 0- Para encerrar.\n -> Opcao: "))

    if (opcao1 == 1):
        mensagemEnvioClient = random.choice(opcoesJogadas)

    if (opcao1 == 2):
        opcao2 = int(input("\n* Ecolha o palpite:\n 1- Pedra\n 2- Papel\n 3- Tesoura\n -> Opcao: "))

        if (opcao2 == 1):
            mensagemEnvioClient = 'Pedra'
        elif (opcao2 == 2):
            mensagemEnvioClient = 'Papel'
        elif (opcao2 == 3):
            mensagemEnvioClient = 'Tesoura'
    
    if (opcao1 == 0):
        print("\nConexão encerrada!\n")
        sock.close()
        break

    sock.sendall(str.encode(mensagemEnvioClient)) # Enviar mensagem para o servidor

    print("\n-> Palpite enviado pelo cliente: ", mensagemEnvioClient)

    # Resposta do servidor
    data = sock.recv(1024) # Bytes

    print('\n*** Resultado final do jogo: \n', data.decode().upper())

    

