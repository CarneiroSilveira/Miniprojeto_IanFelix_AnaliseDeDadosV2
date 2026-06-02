import pandas as pd

# Essa função trata os dados em formato invalido e os converte para NaT e depois converte os dados corretos para pro formato date time
def adjust_datatime(df :pd.DataFrame):
    coluna_data = "DATA"
    if coluna_data in df.columns:
        datas_invalidas = pd.to_datetime(df[coluna_data], errors="coerce").isna().sum()
        print("\nDatas inválidas:", datas_invalidas)
        df[coluna_data] = pd.to_datetime(df[coluna_data], errors="coerce")

# a mesma coisa da função acima trata os dados e depois trata os nulos
def ajust_pr_cat(df: pd.DataFrame):
    
    if "PR_CAT" in df.columns:
        categorias_vazias = (df["PR_CAT"].astype(str).str.strip() == "").sum()
        print("Categorias vazias:", categorias_vazias)
    if "PR_CAT" in df.columns:
        df["PR_CAT"] = df["PR_CAT"].fillna("Sem Categoria")
        df["PR_CAT"] = df["PR_CAT"].replace("", "Sem Categoria")

# Faz um tratamento generico nas colunas de String(ou no caso Objeto)
def generic_treatment_of_text_columns(df: pd.DataFrame):
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna("Desconhecido")

# Faz um tratamento generico nas colunas numericas
def generic_treatment_of_number_columns(df: pd.DataFrame):
    colunas_numericas = df.select_dtypes(include=["int64", "float64"]).columns

    for col in colunas_numericas:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())