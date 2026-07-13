import cv2
import numpy as np
from Aplicativo.Processamento.calc_percentual import calc_percentuais
from Aplicativo.Processamento.formulas_lab import calcular_ie

def analisar_imagem(img, mask):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    escuros, claros = calc_percentuais(mask, gray)

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    pixels = lab[mask > 0]

    if len(pixels) == 0:
        return {
            "escuras": 0,
            "claras": 0,
            "L": 0,
            "a": 0,
            "b": 0,
            "ie": 0
        }

    L = np.mean(pixels[:,0]) * (100/255)
    a = np.mean(pixels[:,1]) - 128
    b = np.mean(pixels[:,2]) - 128

    ie = calcular_ie(L,a,b)

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