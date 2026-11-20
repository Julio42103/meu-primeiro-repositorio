from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

VARIAVEIS = ["temperatura_c", "umidade_pct", "vento_kmh", "chuva_mm", "alugueis"]
PASTA_FIGURAS = Path("figuras")
PASTA_FIGURAS.mkdir(exist_ok=True)

df = pd.read_csv("dias.csv")

linhas = []
for var in VARIAVEIS:
    serie = df[var].dropna()
    skew = stats.skew(serie)
    curtose = stats.kurtosis(serie)
    w, p = stats.shapiro(serie)
    linhas.append({"variavel": var, "skew": skew, "curtose": curtose,

                   "shapiro_W": w, "shapiro_p": p})
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(serie, kde=True, ax=ax)
    ax.set_title(f"Distribuição de {var}")
    fig.tight_layout()
    fig.savefig(PASTA_FIGURAS / f"hist_{var}.png", dpi=120)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(5, 5))
    stats.probplot(serie, dist="norm", plot=ax)
    ax.set_title(f"QQ-plot de {var}")
    fig.tight_layout()
    fig.savefig(PASTA_FIGURAS / f"qq_{var}.png", dpi=120)
    plt.close(fig)

print(pd.DataFrame(linhas).round(4).to_string(index=False))