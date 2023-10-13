# Instalando fl_networking_tools

#import fl_networking_tools
#print("fl_networking_tools importado")

# Enviando Cada Pixel:

# Utilizar o Python Image Library PIL para abrir uma imagem e obter dimensões largura e altura:
from PIL import Image
image = Image.open("/home/asap/Pictures/walpaper")

width, height = image.size
print(width, height)

# Enviando os Pixeis:

import pickle
import socket

# Criação de um Socket UDP denominado de "udp_client":
# Protocolo "AF_INET": Internet Versão 4;
# Protocolo "SOCK_DGRAM": UDP.

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

localIP     = "127.0.0.1"
localPort   = 20001

# Contruir uma Meesagem para cada Pixel, contendo a Poisção e RGBA:
# Obter os Dados de Cor de Pixel usando o Método image.getpixel:

for y in range (height):
    for x in range (width):
        pos = (x, y)
        rgba = image.getpixel(pos)
        print(pos, rgba)

# Usando o módulo Pickle Vamos Converter a Mensagem em Bytes:

message = (pos, rgba)
data = pickle.dumps(message)

# Enviar os Dados de Pixel usando o Socket "udp_client":

udp_client.sendto(data, (localIP, localPort))