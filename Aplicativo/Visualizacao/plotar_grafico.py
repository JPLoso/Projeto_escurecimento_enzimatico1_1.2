#Importa a biblioteca dos gráficos
from matplotlib.pyplot import plot as plt

#Define a função
def plotar_grafico(valores):
    #Define as 3 categorais do gráfico
    categorias = ["Escuras", "Médias", "Claras"]

    #Cria um gráfico de tamango 6x4 com o eixo X sendo categorias e o Y valores
    plt.figure(figsize=(6,4))
    plt.bar(categorias, valores)

    #Mostra a porcentagem em cima da barra
    for i, v in enumerate(valores):
        plt.text(i, v+1, f"{v:.1f}%", ha='center')

    #Define o limite de 0 a 100 do gráfico, o titulo eo rotulo do eixo Y
    plt.ylim(0,100)
    plt.title("Distribuição de claridade")
    plt.ylabel("% dos Pixels")

    #Abre a janela do gráfico
    plt.show()