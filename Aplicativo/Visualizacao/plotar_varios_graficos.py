import matplotlib.pyplot as plt
import numpy as np
from Aplicativo.Processamento.calcular_variacao import calcular_variacao
from Aplicativo.Processamento.formulas_lab import calcular_variacao_ie

def plotar_varios_graficos(
    resultados,
    limite=12,
    texto_lab=""
):

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
    plt.figure(figsize=(14, 8))

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

    variacoes = calcular_variacao(resultados)

    variacoes_ie = calcular_variacao_ie(resultados)

    texto_ie = "Índice de Escurecimento\n\n"

    for v in variacoes_ie:

        texto_ie += (
            f"{v['imagem']}\n"
            f"IE: {v['ie']:.2f}\n"
            f"{v['variacao']:+.1f}%\n\n"
        )
    
    plt.figtext(
        0.58,
        0.02,
        texto_ie,
        fontsize=9,
        bbox=dict(facecolor="white",alpha=0.8)
    )

    texto_variacao = "Variação (%)\n\n"

    for v in variacoes:
        texto_variacao += (
            f"{v['comparacao']}\n"
            f"Escuros: {v['escuros']:+.1f}%\n"
            f"Claros : {v['claros']:+.1f}%\n\n"
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

    plt.grid(
        axis='y',
        linestyle='--',
        alpha=0.7
    )

    plt.legend(
        loc='center left',
        bbox_to_anchor=(1.02, 0.5)
    )

    # Exibe resultados LAB na mesma janela
    if texto_lab:
        plt.figtext(
            0.02,
            0.01,
            texto_lab,
            fontsize=10,
            bbox=dict(
                facecolor="white",
                alpha=0.8
            )
        )

    plt.figtext(
        0.78,
        0.02,
        texto_variacao,
        fontsize=9,
        bbox=dict(
            facecolor="white",
            alpha=0.8
        )
    )

    plt.tight_layout(
        rect=[0, 0.18, 1, 1]
    )

    plt.show()