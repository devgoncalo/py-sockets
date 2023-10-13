# Importação do Módulo de Socket:
import socket

# Criaçõo de um Socket UDP denominado de "udp_server":
# Protocolo "AF_INET": Internet Versão 4;
# Protocolo "SOCK_DGRAM": UDP.

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

# Configuração do Socket para usar um Endereço e uma Porta:

udp_server.bind((localIP, localPort))

while True:
    data, client_address = udp_server.recvfrom(bufferSize)
    print(data)
    