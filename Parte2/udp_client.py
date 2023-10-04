# Importação do Módulo de Socket:
import socket

# Criaçõo de um Socket UDP denominado de "udp_client":
# Protocolo "AF_INET": Internet Versão 4;
# Protocolo "SOCK_DGRAM": UDP.

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     
msgFromClient       = "Thanks for connecting me!"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Envio da Mensagem para o Servidor Usando o Socket UDP:

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# Recebimento da Mengsaem do Servidor:

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
