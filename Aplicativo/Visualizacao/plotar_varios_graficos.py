import matplotlib.pyplot as plt
import math

def plotar_varios_graficos(resultados, limite=12):
    # pega apenas os primeiros N
    itens = list(resultados.items())[:limite]

    total = len(itens)

    # define grade (ex: 3x4, 4x4 etc)
    colunas = 4
    linhas = math.ceil(total / colunas)

    fig, axes = plt.subplots(linhas, colunas, figsize=(16, 4 * linhas))
    axes = axes.flatten()

    for i, (nome, valores) in enumerate(itens):
        categorias = ["Escuras", "Médias", "Claras"]

        axes[i].bar(categorias, [
            valores["escuras"],
            valores["medias"],
            valores["claras"]
        ])

        axes[i].set_title(nome[:15])  # corta nome se for grande
        axes[i].set_ylim(0, 100)

    # remove espaços vazios
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()