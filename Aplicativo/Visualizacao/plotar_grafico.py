import matplotlib.pyplot as plt

def plotar_grafico(valores):

    categorias = ["Escuras", "Claras"]

    plt.figure(figsize=(6, 4))

    barras = plt.bar(categorias, valores)

    # Valores acima das barras
    for barra in barras:

        altura = barra.get_height()

        plt.text(
            barra.get_x() + barra.get_width() / 2,
            altura + 1,
            f"{altura:.1f}%",
            ha='center'
        )

    plt.ylim(0, 100)

    plt.title("Distribuição de Claridade")

    plt.ylabel("% dos Pixels")

    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()

    plt.show()