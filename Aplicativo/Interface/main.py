import tkinter as tk
from tkinter import messagebox, filedialog

from Aplicativo.Processamento.analisar_pasta import analisar_pasta
from Aplicativo.Visualizacao.plotar_varios_graficos import plotar_varios_graficos

def main():
    janela = tk.Tk()
    janela.title("Analisador de Imagem")
    janela.geometry("500x250")

    def clicar_pasta():
        try:
            pasta = filedialog.askdirectory()
            if not pasta:
                return

            resultados = analisar_pasta(pasta)
            if not resultados:
                messagebox.showwarning(
                    "Aviso",
                    "Nenhuma imagem encontrada"
                )
                return

            plotar_varios_graficos(resultados)

        except Exception as e:
            messagebox.showerror(
                "Erro",
                str(e)
            )

    tk.Label(
        janela,
        text="Selecione uma pasta para análise"
    ).pack(pady=20)

    tk.Button(
        janela,
        text="Analisar Pasta",
        command=clicar_pasta
    ).pack(pady=10)

    janela.mainloop()

if __name__ == "__main__":
    main()