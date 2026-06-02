import pandas as pd
import numpy as np
import utils.views_utils as Vutil
import utils.func_utils as Futil

# Configurações para deixar a exibição mais legível/ Sim Professora eu copiei essa parte dos exercicios. Mas só desta parte😅
pd.set_option('display.max_columns', None)   # Mostrar todas as colunas
pd.set_option('display.float_format', '{:.2f}'.format)  # 2 casas decimais

# importando as bibliotecas necessarias pro projeto 
# O argumento sep=";" serve para que a separação das colunas do arquivo sejam defididas por ; que é o padrão dos arquivos .csv

df = pd.read_csv("./Base-Varejo/Base-Varejo.csv",sep=";")

Vutil.views_brutecsv_statistics(df)

Futil.adjust_datatime(df)
Futil.ajust_pr_cat(df)

df = df.drop_duplicates()

Futil.generic_treatment_of_text_columns(df)
Futil.generic_treatment_of_number_columns(df)

print("Base de dados limpa!-----------")
print(df.info())