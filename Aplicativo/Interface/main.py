#main.py
import tkinter as tk
from tkinter import messagebox, filedialog

from Aplicativo.App.iniciar_programa import iniciar_programa
from Aplicativo.Processamento.analisar_pasta import analisar_pasta
from Aplicativo.Utils.salvar_json import salvar_json
from Aplicativo.Interface.selecionar_imagem import selecionar_imagem
from Aplicativo.Visualizacao.plotar_varios_graficos import plotar_varios_graficos

def main():
    janela = tk.Tk()
    janela.title("Analisador de Imagem")
    janela.geometry("500x250")

    entrada_imagem = tk.StringVar()

    def clicar_buscar():
        caminho = selecionar_imagem()
        if caminho:
            entrada_imagem.set(caminho)
            botao_iniciar.config(state="normal")

    def clicar_iniciar():
        try:
            iniciar_programa(entrada_imagem.get())
            messagebox.showinfo("Sucesso", "Gráfico gerado!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
            
    def clicar_pasta():
        try:
            pasta = filedialog.askdirectory()
            if not pasta:
                return
            resultados = analisar_pasta(pasta)
            if not resultados:
                messagebox.showwarning("Aviso", "Nenhuma imagem encontrada")
                return
            
            salvar_json(resultados)
            plotar_varios_graficos(resultados, limite=12)
            messagebox.showinfo("Sucesso", "Análise concluída!")

        except Exception as e:
            messagebox.showerror("Erro", str(e))


    def clicar_json():
        try:
            caminho = filedialog.askopenfilename(
                title="Selecionar arquivo JSON",
                filetypes=[("JSON", "*.json")]
            )

            if not caminho:
                return

            from Aplicativo.Utils.carregar_json import carregar_json
            dados = carregar_json(caminho)

            plotar_varios_graficos(dados)

            messagebox.showinfo("Sucesso", "Gráficos carregados do JSON!")

        except Exception as e:
            messagebox.showerror("Erro", str(e))
    

    tk.Label(janela, text="Selecione uma imagem:").pack(pady=5)
    tk.Entry(janela, textvariable=entrada_imagem, width=50).pack(pady=5)

    tk.Button(janela, text="Buscar Imagem", command=clicar_buscar).pack(pady=5)
    tk.Button(janela, text="Abrir JSON", command=clicar_json).pack(pady=5)

    botao_iniciar = tk.Button(janela, text="Gerar Gráfico", state="disabled", command=clicar_iniciar)
    botao_iniciar.pack(pady=5)

    tk.Button(janela, text="Analisar Pasta", command=clicar_pasta).pack(pady=5)

    janela.mainloop()