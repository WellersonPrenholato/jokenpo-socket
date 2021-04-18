# Bibliotecas
import socket
import random

HOST = '127.0.0.1'
PORT = 5000

# Lista com as possíveis jogadas que podem ser escolhidas pelo cliente.
opcoesJogadas = ['Pedra', 'Papel', 'Tesoura']

# O mecanismo de Socket foi criado para receber a conexão, onde na função passamos 2 argumentos, AF_INET que declara a família do protocolo; 
# Se fosse um envio via Bluetooth por exemplo, seria: AF_BLUETOOTH, e o SOCKET_STREAM, indica que será TCP/IP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Realiza a conexão com o servidor
sock.connect((HOST, PORT)) # Parênteses duplo pq o connect tem apenas um parâmetro.

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
        # Serve para fechar a conexão entre as duas aplicações.
        sock.close()
        break
    
    # Utilizado para fazer o envio de dados para o servidor.
    sock.sendall(str.encode(mensagemEnvioClient)) # Enviar mensagem para o servidor
    
    print("\n-> Palpite enviado pelo cliente: ", mensagemEnvioClient) # Apresenta o palpite escolhido pelo cliente

    # Aguarda o retorno do servidor, um dado enviado pela rede de até 1024 Bytes, a função ‘recv’ possui somente 1 argumento que é o tamanho do Buffer.
    data = sock.recv(1024) # Bytes

    # Decodifica a mensagem recebida pelo servidor, coloca todas as letras em maiúsculo e por último essa mensagem é apresentada.
    print('\n*** Resultado final do jogo: \n', data.decode().upper())

    

