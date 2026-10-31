import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("graficos", exist_ok=True)

# Passo 1: carregar e unir os dados

pedidos = pd.read_csv("pedidos.csv")
produtos = pd.read_csv("produtos.csv")

df = pedidos.merge(produtos, on="id_produto", how="left")

# Passo 2: primeiro olhar

print("Shape:", df.shape)
print(df.head())
df.info()
print(df.describe())

# O que vi: mediana em 1 unidade, 75% dos pedidos com até 2, mas há valores
#   fora do padrão: mínimo -1 (quantidade negativa) e máximo 40.
# O que faria: tratar o -1 como erro de registro e investigar o pedido de 40
#   antes de usar a coluna em qualquer média.

# Passo 3: nulos

print(df.isnull().mean())

# Passo 4: duplicados e valores impossíveis

print("Duplicadas:", df.duplicated().sum())
print("qtd negativa:", (df["qtd"] < 0).sum())
print("qtd > 20:", (df["qtd"] > 20).sum())

# Passo 5: canal

print("Antes:", df["canal"].nunique(), "valores distintos")

df["canal"] = df["canal"].str.strip().str.lower()

print("Depois:", df["canal"].nunique(), "valores distintos")
print(df["canal"].value_counts())

# Passo 6: limpeza

antes = len(df)
df = df.drop_duplicates()
df = df[df["qtd"] >= 0]
print("Linhas antes:", antes, "| depois:", len(df))

# Passo 7: gráficos

plt.figure(figsize=(6, 5))
sns.countplot(data=df, x="canal")
plt.title("Pedidos por canal")
plt.savefig("graficos/canal.png")
plt.close()

plt.figure(figsize=(6, 5))
sns.boxplot(y=df["qtd"])
plt.title("Quantidade por pedido")
plt.savefig("graficos/boxplot_qtd.png")
plt.close()

df["data"] = pd.to_datetime(df["data"])
dias = {0: "Seg", 1: "Ter", 2: "Qua", 3: "Qui", 4: "Sex", 5: "Sáb", 6: "Dom"}
df["dia_semana"] = df["data"].dt.dayofweek.map(dias)
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="dia_semana", order=list(dias.values()))
plt.title("Pedidos por dia da semana")
plt.savefig("graficos/dia_semana.png")
plt.close()

