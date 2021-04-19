# JOKENPO UTILIZANDO SOCKET E A LINGUAGEM DE PROGRAMAÇÃ PYTHON
# AUTOR: WELLERSON PRENHOLATO DE JEUS

# Bibliotecas
import socket
import random

# Identificação do HOST E PORT do client
HOST = '127.0.0.1' # Identifica o nome do client
PORT = 5000 # Identifica a porta do client para comunicar com o servidor

# Lista com as possíveis jogadas que podem ser escolhidas pelo cliente.
opcoesJogadas = ['Pedra', 'Papel', 'Tesoura']

# O mecanismo de Socket foi criado para receber a conexão, onde na função passamos 2 argumentos, AF_INET que declara a família do protocolo; 
# Se fosse um envio via Bluetooth por exemplo, seria: AF_BLUETOOTH, e o SOCKET_STREAM, indica que será TCP/IP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# A constante AF_INET faz parte de um grupo denominado famílias de endereços, ou address families, que constitui exatamente o primeiro parâmetro opcional do construtor socket. 
# A AF_INET abrange os endereços do tipo IPv4, antigo padrão da Internet.

# Realiza a conexão com o servidor
sock.connect((HOST, PORT)) # Parênteses duplo pq o connect tem apenas um parâmetro.

while True: # O cliente pode realizar n comunicações com o servidor, ou até essa ligação ser encerrada.
    # O usuário escolhe o tipo de jogada que será feita, sendo 1 - Palpite aleatório e 2 o usuário informa um palpite, por fim caso ele informe 0(zero) a conexão é encerrada.
    opcao1 = int(input("\n* Escolha uma opção:\n 1- Palpite aleatório\n 2- Informar um palpite\n 0- Para encerrar.\n -> Opcao: "))

    # Caso o usuário escolha a opcao 1, então o palpite será aleatório. Essa aleatoriedade é dada de acordo com a lista opcoesJogadas.
    if (opcao1 == 1):
        mensagemEnvioClient = random.choice(opcoesJogadas) # Randomização da jogada de acordo com a lista opcoesJogadas.

    # Caso o usuário escolha a opcao 2, então um menu é aberto para escolhar o palpite.
    if (opcao1 == 2):
        opcao2 = int(input("\n* Ecolha o palpite:\n 1- Pedra\n 2- Papel\n 3- Tesoura\n -> Opcao: "))

        if (opcao2 == 1):
            mensagemEnvioClient = 'Pedra' # Caso o usuário escolha a opção 1, então a jogada será Pedra.
        elif (opcao2 == 2):
            mensagemEnvioClient = 'Papel' # Caso o usuário escolha a opção 1, então a jogada será Papel.
        elif (opcao2 == 3):
            mensagemEnvioClient = 'Tesoura' # Caso o usuário escolha a opção 1, então a jogada será Tesoura.
    
    # Caso o usuário informe 0(zero) no momento de escolher a jogada, então a conexão é encerrada. 
    if (opcao1 == 0):
        print("\nConexão encerrada!\n")
        # Utilizado para fechar a conexão entre as duas aplicações.
        sock.close()
        break
    
    # Utilizado para fazer o envio de dados para o servidor.
    sock.sendall(str.encode(mensagemEnvioClient)) # Enviar mensagem para o servidor
    
    print("\n-> Palpite enviado pelo cliente: ", mensagemEnvioClient) # Apresenta o palpite escolhido pelo cliente

    # Aguarda o retorno do servidor, um dado enviado pela rede de até 1024 Bytes, a função ‘recv’ possui somente 1 argumento que é o tamanho do Buffer.
    data = sock.recv(1024) # Bytes

    # Decodifica a mensagem recebida pelo servidor, coloca todas as letras em maiúsculo e por último essa mensagem é apresentada.
    print('\n*** Resultado final do jogo: \n', data.decode().upper())
