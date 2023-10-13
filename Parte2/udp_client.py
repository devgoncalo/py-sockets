# Importação do Módulo de Socket:
import socket

# Criação de um Socket UDP denominado de "udp_client":
# Protocolo "AF_INET": Internet Versão 4;
# Protocolo "SOCK_DGRAM": UDP.

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     
msgFromClient       = "Thanks for connecting me!"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Envio da Mensagem para o Servidor Usando o Socket UDP:

#UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# Recebimento da Mengsaem do Servidor:

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])
print(msg)

# Enviado Mais do que Apenas Strings:

from time import time
from platform import node, python_version_tuple

current_time = time()
network_name = node()
python_version = python_version_tuple()

# Estrutura da Mensagem (current time, network name, major, minor, revision)

# Transformar a Variável Current Time (Float) em String:
current_time = str(current_time)
message = current_time

# Adicionar Caracter para Separar as Variaveis (,):
message = message + ","

# Adicionar o Nome da Rede há mensagem:
message = message + network_name + ","

# Adiconar a Versão de Python há mensagem (Tupla de 3 Valores):
message = message + python_version[0] + "," + python_version[1] + "," + python_version[2]

# Codificação da Mensagem em Bytes:
data = message.encode()

# Envio da Mensagem:
UDPClientSocket.sendto(data, serverAddressPort)

# Serialização:

# Importação do Pacote Pickle:
import pickle

message = (current_time, network_name, python_version)
data = pickle.dumps(message)

# Envio da Mensagem Serializada com a Biblioteca Pickles:
UDPClientSocket.sendto(data, serverAddressPort)