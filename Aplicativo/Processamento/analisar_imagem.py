import cv2
import numpy as np
from Aplicativo.Processamento.calc_percentual import calc_percentuais
from Aplicativo.Processamento.formulas_lab import calcular_ie

def analisar_imagem(img, mask):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    escuros, claros = calc_percentuais(mask, gray)

    # 1. Converte de BGR para LAB mantendo em uint8 (padrão estável do OpenCV)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # 2. Filtra apenas os pixels de dentro da máscara
    pixels = lab[mask > 0]

    if len(pixels) == 0:
        return {
            "escuras": 0, "claras": 0,
            "L": 0, "a": 0, "b": 0, "ie": 0
        }

    # 3. SEPARAÇÃO DOS CANAIS ANTES DE CALCULAR A MÉDIA
    # Convertemos os canais extraídos para float comum do Python.
    # Isso impede o "underflow" (subtrair 128 de um uint8 menor que 128).
    canal_L = pixels[:, 0].astype(float)
    canal_a = pixels[:, 1].astype(float)
    canal_b = pixels[:, 2].astype(float)

    # 4. APLICA A CORREÇÃO DE ESCALA DO OPENCV PARA UINT8
    # OpenCV mapeia: L -> L * 255 / 100 | a -> a + 128 | b -> b + 128
    L = np.mean(canal_L) * (100.0 / 255.0)
    a = np.mean(canal_a) - 128.0
    b = np.mean(canal_b) - 128.0

    # 5. Calcula o Índice de Escurecimento com os valores corrigidos
    ie = calcular_ie(L, a, b)

    print(f"L={L:.2f}")
    print(f"a={a:.2f}")
    print(f"b={b:.2f}")
    print(f"IE={ie:.2f}")
    print("-"*30)

    return {
        "escuras": escuros,
        "claras": claros,
        "L": L,
        "a": a,
        "b": b,
        "ie": ie
    }