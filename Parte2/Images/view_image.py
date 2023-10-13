# Resconstruindo a Imagem:

# Importação do Módulo "fl_networking_tools"
from fl_networking_tools import ImageViewer

# Criação de um Objeto ImageViewer e Inicia-lo em Execução:
viewer = ImageViewer()
viewer.start()

# Importação do Módulo de "Socket" e "Pickle":
import socket
import pickle

# Criaçõo de um Socket UDP denominado de "udp_server":
# Protocolo "AF_INET": Internet Versão 4;
# Protocolo "SOCK_DGRAM": UDP.

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

# Configuração do Socket para usar um Endereço e uma Porta:

udp_server.bind((localIP, localPort))

# Defenir uma função "get_pixel_data" que irá esperar os Dados Recebidos do Socket UDP:
def get_pixel_data():
    while True:
        data, client_address = udp_server.recvfrom(bufferSize)

        # Extrair a Mensagem e Dividi-la nas Partes das Suas Componentes:
        message = pickle.loads(data)
        pos = message[0]
        rgba = message[1]

        # Usar o método "put_pixel" para Passar a Posição e os Valores dos Pixeis:
        viewer.put_pixel(pos, rgba)

        # Variáveis que Gaurdam o Número Perdidos de Pixeis e o último Pixel Atualizado:
        lost_pixels = 0
        last_pixel_updated = (-1, 1)

        # Exibir quantos Pixeis foram Perdidos no ImageViewer
        viewer.text = lost_pixels

        # Verificar se o Pixel Recebido está fora de Sequência:
        last_pixel_updated

        # Comparar a Posição do Pixel recebido com a Posição do último Recebido e Atualizar a Variável "last_updated_pixel":
        if(pos[0]-last_pixel_updated[0]>1) or (pos[1]-last_pixel_updated[1]>1):
            lost_pixels += 1
            viewer.text = lost_pixels
            last_pixel_updated = pos

# Preparar o Código para Iniciar o Visualizador de Imagens:
viewer.start(get_pixel_data)