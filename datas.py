from datetime import datetime
texto = input("data de nascimento (dd/mm/aaaa): ")
nascimento = datetime.strptime(texto,"%d/%m/%Y")
print(nascimento)
hoje = datetime.now()
dias = (hoje - nascimento).days
idade = dias // 365
print(F"idade aproximada: {int(idade)} anos")
print(nascimento.weekday())

dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
numero = nascimento.weekday()
print(f"você nasceu em uma {dias_semana[numero]}")

natal = datetime(hoje.year, 12, 25)
if hoje > natal:
    natal = datetime(hoje.year + 1, 12, 25)
faltam = (natal - hoje).days
print(f"faltam {faltam} dias para o natal")
