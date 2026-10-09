import re
with open("contatos.csv", encoding="utf-8") as f:
    linhas = f.readlines()
for linha in linhas[1:]:
    if not linha.strip():
        continue
    nome, telefone = linha.strip().split(",")
    numero = re.sub(r"\D", "", telefone)
    if re.fullmatch(r"\d{11}", numero):
        print(nome, numero, "é válido")
    else:
        print(nome, numero, "é inválido")
