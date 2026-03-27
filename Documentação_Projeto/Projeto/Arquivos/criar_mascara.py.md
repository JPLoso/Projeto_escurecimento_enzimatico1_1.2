```python
#Importa o analisador de imagem(cv2) e o numpy
import cv2
import numpy as np

def criar_mascara(img):
	#Cria uma mascara, onde pixeis claros ficam com 255 e escuros 0
	mask_no_black = cv2.inRange(img, (40,40,40), (255,255,255))
	
	#Detecta contornos na mascara
	contornos, _ = cv2.findContours(mask_no_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	#Seleciona os 3 maiores objetos
	contornos = sorted(contornos, key=cv2.contourArea, reverse=True)[:3]
	
	#Cria uma imagme preta do mesmo tamanho que a original
	mask_final = np.zeros(img.shape[:2], dtype="uint8")
	
	#Caso o programa não encontre contornos, vai retornar uma mascara vazia
	if len(contornos) == 0:
		return mask_no_black
	
	#Preenche os contornos com -1 na mascara
	for cnt in contornos:
		cv2.drawContours(mask_final, [cnt], -1, 255, -1)
	
	#Retorna a mascara
	return mask_final
```