import pandas as pd

df = pd.read_csv("vendas.csv")
df["total"] = df["quantidade"] * df["preco"]

resumo = df.groupby("categoria").agg(
    total_vendido=("total", "sum"),
    itens_vendidos=("quantidade", "sum"),
    preco_medio=("preco", "mean"),
)
resumo = resumo.sort_values("total_vendido", ascending=False)
resumo.to_csv("resumo_categorias.csv")
print(resumo)