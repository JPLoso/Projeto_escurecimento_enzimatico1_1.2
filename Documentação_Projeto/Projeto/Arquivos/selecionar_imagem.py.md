```python
#Importando filedialog e os
from tkinter import filedialog
import os

def selecionar_imagem():
	#Define o caminho
	caminho = filedialog.askopenfilename(
		title="Selecione uma imagem",
		#Define quais tipos de arquivo podem ser usados
		filetypes=[
			("Imagens", "*.png *.jpg *.jpeg *.bmp"),
			("Todos os arquivos", "*.*")
		]
	)
	
	#Se o caminho for vazio, ele vai retornar vazio
	if not caminho:
		return None
	
	#Se o caminho for inválido, vai retornar vazio
	if not os.path.exists(caminho):
		return None
	
	#Se estiver tudo correto, vai retornar o caminho
	return caminho
```

