import pandas as pd
import numpy as np

# o argumento df: pd.DataFrame é para que a função só consiga receber Data Fremes.

def views_brutecsv_statistics(df: pd.DataFrame, nome = "DataFrame"):
#   Trecho de codigo usado dos exemplos da aula teorica
    datas_invalidas = pd.to_datetime(df["DATA"], errors="coerce").isna().sum()
    categorias_vazias = df["PR_CAT"].astype(str).str.strip().eq("").sum()

    print("\nDatas inválidas:", datas_invalidas)
    print("=" * 55)
    print(f"  📊 DIAGNÓSTICO: {nome}")
    print("=" * 55)
    print(f"  Linhas:           {df.shape[0]:,}")
    print(f"  Colunas:          {df.shape[1]}")
    print(f"  Linhas duplicadas:{df.duplicated().sum():,}")
    print(f"  Datas inválidas: {datas_invalidas}")
    print(f"  Categorias vazias: {categorias_vazias}")
    print()
    
    nulos = df.isnull().sum()
    pct   = (nulos / len(df) * 100).round(1)
    
    print("  Coluna           | Tipo       | Nulos | % Nulos")
    print("  " + "-"*50)
    for col in df.columns:
        tipo = str(df[col].dtype)
        print(f"  {col:<18}| {tipo:<10} | {nulos[col]:<5} | {pct[col]}%")
    print("=" * 55)

def view_cleancsv_statistics(df: pd.DataFrame):
    filhos = df["CL_FHL"].dropna()

    print("\n===== ESTATÍSTICAS CL_FHL =====")

    print("Média:", np.mean(filhos))
    print("Mediana:", np.median(filhos))
    print("Desvio padrão:", np.std(filhos))
    print("Moda:")
    print(filhos.mode())

    print("Máximo:", np.max(filhos))
    print("Mínimo:", np.min(filhos))
    print("Contagem:", filhos.count())

    print("\nQuartis:")
    print(filhos.quantile([0.25, 0.50, 0.75]))

def grups(df: pd.DataFrame):
    print("\n===== COMPRAS POR GÊNERO =====")

    print(df.groupby("CL_GENERO").size().sort_values(ascending=False))

    print("\n===== COMPRAS POR CATEGORIA =====")

    print(df.groupby("PR_CAT").size().sort_values(ascending=False))