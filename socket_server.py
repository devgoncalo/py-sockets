# Importação do Módulo de Socket:
import socket

# Criaçõo de um Socket TCP/IP denominado de "server_socket":
# Protocolo "AF_INET": Internet Versão 4;
# Protocolo "SOCK_STREAM": TCP.

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuração do Socket para usar um Endereço e uma Porta:
server_socket.bind(("0.0.0.0", 8081))

# Colocação do Socket há escuta para conexão:
server_socket.listen()
print("Waiting Connection...")

# Espera pela conexão e aceitação:
conection_socket, address = server_socket.accept()
print("Client Connected.")


