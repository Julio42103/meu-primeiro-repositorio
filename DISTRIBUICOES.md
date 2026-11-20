# Perfil de distribuição — dias.csv



Números calculados em `distribuicoes_dias.py`. Figuras em `figuras/` (histograma com KDE e QQ-plot de cada variável).



| Variável | Skew | Curtose | Shapiro-Wilk (p) | Classificação | Transformação |

|---|---|---|---|---|---|

| temperatura_c | -0.034 | -1.033 | 0.0000 | Simétrica e achatada, não normal | Nenhuma |

| umidade_pct | -0.077 | -0.075 | 0.1352 | Aproximadamente normal | Nenhuma |

| vento_kmh | 1.524 | 3.803 | 0.0000 | Assimétrica à direita, caudas pesadas | log1p |

| chuva_mm | 5.730 | 38.208 | 0.0000 | Extremamente assimétrica à direita | log1p |

| alugueis | 0.025 | -0.347 | 0.0488 | Praticamente simétrica | Nenhuma |



## Justificativa



- **temperatura_c:** o skew é próximo de 0, então a distribuição é simétrica. A curtose de -1.03 indica topo achatado (caudas leves), e o Shapiro-Wilk (p < 0.05) rejeita a normalidade. Como a forma é simétrica, não vejo ganho em transformar.

- **umidade_pct:** skew e curtose próximos de 0 e p = 0.1352 (> 0.05). Não rejeita a normalidade, e o QQ-plot segue a reta.

- **vento_kmh:** skew de 1.52 mostra cauda longa à direita, e a curtose de 3.80 indica caudas pesadas (valores extremos de vento). Shapiro-Wilk rejeita a normalidade. Proponho `log1p` para reduzir a assimetria.

- **chuva_mm:** skew de 5.73 e curtose de 38.2 são extremos, e o W de 0.28 está muito longe de 1. Provavelmente há muitos dias sem chuva e poucos dias com chuva muito forte. `log1p` ajuda, mas não resolve totalmente os zeros. Alternativa: criar uma variável binária (choveu / não choveu).

- **alugueis:** skew e curtose baixos indicam forma quase simétrica. O p = 0.0488 está no limite de 0.05, e o Shapiro-Wilk é sensível a pequenos desvios em amostras grandes. Considero aproximadamente normal, sem transformação.

