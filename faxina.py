import csv

import limpeza



with open("sujo.csv", encoding="utf-8", newline="") as entrada:

    leitor = csv.DictReader(entrada)

    linhas = []

    for linha in leitor:

        linhas.append({

            "nome": limpeza.limpar_nome(linha["nome"]),

            "telefone": limpeza.limpar_telefone(linha["telefone"]),

            "data": limpeza.limpar_data(linha["data"]),

        })



with open("limpo.csv", "w", encoding="utf-8", newline="") as saida:

    escritor = csv.DictWriter(saida, fieldnames=["nome", "telefone", "data"])

    escritor.writeheader()

    escritor.writerows(linhas)



print(f"{len(linhas)} linhas gravadas em limpo.csv")

