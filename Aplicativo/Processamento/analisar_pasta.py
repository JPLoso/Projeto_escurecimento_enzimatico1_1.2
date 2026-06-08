import os
import re
from Aplicativo.Processamento.carregar_imagem import carregar_imagem
from Aplicativo.Processamento.criar_mascara import criar_mascara
from Aplicativo.Processamento.analisar_imagem import analisar_imagem

def ordenacao_natural(nome):
    return [
        int(texto) if texto.isdigit() else texto.lower()
        for texto in re.split(r'(\d+)', nome)
    ]

def analisar_pasta(caminho_pasta):
    resultados = {}
    if not os.path.exists(caminho_pasta):
        raise FileNotFoundError(f"Pasta não encontrada: {caminho_pasta}")

    arquivos = sorted(
        os.listdir(caminho_pasta),
        key=ordenacao_natural
    )

    for arquivo in arquivos:
        caminho_completo = os.path.join(caminho_pasta, arquivo)
        if arquivo.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
            try:
                img = carregar_imagem(caminho_completo)
                mask = criar_mascara(img)
                valores = analisar_imagem(img, mask)

                resultados[arquivo] = {
                    "escuras": valores[0],
                    "claras": valores[1]
                }
            
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")

    return resultados