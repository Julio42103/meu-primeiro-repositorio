pessoa = {"nome": "Antedeguemom", "idade": 98, "cidade": "Pindamonhangaba", "profissao": "Ferreiro"}
print("1. Dicionário Original:", pessoa)
pessoa.update({"e-mail":"antedeguemom@gamil.com"})
print("2. Dicionário completo:", pessoa)
print("3. Dados linha a linha:")
for chave, valor in pessoa.items():
    print(f"   {chave}: {valor}")
