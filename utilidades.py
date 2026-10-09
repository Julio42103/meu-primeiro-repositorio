def media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas)

def desconto(preço, percentual=10):
    """Calcula o preço com desconto. Percentual padrão é 10%."""
    return preço - (preço * percentual / 100)

def estatisticas(notas):
    """Retorna o mínimo, o máximo e a média de uma lista de notas."""
    return min(notas), max(notas), media(notas)

def situação(media):
    """Retorna 'Aprovado' se a media for maior ou igual a 7, caso contrário 'Reprovado'."""
    return "Aprovado" if media >= 7 else "Reprovado"

notas = [8, 6.5, 9, 7]
print(media(notas))  # 7.625
print(media(notas=[5, 7, 10]))  # 7.333333333333333

print(desconto(200))  # 180.0
print(desconto(200, 20))  # 160.0
print(desconto(preço=200, percentual=30))  # 140.0

mínimo, máximo, média = estatisticas(notas)
print(mínimo, máximo, média)  # 6.5 9 7.625
print(situação(média))  # Aprovado
print(situação(media=5))  # Reprovado