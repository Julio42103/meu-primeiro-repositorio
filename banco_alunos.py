alunos = [{"nome": "Carol", "nota": 8.5}, {"nome": "Joao", "nota": 7.5}, {"nome": "Maria", "nota": 5.5}, {"nome": "Pedro", "nota": 6.5}]
aprovados = 0
for aluno in alunos:
    if aluno["nota"] >= 7:
        print(aluno["nome"], aluno["nota"])
        aprovados += 1
print("Total de alunos aprovados:", aprovados)