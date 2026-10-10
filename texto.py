import re

def so_digitos(texto):
    return re.sub(r"\D", "", texto)

def normalizar_nome(nome):
    return nome.strip().title()

def formatar_data(texto):
    dia, mes, ano = texto.split("/")
    return f"{ano}-{mes}-{dia}"
if __name__ == "__main__":
    print(so_digitos("47) 99999-1234"))  # 47999991234
    print(normalizar_nome("  Maria da Rocha  "))  # Maria Da Rocha
    print(formatar_data("25/12/2026"))
      # 2023-12-31