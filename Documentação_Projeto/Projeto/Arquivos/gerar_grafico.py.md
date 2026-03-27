------------------------------------------------------------------------
É a função responsável por gerar os gráficos das imagens.

**Utilização**
```python
GerarGrafico(imagemASerConvertida) #Chama a função
```

Ela completa:
```python
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from calc_percentual import calc_percentual

def gerarGrafico(entrada):
	saida = "imagem_convertida.png"
	img_pil = Image.open(entrada).convert("RGB")
	img_pil.save(saida)
	img = cv2.imread(saida)
	if img is None:
		print("Erro ao carregar")
		exit()

	# Reduz tamanho opcional
	altura = img.shape[0] // 2
	largura = img.shape[1] // 2
	img = cv2.resize(img, (largura, altura))
		
	# Máscara para ignorar preto
	mask = cv2.inRange(img, (0,0,0), (40,40,40))
	mask_inv = cv2.bitwise_not(mask)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		
	# --- Dividir imagem em duas regiões ---
	meio = img.shape[1] // 2
	regioes = {
		"Parte Esquerda": (slice(None), slice(0, meio)),
		"Parte Direita": (slice(None), slice(meio, img.shape[1]))
	}

	# --- Analisar cada região separadamente ---
	resultados = {}
	for nome, (ys, xs) in regioes.items():
		sub_gray = gray[ys, xs]
		sub_mask = mask_inv[ys, xs]
		resultados[nome] = calc_percentuais(sub_mask, sub_gray)

	# --- Plotar ---
	categorias = ["Escuras", "Médias", "Claras"]
	cores = ["#2c3e50", "#95a5a6", "#ecf0f1"]

	fig, axes = plt.subplots(1, 2, figsize=(10,4), sharey=True)
	for ax, (nome, valores) in zip(axes, resultados.items()):
		ax.bar(categorias, valores, color=cores)
		ax.set_title(nome)
		ax.set_ylim(0,100)
		for i, v in enumerate(valores):
			ax.text(i, v+1, f"{v:.1f}%", ha='center', fontweight='bold')
	plt.suptitle("Distribuição de Brilho por Região")
	plt.show()
```

## Destrinchando o Código
--------------------------------------------------------------------
**Importação**
```python
import cv2 #Esta importando a Biblioteca OpenCV2, para analizar a imagem
import numpy as np #Para calculos e manipulação de arrays
import matplotlib.pyplot as plt #Para geração de geáficos
from PIL import Image #Converter imagens
#Nesse caso só importei bibliotecas internas
```
#import -> Vai pegar arquivos de outras bibliotecas/arquivos e transportar para o arquivo do código.
#as -> Criar apelidos para as funções

----------------------------------------------------------------------
**Conversor de imagem**
```python
img_pil = Image.open(entrada).convert("RGB") #Abre a imagem e converte para RGB
img_pil.save(saida) #Salva como PNG
img = cv2.imread(saida) #Le a imagem convertida(em formato RGB)
```

#imread 
#open ->
#convert ->
#save ->

------------------------------------------------------------------------
**Verificação de imagem**
```python
if img is None:#Verifica se a variavel img está vazia
	print("Erro ao carregar") #Mostra uma mensagem que não está carregando a img
	exit() # Saí do programa
```

Verifica se a imagem está vazia,  se estiver o programa não vai funcionar

----------------------------------------------------------------------------------------------
**Reduz o tamanho da imagem**
```python
altura = img.shape[0] // 2 # Divide a altura em dois
largura = img.shape[1] // 2 # Divide a largura em dois
img = cv2.resize(img, (largura, altura)) # Efetua a redução de tamanho
```
#shape 
#resize ->

----------------
**Cria a mascara da imagem**
```python
mask = cv2.inRange(img, (0,0,0), (40,40,40)) #Cria a mascara, detectando pixeis pretos
mask_inv = cv2.bitwise_not(mask) #Pega a mascara de pixeis que não são pretos
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Re-colore a imagem com tons de cinza
```
#inRange 
#bitwise_not ->
#cvtColor ->
#COLOR_BGR2GRAY ->

-------------------------------------------------------
**Divide a imagem em 2 regiões**
```python
meio = img.shape[1] // 2 #Divide a imagem em dois(esquerda e direita)
regioes = { #cria um dicionario chamado regiões
	"Parte Esquerda": (slice(None), slice(0, meio)),#pega colunas da esquerda até o meio
	"Parte Direita": (slice(None), slice(meio, img.shape[1]))#pega as colunas da esquerda até o meio
}
```
#shape 
#slice ->

----------
**Armazena as porcentagens**
```python
resultados = {} #Cria um dicionariopara armazenar as porcentagens de cada metade
for nome, (ys, xs) in regioes.items(): #Vai para a  esquerda e direita
	sub_gray = gray[ys, xs] #Recorta a parte correspondente da imagem em tons de cinza.
	sub_mask = mask_inv[ys, xs]#recorta a máscara inversa correspondente.
	resultados[nome] = calc_percentuais(sub_mask, sub_gray) #Guarda os resultados da função calc_percentuais
```

-----------
**Gráfico**
```python
categorias = ["Escuras", "Médias", "Claras"] #Define uma lista com as categorias
cores = ["#2c3e50", "#95a5a6", "#ecf0f1"] # Define as cores das barras do gráfico
```

```python
fig, axes = plt.subplots(1, 2, figsize=(10,4), sharey=True)
for ax, (nome, valores) in zip(axes, resultados.items()):
	ax.bar(categorias, valores, color=cores)
	ax.set_title(nome)
	ax.set_ylim(0,100)
	for i, v in enumerate(valores):
		ax.text(i, v+1, f"{v:.1f}%", ha='center', fontweight='bold')
plt.suptitle("Distribuição de Brilho por Região")
plt.show()
```