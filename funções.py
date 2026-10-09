def e_bissexto(ano):
    """Retorna True se o ano for bissexto, se não False."""
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
def calcular_imc(peso, altura):
    """Calcula o IMC: peso (kg) dividido pela altura (m) ao quadrado."""
    return peso / (altura ** 2) 
print(e_bissexto(2000))  # True
print(e_bissexto(1900))  # False
print(e_bissexto(2024))  # True
print(e_bissexto(2023))  # False

print(calcular_imc(70, 1.75))  # 22.857142857142858
print(calcular_imc(80, 1.80))  # 24.691358024691358
