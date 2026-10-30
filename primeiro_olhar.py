import pandas as pd

pedidos = pd.read_csv("pedidos.csv")
produtos = pd.read_csv("produtos.csv")
print(pedidos.columns.tolist())
print(produtos.columns.tolist())

df = pedidos.merge(produtos,on="id_produto", how="left")
print(df.shape)
print(df.head())
df.info()
print(df.describe())
print(df.isnull().mean())
print(df.duplicated().sum())

# Observações:

# 1. tempo_entrega_min tem outlier: máximo 480 contra 75% em 40 minutos.
# 2. preco é sempre maior que custo (custo 1,7 a 5,4; preco 5 a 15).
# 3. (preencher depois de ver count/info: colunas com nulos)