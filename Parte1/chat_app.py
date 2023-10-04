# Importação do Módulo de Socket:

import socket

choice = input("1 - Start a Server, 2 - Connect With a Client: ")

if choice == "1":
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
    print("Connection Detected At..." + str(address))
else:
    address = input("What is the Server IP address?")
    connection =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((address, 8081))
    name = input("What is Your Name?")
    connection.send(bytes(name + " is Connected to the Server!", "utf-8"))

while True:
    message = connection.recv(1024)
    print(message.decode())
    new_message = input("Type a Message: ")
    connection.send(new_message.encode())