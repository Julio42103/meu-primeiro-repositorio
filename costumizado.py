import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_csv("pedidos_prontos.csv")
fat = df.groupby("categoria")["total"].sum().sort_values(ascending=False)

def reais(x, pos):
    return "R$ " + f"{x:,.0f}".replace(",", ".")

cores = ["#1f77b4"] * len(fat)
cores[0] = "#d62728"  # barra de maior valor em destaque

fig, ax = plt.subplots(figsize=(9, 5))
barras = ax.bar(fat.index, fat.values, color=cores)

ax.set_title("Faturamento por categoria")
ax.set_xlabel("Categoria")
ax.set_ylabel("Faturamento (R$)")
ax.yaxis.set_major_formatter(FuncFormatter(reais))
ax.annotate("Maior faturamento",
            xy=(0, fat.values[0]),
            xytext=(0, fat.values[0] * 1.05),
            ha="center")

plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("categoria.png", dpi=150)
plt.show()