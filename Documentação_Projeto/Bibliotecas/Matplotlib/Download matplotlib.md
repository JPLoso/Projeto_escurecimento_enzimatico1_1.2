Fonte - https://matplotlib.org/stable/users/getting_started/

(Windows)
```terminal
pip install matplotlib 
```
(Ubuntu)
```terminal
sudo apt install python3-matplotlib
```

Exemplo para teste: Se rodar sem erros é por que foi instalado com sucesso 

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
```
