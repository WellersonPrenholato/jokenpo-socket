import socket
import random

HOST = 'localhost'
PORT = 5000
addr = (HOST, PORT)

# Lista com as possíveis jogadas que podem ser escolhidas pelo servidor.
opcoesJogadas = ['Pedra', 'Papel', 'Tesoura']

# O mecanismo de Socket foi criado para receber a conexão, onde na função passamos 2 argumentos, AF_INET que declara a família do protocolo; 
# Se fosse um envio via Bluetooth por exemplo, seria: AF_BLUETOOTH, e o SOCKET_STREAM, indica que será TCP/IP.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM identificação do TCP

# Esta linha define para qual IP e porta o servidor deve aguardar a conexão.
sock.bind(addr)

# Define o limite de conexões. E no caso, estamos limitando em 5 conexões.
sock.listen(5)

print("Aguardando conexão de um cliente:")

conn, ender = sock.accept() # Conexão e endereço

print('Connectado com', ender) # Apresentação do endereço do cliente, composto de nome do host e a porta que foram conectados.
print("\nOs palpites do servidor são ALEATÓRIOS!\n")

while True:
    # Aguarda um dado enviado pela rede de até 1024 Bytes, a função ‘recv’ possui somente 1 argumento que é o tamanho do Buffer.
    data = conn.recv(1024) # 1024 Byter serão recebidos do client

    # print("Resposta do cliente:", data.decode())

    if not data: # Quanto não tiver mais nada lá dentro
        print("\nConexão encerrada!\n")

        conn.close() # Serve para fechar a conexão entre as aplicações.
        break
    
    palpiteClient = str(data.decode()) # Utilizado para decodificar e transformar a mensagem em string enviada pelo cliente.
    palpiteServ = random.choice(opcoesJogadas) # O palpite do servidor é escolhido de forma randômica, as opções estão dentro da lista opcoesJogadas.

    print("* O Servidor respondeu:", palpiteServ) # Apresenta o palpite do servidor

    # Verifica quando o cliente ganha a jogada
    if ((palpiteClient == 'Tesoura' and palpiteServ == 'Papel') or (palpiteClient == 'Pedra' and palpiteServ == 'Tesoura') or (palpiteClient == 'Papel' and palpiteServ == 'Pedra')):
        ganhador = 'Cliente'
    
    # Verifica quando o Servidor ganha a jogada
    if ((palpiteClient == 'Papel' and palpiteServ == 'Tesoura') or (palpiteClient == 'Tesoura' and palpiteServ == 'Pedra') or (palpiteClient == 'Pedra' and palpiteServ == 'Papel')):
        ganhador = 'Servidor'
    
    # Verificação em caso de empate
    if (palpiteClient == palpiteServ):
        ganhador = 'Empate'

    # String de retorno para o cliente
    result = '- Cliente: '+ str(palpiteClient) + '\n - Servidor: ' + str(palpiteServ) + '\n=> GANHADOR: ' + str(ganhador) + '\n'

    # Utilizado para enviar o resultodo para o cliente.
    conn.sendall(bytes(str(result), 'utf8'))
