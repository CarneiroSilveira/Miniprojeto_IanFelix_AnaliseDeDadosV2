import pandas as pd
import numpy as np
import re

#  Econverte os dados para pro formato date time
def adjust_datatime(df :pd.DataFrame):
    coluna_data = "DATA"
    df[coluna_data] = pd.to_datetime(df[coluna_data], errors="coerce")

# a mesma coisa da função acima trata os dados e depois trata os nulos
def ajust_cat(df: pd.DataFrame):
    df["PR_CAT"] = df["PR_CAT"].astype(str).apply(lambda x: re.sub(r"\s+", " ", x).strip())
    df["PR_CAT"] = np.where((df["PR_CAT"] == "") | (df["PR_CAT"] == "nan"), "Sem Categoria",df["PR_CAT"])

def cleaning_converting_children_column(df: pd.DataFrame):
    # Limpeza da coluna de filhos e convertendo para numero. 
    df["CL_FHL"] = df["CL_FHL"].astype(str).apply(lambda x: re.sub(r"[^0-9]", "", x))
    df["CL_FHL"] = pd.to_numeric( df["CL_FHL"], errors="coerce")
    df["CL_FHL"] = df["CL_FHL"].fillna(df["CL_FHL"].median())
