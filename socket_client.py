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
# data = client_socket.recv(1024)

# Descodificação da Mensagem em Bytes e Escrita da Mesma:
# mensagem = data.decode()
# print(mensagem)

# Subsituição da Receção da Mensagem Aceitando a Nova Função "send_text":
def get_text(receiving_socket):
    buffer = ""
    socket_open = True
    while socket_open:
        # Leitura dos Dados do Socket:
        data = receiving_socket.recv(1024)

        # Sem Dados o Socket deve Fechar:
        if not data:
            socket_open = False
        # Adicionar Dados ao Buffer:
        buffer = buffer + data.decode()

        # Verificar se existe a terminação (\n) no Buffer:
        terminator_pos = buffer.find("\n")

        # Se o valor do Terminador for "-1", o Caracter deve Existir:
        while terminator_pos > -1:
            # Retirar Todo o Contéudo do Buffer:
            mensagem = buffer[:terminator_pos]

            # Retirar apenas a Mensagem do Buffer:
            buffer = buffer[terminator_pos + 1:]

            # Returnar a Mensagem com "yield":
            yield mensagem

            # Verificar se Existe outro Terminador (\n) no Buffer:
            terminator_pos = buffer.find("\n")

# 1 - Obter a Mensagem com um Ciclo For até a Função do Gerador "get text" seja Concluida e o Socket for Fechado:
#for mensagem in get_text(client_socket):
#    print(mensagem)

# 2 - Usar "next" para Chamar a Função "get_text" uma vez e Pbter uma Única Mensagem
mensagem = next(get_text(client_socket))
print(mensagem)

# Mensagem a ser Enviada para o Servidor:
mensagem = "Thank you for connecting me!"

# Codificação da Mensagem para uma série de Bytes:
data = mensagem.encode()

# Envio da Mensagem já Codificada para o Cliente:
client_socket.send(data)

# Fechamento e Desconecção do Socket:
client_socket.close()