import pandas as pd

df = pd.read_csv("pedidos_prontos.csv")

print(", ".join(df.columns))