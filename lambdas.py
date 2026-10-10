alunos = [
    {"nome": "Ana", "nota": 9.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Thaís", "nota": 7.5},
    {"nome": "Diego", "nota": 8.0},
    {"nome": "Amanda", "nota": 5.5},
]

ordenados = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)
print("ordenados por nota:")
for aluno in ordenados:
    print(aluno["nome"], aluno["nota"])

aprovados = list(filter(lambda aluno: aluno["nota"] >= 7, alunos))
print("Aprovados:")
for aluno in aprovados:
    print(aluno["nome"])
