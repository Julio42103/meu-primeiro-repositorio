# Relatório de EDA: Cafeteria

## Dados analisados
- `pedidos.csv` unido a `produtos.csv` pela coluna `id_produto`.
- 687 linhas e 12 colunas antes da limpeza; 672 linhas depois.

## Tabela de problemas
| Problema | Quantidade | Decisão |
|---|---|---|
| Linhas duplicadas | 12 | Remover |
| `qtd` negativa | 3 pedidos | Remover |
| `qtd` acima de 20 | 4 pedidos | Investigar antes de decidir |
| `canal` com grafias diferentes | 9 valores para 3 canais | Padronizar (tirar espaços e pôr em minúsculas) |
| `tempo_entrega_min` com nulos | ~83% da coluna | Não usar a coluna sem entender por que falta |

Também há nulos em `id_cliente` (~19%) e `avaliacao` (~17%), ainda sem decisão.

## Achados do negócio

1. O balcão é o canal com mais pedidos (309), seguido do app (253) e do delivery (125), que tem menos da metade do balcão.
2. Os pedidos se concentram no fim de semana: domingo tem cerca de 150 e quinta cerca de 65.
3. Quase todos os pedidos têm 1 ou 2 unidades, mas existem pedidos isolados com 40, que precisam ser verificados.

## Gráficos

- `graficos/canal.png`
- `graficos/boxplot_qtd.png`
- `graficos/dia_semana.png`