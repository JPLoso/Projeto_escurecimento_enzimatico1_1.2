import json

def salvar_json(resultados, caminho_saida="resultado.json"):
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=4)