#Importa o NumPy, o analisador de imagem e o PIL para caminhos
import numpy as np
import cv2
from PIL import Image

def carregar_imagem(caminho):
    #Abre a imagem a partir do caminho e garante que esteja em RGB
    img_pil = Image.open(caminho).convert("RGB")

    #Converte cada pixel em um valor númerico e salva em uma lista numPy
    #o cv2 trabalha com BGR e não RGB, então nós convertemos
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)