import socket
import random

HOST = 'localhost'
PORT = 5000
addr = (HOST, PORT)

opcoesJogadas = ['Pedra', 'Papel', 'Tesoura']

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM identificação do TCP

sock.bind(addr)
sock.listen()

print("Aguardando conexão de um cliente:")

conn, ender = sock.accept() # Conexão e endereço

# print(f"Conectado em {ender}")

print('Connectado com', ender)
while True:
    data = conn.recv(1024) # 1024 Byter serão recebidos do client
    # print("Resposta do cliente:", data.decode())

    if not data: # Quanto não tiver mais nada lá dentro
        print("\nConexão encerrada!\n")
        conn.close()
        break
    
    palpiteClient = str(data.decode())
    palpiteServ = random.choice(opcoesJogadas)

    print("* O Servidor respondeu:", palpiteServ)

    # palpiteClient = str(palpiteClient.lower())

    if ((palpiteClient == 'Tesoura' and palpiteServ == 'Papel') or (palpiteClient == 'Pedra' and palpiteServ == 'Tesoura') or (palpiteClient == 'Papel' and palpiteServ == 'Pedra')):
        ganhador = 'Cliente'
    
    if ((palpiteClient == 'Papel' and palpiteServ == 'Tesoura') or (palpiteClient == 'Tesoura' and palpiteServ == 'Pedra') or (palpiteClient == 'Pedra' and palpiteServ == 'Papel')):
        ganhador = 'Servidor'
    
    if (palpiteClient == palpiteServ):
        ganhador = 'Empate'

    result = '- Cliente: '+ str(palpiteClient) + '\n - Servidor: ' + str(palpiteServ) + '\n=> GANHADOR: ' + str(ganhador) + '\n'

    conn.sendall(bytes(str(result), 'utf8'))
