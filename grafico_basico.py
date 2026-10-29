import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pedidos_prontos.csv")
pedidos_mes = df.groupby("mes").size()

plt.plot(pedidos_mes.index, pedidos_mes.values, marker="o")
plt.title("Pedidos por mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade de pedidos")
plt.show()
fat_canal = df.groupby("canal")["total"].sum()

plt.figure()
plt.bar(fat_canal.index, fat_canal.values)
plt.title("Faturamento por canal")
plt.xlabel("Canal")
plt.ylabel("Faturamento")
plt.savefig("canal.png")
plt.show()
plt.figure()
plt.scatter(df["preco"], df["qtd"], alpha=0.5)
plt.title("Preço x Quantidade")
plt.xlabel("Preço")
plt.ylabel("Quantidade")
plt.show()

# Dispersão preço x quantidade:
# (escreva aqui o que você vê: tem tendência? algum ponto fora do padrão?)

# Dispersão preço x quantidade:
# Não há relação clara entre preço e quantidade: a maioria dos pedidos
# tem de 1 a 4 unidades em qualquer faixa de preço.
# Há 4 outliers com quantidade perto de 40, em preços diferentes,
# que merecem ser verificados (pedido grande ou erro de dado).


