import tkinter as tk
from tkinter import messagebox

from Aplicativo.Processamento.formulas_lab import (
    calcular_ie,
    calc_perc_ie
)
from Aplicativo.Visualizacao.plotar_varios_graficos import plotar_varios_graficos
from Aplicativo.Processamento.analisar_pasta import (
    analisar_pasta,
    ordenacao_natural
)  


def abrir_janela_lab(janela_pai, pasta, arquivos):
    arquivos = sorted(arquivos, key=ordenacao_natural)
    janela = tk.Toplevel(janela_pai)
    janela.title("Valores LAB")

    entradas = []

    # Cabeçalho
    tk.Label(janela, text="Imagem").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(janela, text="L").grid(row=0, column=1, padx=5, pady=5)
    tk.Label(janela, text="a").grid(row=0, column=2, padx=5, pady=5)
    tk.Label(janela, text="b").grid(row=0, column=3, padx=5, pady=5)

    # Cria uma linha para cada imagem
    for i, arquivo in enumerate(arquivos):

        tk.Label(
            janela,
            text=arquivo
        ).grid(row=i + 1, column=0, padx=5, pady=2)

        entrada_L = tk.Entry(janela, width=8)
        entrada_L.grid(row=i + 1, column=1)

        entrada_a = tk.Entry(janela, width=8)
        entrada_a.grid(row=i + 1, column=2)

        entrada_b = tk.Entry(janela, width=8)
        entrada_b.grid(row=i + 1, column=3)

        entradas.append((arquivo, entrada_L, entrada_a, entrada_b))

    def confirmar():

        try:

            ies = {}

            # Calcula o IE de cada imagem
            for arquivo, entrada_L, entrada_a, entrada_b in entradas:

                L = float(entrada_L.get())
                a = float(entrada_a.get())
                b = float(entrada_b.get())

                ies[arquivo] = calcular_ie(L, a, b)

            # Primeira imagem é a referência
            ie_inicial = ies[arquivos[0]]

            # -------------------------------
            # Janela de resultados
            # -------------------------------
            janela_resultados = tk.Toplevel(janela)
            janela_resultados.title("Resultados do IE")

            tk.Label(
                janela_resultados,
                text="Imagem",
                font=("Arial", 10, "bold")
            ).grid(row=0, column=0, padx=10, pady=5)

            tk.Label(
                janela_resultados,
                text="IE",
                font=("Arial", 10, "bold")
            ).grid(row=0, column=1, padx=10, pady=5)

            tk.Label(
                janela_resultados,
                text="% Escurecimento",
                font=("Arial", 10, "bold")
            ).grid(row=0, column=2, padx=10, pady=5)

            for i, arquivo in enumerate(arquivos):

                porcentagem = calc_perc_ie(
                    ie_inicial,
                    ies[arquivo]
                )

                tk.Label(
                    janela_resultados,
                    text=arquivo
                ).grid(row=i + 1, column=0)

                tk.Label(
                    janela_resultados,
                    text=f"{ies[arquivo]:.2f}"
                ).grid(row=i + 1, column=1)

                tk.Label(
                    janela_resultados,
                    text=f"{porcentagem:.2f}%"
                ).grid(row=i + 1, column=2)

            def continuar():

                resultados = analisar_pasta(pasta)

                plotar_varios_graficos(resultados)

                janela_resultados.destroy()
                janela.destroy()

            tk.Button(
                janela_resultados,
                text="Continuar",
                command=continuar
            ).grid(
                row=len(arquivos) + 1,
                column=0,
                columnspan=3,
                pady=10
            )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Preencha todos os valores de L, a e b."
            )

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    tk.Button(
        janela,
        text="Confirmar",
        command=confirmar
    ).grid(
        row=len(arquivos) + 1,
        column=0,
        columnspan=4,
        pady=10
    )