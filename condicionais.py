import pandas as pd
import numpy as np

df = pd.read_csv("arquivos/pedidos.csv")

# Colunas da atividade anterior
df["data"] = pd.to_datetime(df["data"])
df["mes"] = df["data"].dt.month
df["dia_semana"] = df["data"].dt.dayofweek

df["canal"] = df["canal"].str.strip().str.title()

nomes = {0: "seg", 1: "ter", 2: "qua", 3: "qui", 4: "sex", 5: "sab", 6: "dom"}
df["dia"] = df["dia_semana"].map(nomes)

def faixa_entrega(minutos):
    if pd.isna(minutos):
        return "sem entrega"
    if minutos <= 20:
        return "rápida"
    if minutos <= 35:
        return "normal"
    return "demorada"

df["faixa_entrega"] = df["tempo_entrega_min"].apply(faixa_entrega)

# 1) pedido_grande: qtd >= 3
df["pedido_grande"] = np.where(df["qtd"] >= 3, "sim", "nao")
print(df["pedido_grande"].value_counts())

# 2) perfil: 3 regras e default "sem nota"
regras = [
    df["avaliacao"] >= 4,
    df["avaliacao"] == 3,
    df["avaliacao"] <= 2,
]
perfis = ["satisfeito", "neutro", "insatisfeito"]
df["perfil"] = np.select(regras, perfis, default="sem nota")
print(df["perfil"].value_counts())

# 3) taxa_entrega com .loc (valor de exemplo: 5.0 só no Delivery)
df["taxa_entrega"] = 0.0
df.loc[df["canal"] == "Delivery", "taxa_entrega"] = 5.0
print(df["taxa_entrega"].value_counts())

# 4) faixa_tempo com pd.cut
limites = [0, 20, 30, 45, np.inf]
nomes_faixa = ["até 20", "21 a 30", "31 a 45", "mais de 45"]
df["faixa_tempo"] = pd.cut(df["tempo_entrega_min"], bins=limites, labels=nomes_faixa)
print(df["faixa_tempo"].value_counts())