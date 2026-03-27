#Importando tk, messagebox, e duas funções internas
import tkinter as tk 
from tkinter import messagebox 
from iniciar_programa import iniciar_programa 
from selecionar_imagem import selecionar_imagem 

def main():
	#Define a janela, o titulo dela e o tamanho
	janela = tk.Tk() 
	janela.title("Analisador de Imagem") 
	janela.geometry("500x220") 
	
	#Define uma variavel que pode conter o caminho da imagem
	entrada_imagem = tk.StringVar() 
	
	#Define o que vai fazer quando clicar no botão para buscar a imagem
	def clicar_buscar(): 
		caminho = selecionar_imagem()
		if caminho:
			entrada_imagem.set(caminho) 
			botao_iniciar.config(state="normal") 
	
	#Define o que vai fazer quando clicar no botão de gerar gráfico.
	def clicar_iniciar():
		try:
			caminho = entrada_imagem.get()
			iniciar_programa(caminho)
			messagebox.showinfo("Sucesso", "Gráfico gerado com sucesso!") 
		except ValueError as e:
			messagebox.showwarning("Atenção", str(e)) 
		except Exception as e:
			messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
	
	#Define os campos para escolher a imagem, texto, campo de texto e botão
	tk.Label(janela, text="Selecione uma imagem para análise:").pack(pady=5)
	tk.Entry(janela, textvariable=entrada_imagem, width=50).pack(pady=5)
	tk.Button(janela, text="Buscar Imagem", command=clicar_buscar).pack(pady=5)
		
	#Define o botão de iniciar
	botao_iniciar = tk.Button(janela, text="Iniciar Programa", state="disabled", command=clicar_iniciar)
	botao_iniciar.pack(pady=10)
	
	#Mantem a janela aberta até o final do programa
	janela.mainloop()

  
#Garante que o código não ira rodar por outros arquivos
if __name__ == "__main__":
	main()
