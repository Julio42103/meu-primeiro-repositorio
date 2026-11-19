import pandas as pd

from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv("arquivos/imoveis_tratado.csv")

# 1. colunas de texto
print(df.select_dtypes(include="object").columns)

# 2. binárias para 0 e 1
mapa_bin = {"Sim": 1, "Não": 0}
df["aceita_pet"] = df["aceita_pet"].map(mapa_bin)
df["mobiliado"] = df["mobiliado"].map(mapa_bin)
print(df[["aceita_pet", "mobiliado"]].isna().sum())

# 3. ordinal com dicionário
ordem = {"Ruim": 0, "Regular": 1, "Bom": 2, "Ótimo": 3}
df["condicao_num"] = df["condicao"].map(ordem)
print(df["condicao_num"].isna().sum())

# 4. mesma coisa com OrdinalEncoder
enc = OrdinalEncoder(categories=[["Ruim", "Regular", "Bom", "Ótimo"]])
df["condicao_enc"] = enc.fit_transform(df[["condicao"]]).ravel()
print((df["condicao_num"] == df["condicao_enc"]).all())

