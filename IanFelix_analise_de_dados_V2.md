# Miniprojeto Ian Felix — Análise de Dados V2

Projeto em Python para limpeza, diagnóstico e análise exploratória de uma base de varejo.

## Estrutura do projeto

- `base.py`: script principal que carrega os dados, executa a limpeza e chama as análises.
- `utils/func_utils.py`: funções de tratamento e padronização dos dados.
- `utils/views_utils.py`: funções de diagnóstico e estatística descritiva.
- `Base-Varejo/Base-Varejo.csv`: base original usada na análise.

## Principais etapas da análise

1. Importação do CSV com separador `;`.
2. Remoção de colunas vazias criadas por separadores extras.
3. Diagnóstico da base bruta.
4. Limpeza das colunas.
5. Estatísticas descritivas e agrupamentos por gênero e categoria.

## Insights obtidos da análise dos dados

- A base possui problemas de qualidade que exigem limpeza antes da análise, principalmente em datas inválidas e valores ausentes.
- A coluna `PR_CAT` tinha registros vazios ou inconsistentes, então foi padronizada para evitar perdas na agregação por categoria.
- A coluna `CL_FHL` mistura texto e números, o que mostra que a base precisa de tratamento antes de cálculos estatísticos.
- A análise por gênero permite comparar o volume de compras entre diferentes perfis de clientes.
- A análise por categoria ajuda a identificar quais grupos de produtos concentram mais registros de compra.
- O uso de média, mediana e quartis em `CL_FHL` é importante para entender a distribuição e reduzir o impacto de valores extremos.