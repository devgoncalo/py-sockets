# Importação do Módulo de Socket:
import socket

# Criaçõo de um Socket TCP/IP denominado de "client_socket":
# Protocolo "AF_INET": Internet Versão 4;
# Protocolo "SOCK_STREAM": TCP.

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuração do Socket Cliente com o Socket Servidor:
client_socket.connect(("127.0.0.1", 8081))
print("Connected.")

# Receçao dos Dados até 1024 Bytes de uma vez:
data = client_socket.recv(1024)

# Descodificação da Mensagem em Bytes e Escrita da Mesma:
mensagem = data.decode()
print(mensagem)