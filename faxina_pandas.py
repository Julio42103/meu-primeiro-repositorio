import pandas as pd

df = pd.read_csv("contatos_sujos.csv")

df = df.drop_duplicates()
df["nota"] = df["nota"].fillna(df["nota"].mean())

df["nome"] = df["nome"].str.strip().str.title()
df["telefone"] = df["telefone"].str.replace(r"\D", "", regex=True)
df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")

df.to_csv("contatos_limpos.csv", index=False)
print(df)

# Comparação: faxina.py (Semana 5) tem ___ linhas; este código tem 10 linhas.

