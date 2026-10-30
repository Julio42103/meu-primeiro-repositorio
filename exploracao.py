import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

pedidos = pd.read_csv("pedidos.csv")
produtos = pd.read_csv("produtos.csv")

df = pedidos.merge(produtos, on="id_produto", how="left")
os.makedirs("graficos", exist_ok=True)
entrega = df["tempo_entrega_min"].dropna()

# Gráfico 1a: com os extremos

plt.figure(figsize=(8, 5))
sns.histplot(entrega, bins=30)
plt.title("Tempo de entrega (com extremos)")
plt.xlabel("Minutos")
plt.ylabel("Pedidos")
plt.savefig("graficos/hist_entrega_com_extremos.png")
plt.close()

# Gráfico 1b: sem os extremos

q1 = entrega.quantile(0.25)
q3 = entrega.quantile(0.75)
limite = q3 + 1.5 * (q3 - q1)

entrega_sem_extremos = entrega[entrega <= limite]

plt.figure(figsize=(8, 5))
sns.histplot(entrega_sem_extremos, bins=30)
plt.title("Tempo de entrega (sem extremos)")
plt.xlabel("Minutos")
plt.ylabel("Pedidos")
plt.savefig("graficos/hist_entrega_sem_extremos.png")
plt.close()

# Gráfico 2: boxplot de qtd

plt.figure(figsize=(6, 5))
sns.boxplot(y=df["qtd"])
plt.title("Quantidade por pedido")
plt.ylabel("Unidades")
plt.savefig("graficos/boxplot_qtd.png")
plt.close()

# Histograma do tempo de entrega
# O que vi: com os extremos, quase tudo fica entre 13 e 40 min e um valor isolado
#   perto de 480 achata o gráfico. Sem os extremos, dá para ver o formato real.
# O que faria: investigar se o 480 é erro de digitação ou atraso real e, como
#   83% da coluna é nula, descobrir por que falta o tempo antes de usar a coluna.

# Gráfico 3: pedidos por dia da semana

df["data"] = pd.to_datetime(df["data"])
dias = {0: "Seg", 1: "Ter", 2: "Qua", 3: "Qui", 4: "Sex", 5: "Sáb", 6: "Dom"}
df["dia_semana"] = df["data"].dt.dayofweek.map(dias)
ordem = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="dia_semana", order=ordem)
plt.title("Pedidos por dia da semana")
plt.xlabel("Dia")
plt.ylabel("Pedidos")
plt.savefig("graficos/countplot_dia_semana.png")
plt.close()

# Boxplot de qtd

# O que vi: mediana em 5 unidades, caixa de 3 a 9 e sem pontos isolados fora dos
#   bigodes (qtd vai de 1 a 12), ou seja, sem outliers claros.
# O que faria: manter a coluna como está e conferir se pedidos de 12 unidades
#   são de um tipo de cliente ou produto específico.

# Countplot por dia da semana

# O que vi: os pedidos crescem de sexta a domingo. Domingo tem mais (~150) e
#   quinta tem menos (~65). Segunda a quinta ficam parecidas, entre 65 e 77.
# O que faria: checar se isso se repete em todas as semanas do período e se o
#   canal ou a categoria muda no fim de semana, para planejar estoque e entrega.