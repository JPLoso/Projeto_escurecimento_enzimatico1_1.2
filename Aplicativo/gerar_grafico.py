#Importações de funções internas
from plotar_grafico import plotar_grafico
from analisar_imagem import analisar_imagem
from criar_mascara import criar_mascara
from carregar_imagem import carregar_imagem

#Define a função para gerar grafico
def gerar_grafico(caminho):
    #Guarda a imagem em formato BGR
    img = carregar_imagem(caminho)

    #Remove o fundo e seleciona os principais objetos
    mask = criar_mascara(img)

    #Converte para escala de cinza
    valores = analisar_imagem(img, mask)
    
    #Gera o gráfico
    plotar_grafico(valores)

    #Devolve os percentuais
    return valores