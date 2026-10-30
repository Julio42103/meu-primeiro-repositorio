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
print(df["canal"].unique())

# Observações:

# 1. tempo_entrega_min tem outlier: (máximo 480 contra 75% em 40 minutos), mas só~17% das linhas tem valor.
# 2. preco é sempre maior que custo (custo 1,7 a 5,4; preco 5 a 15).
# 3. tempo_entrega_min tem ~83% de nulos; id_cliente (~19%) e avaliacao (~17%)
#    também têm nulos. Há 12 linhas duplicadas.
# 4. canal tem 9 valores distintos, mas são só 3 canais (App, Delivery, Balcão)
#    escritos com maiúsculas/minúsculas diferentes e espaços sobrando.