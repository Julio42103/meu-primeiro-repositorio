import re 

def limpar_nome(nome):
    """Remove espaços das pontase deixa cada palavra com inichial maiúscula"""
    return nome.strip().title()

def limpar_telefone(telefone):
    """Mantém apenas os dígitos do telefone"""
    return re.sub(r"\D", "", telefone)

def limpar_data(data):
    """Converte data do formato dd/mm/aaaa para aaaa-mm-dd"""
    dia, mes, ano = data.split("/")
    return f"{ano}-{mes}-{dia}"

if __name__ == "__main__":
    print(limpar_nome("  Maria da Rocha  "))  # Maria Da Rocha
    print(limpar_telefone("47) 99999-1234"))  # 47999991234
    print(limpar_data("25/12/2026"))  # 2026-12-25
    