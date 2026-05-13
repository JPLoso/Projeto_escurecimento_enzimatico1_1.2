import json

def carregar_json(caminho):
    # Verifica se o arquivo existe
    import os
    if not os.path.exists(caminho):
        raise FileNotFoundError("Arquivo JSON não encontrado")

    # Abre e carrega o JSON
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Validação básica do formato
    if not isinstance(dados, dict):
        raise ValueError("Formato de JSON inválido")

    return dados