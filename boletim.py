import csv

with open("notas.csv", newline='', encoding="utf-8") as f:
    for aluno in csv.DictReader(f):
        media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
        print(aluno["nome"], "tem média", media)

        import csv
        resultados = []
        with open("notas.csv", newline='', encoding="utf-8") as f:
            for aluno in csv.DictReader(f):
                media = (float(aluno["nota1"]) + float(aluno["nota2"])) / 2
                if media >= 7:
                    situacao = "Aprovado"
                else:
                    situacao = "Reprovado"
                    print(aluno["nome"], "tem média", media, "-", situacao)
                    resultados.append({"nome": aluno["nome"], "media": media, "situacao": situacao})
                    