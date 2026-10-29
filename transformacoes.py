import pandas as pd

df = pd.read_csv("arquivos/pedidos.csv")

# 1) Data e colunas mes e dia_semana
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.month
df["dia_semana"] = df["data"].dt.dayofweek

# 2) Padronizar canal (devem sobrar 3)
df["canal"] = df["canal"].str.strip().str.title()
print(df["canal"].value_counts())

# 3) Coluna dia (seg a dom)
nomes = {0: "seg", 1: "ter", 2: "qua", 3: "qui", 4: "sex", 5: "sab", 6: "dom"}
df["dia"] = df["dia_semana"].map(nomes)

# 4) faixa_entrega com função própria
def faixa_entrega(minutos):
    if pd.isna(minutos):
        return "sem entrega"
    if minutos <= 20:
        return "rápida"
    if minutos <= 35:
        return "normal"
    return "demorada"

df["faixa_entrega"] = df["tempo_entrega_min"].apply(faixa_entrega)

print(df.head())