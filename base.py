import pandas as pd
import utils.views_utils as Vutil
import utils.func_utils as Futil

# Configurações para deixar a exibição mais legível/ Sim Professora eu copiei essa parte dos exercicios. Mas só desta parte😅
pd.set_option('display.max_columns', None)   # Mostrar todas as colunas
pd.set_option('display.float_format', '{:.2f}'.format)  # 2 casas decimais

# importando as bibliotecas necessarias pro projeto 
# O argumento sep=";" serve para que a separação das colunas do arquivo sejam defididas por ; que é o padrão dos arquivos .csv

# =====================================
# 1 - IMPORTANDO OS DADOS!
# =====================================

df = pd.read_csv("./Base-Varejo/Base-Varejo.csv",sep=";")

# Remove colunas vazias criadas pelos ; extras
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# =====================================
# 2 - IDENTIFICANDO PROBLEMAS!
# =====================================

Vutil.views_brutecsv_statistics(df)

# =====================================
# 3 - LIMPANDO OS DADOS!
# =====================================

Futil.adjust_datatime(df)

df = df.drop_duplicates()

Futil.ajust_cat(df)

Futil.cleaning_converting_children_column(df)

# =====================================
# 4 - ESTATÍSTICA DESCRITIVA
# =====================================

Vutil.view_cleancsv_statistics(df)

# =====================================
# 5 - AGRUPAMENTOS
# =====================================
Vutil.grups(df)