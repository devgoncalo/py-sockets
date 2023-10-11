# Criação de um Servidor TCP:

# Importação do Módulo de Socket:
# import socket

# Criaçõo de um Socket TCP/IP denominado de "tcp_server":
# Protocolo "AF_INET": Internet Versão 4;
# Protocolo "SOCK_STREAM": TCP.

# tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuração do Socket para usar um Endereço e uma Porta:
# tcp_server.bind(("0.0.0.0", 8081))

# Colocação do Socket há escuta para conexão:
# tcp_server.listen()

# Espera pela conexão e aceitação:
# conection_socket, address = tcp_server.accept()

# data = conection_socket.recv(1024)
# conection_socket.send(data)

# Criação de um Servidor UDP:

# Importação do Módulo de Socket:
import socket

# Criaçõo de um Socket UDP denominado de "udp_server":
# Protocolo "AF_INET": Internet Versão 4;
# Protocolo "SOCK_DGRAM": UDP.

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer = "Hello, you are Connected!"
bytesToSend = str.encode(msgFromServer)

# Configuração do Socket para usar um Endereço e uma Porta:

UDPServerSocket.bind((localIP, localPort))
print("The UDP Sever is Up and Listening!")

while(True):

    #bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    #message = bytesAddressPair[0]
    #address = bytesAddressPair[1]

    #clientMsg = "Message from Client:{}".format(message)
    #clientIP  = "Client IP Address:{}".format(address)
    
    #print()
    #print(clientMsg)
    #print(clientIP)
    
    # Sending a reply to client:

    #UDPServerSocket.sendto(bytesToSend, address)

    # Receber Mais do que Strings:

    #data = UDPServerSocket.recvfrom(bufferSize)

    #messagem = data.decode()
    #parts = messagem.split(",")
    #current_time = float(parts[0])
    #network_name = parts[1]
    #python_version = (parts[2], parts[3], parts[4])

    # Serialização:

    data = UDPServerSocket.recvfrom(bufferSize)

    print(data.decode())

    # Importação do Pacote Pickle:
    import pickle

    #Descontrução em Série e Tranformação num Vetor:
    message = pickle.loads(data)

    current_time = message[0]
    network_name = message[1]
    python_version = message[2]

