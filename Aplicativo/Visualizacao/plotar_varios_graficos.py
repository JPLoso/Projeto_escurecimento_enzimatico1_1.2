import matplotlib.pyplot as plt
import numpy as np

def plotar_varios_graficos(resultados, limite=12):

    # Limita quantidade
    itens = list(resultados.items())[:limite]

    # Nomes dos arquivos/processamentos
    tempos = [nome for nome, _ in itens]

    # Valores
    escuros = [valores["escuras"] for _, valores in itens]
    claros = [valores["claras"] for _, valores in itens]

    # Posições do eixo X
    x = np.arange(len(tempos))

    # Largura das barras
    largura = 0.35

    # Cria figura
    plt.figure(figsize=(14, 6))

    # Barras
    barras_escuros = plt.bar(
        x - largura / 2,
        escuros,
        largura,
        label="Escuros",
        color="#2C2C2C"
    )

    barras_claros = plt.bar(
        x + largura / 2,
        claros,
        largura,
        label="Claros",
        color="#F4C542"
    )

    # Valores acima das barras
    for barras in [barras_escuros, barras_claros]:

        for barra in barras:

            altura = barra.get_height()

            plt.text(
                barra.get_x() + barra.get_width() / 2,
                altura + 1,
                f"{altura:.1f}%",
                ha='center',
                va='bottom',
                fontsize=8
            )

    # Configurações
    plt.xticks(x, tempos, rotation=45)

    plt.xlabel("Imagens / Processamentos")

    plt.ylabel("% dos Pixels")

    plt.title("Distribuição de Claridade")

    plt.ylim(0, 100)

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.legend(
        loc='center left',
        bbox_to_anchor=(1.02, 0.5)
    )

    plt.tight_layout()

    plt.show()