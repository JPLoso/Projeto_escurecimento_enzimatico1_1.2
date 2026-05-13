#iniciar_programa.py
#Importa uma função interna e os(Permite mecher com arquivos do sistema)
from Aplicativo.App.gerar_grafico import gerar_grafico
import os

#Define a função que inicia o programa
def iniciar_programa(caminho_imagem):
	#Se o caminho estiver vazio, vai entrar nesse if
	if not caminho_imagem or caminho_imagem.strip() == "":
		raise ValueError("Nenhuma imagem selecionada")
	
	#Se o caminho não existe no sistema, vai entrar nesse if
	if not os.path.exists(caminho_imagem):
		raise FileNotFoundError("Arquivo não encontrado")
	
	#Chama a função para gerar o gráfico
	gerar_grafico(caminho_imagem)