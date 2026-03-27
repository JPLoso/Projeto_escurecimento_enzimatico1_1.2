Como funciona:
- Abre a imagem com **cv2.imread()** como **matrizNumpy**
- #matrizNumpy:
	- Cada pixel tem 3 valores: #BRG **(Blue, Green, Red)**
		- (0, 0 ,0) - > Preto
		- (255, 255, 255) -> Branco
		- (0, 0 , 255) -> Vermelho
	- Tamanho da imagem é: **Altura x Largura x 3**

Exemplo:

```python
imagem = cv2.imread("Foto.jpg")

altura = img.shape[0]
largura = img.shape[1]  

print(altura)
print(largura)
print(img.shape)
```
Saída:

```python
(1080, 1920, 3)   # 1080 pixels de altura, 1920 de largura, 3 canais (BGR)
```

#imread -> Lê a imagem e transforma em uma matrizNumpy
#shape -> Pega as medidas da imagem (Altura, Largura e Canais de Cores)
		->Quando está especificando entre chaves [], ele pega apenas um, 0 é a altura da imagem, 1 é a largura da imagem e 2 é as cores da imagem. Assim possibilitando armazenar dados mais específicos.
		
------------------------------------------------------------------------
#inRange -> Cria uma mascara da imagem, onde só tem 0 e 255.
- Como Funciona?
  - Pega pixel por pixel e compara o valor da cor do pixel escolhido com o valor inserido para comparar. Se estiver no alcance inserido, na mascara ficara 0, se não estiver, fica 255.
		
Exemplo:

```python

mask = cv2.inRange(img, (0,0,0), (40,40,40))

  

cv2.imshow("Mascara", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
#imshow -> Abre uma janela que mostra a imagem e a mascara.
#waitKey -> Espera que uma tecla seja pressionada para continuar o código
- Parâmetros -> Geralmente por tempo em milissegundos
	- 0 -> Tempo indefinido, espera uma tecla ser apertada para continuar
	- 1000 -> Ficaria 1 segundo
	- 1 -> 1 milissegundo
#destroyAllWindows ->Fecha todas as janelas do open CV