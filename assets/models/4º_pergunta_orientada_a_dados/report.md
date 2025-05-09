# 1. Upload do arquivo (ZIP) para o Colab
from google.colab import files
uploaded = files.upload()  # Faça upload do arquivo baixado do Kaggle (.zip)

import os
import zipfile

# 2. Extrair o arquivo ZIP
zip_files = [f for f in os.listdir() if f.endswith('.zip')]
if zip_files:
    zip_path = zip_files[0]
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()
    print('ZIP extraído!')

# 3. Descobrir nome do CSV extraído
csv_files = [f for f in os.listdir() if f.endswith('.csv')]
if len(csv_files) == 0:
    raise Exception("Nenhum .csv encontrado! Confira o upload e a extração.")
csv_path = csv_files[0]
print(f"Usando arquivo CSV: {csv_path}")

# 4. Ler o CSV
import pandas as pd
df_brazil = pd.read_csv(csv_path)

# 5. Detecção automática dos nomes das colunas principais
print("\nColunas originais:")
for col in df_brazil.columns:
    print(f"- {col}")

# Garante pegar as colunas certas, mesmo com nomes diferentes
faixa_sal_col = [col for col in df_brazil.columns if "faixa salarial" in col.lower()]
exp_col = [col for col in df_brazil.columns if "experiência" in col.lower() or "trabalha com dados" in col.lower()]
col_sql = [col for col in df_brazil.columns if "sql" in col.lower()]
col_r = [col for col in df_brazil.columns if (col.lower().strip().endswith(" r") or col.lower().strip() == 'r')]
col_python = [col for col in df_brazil.columns if "python" in col.lower()]
col_js = [col for col in df_brazil.columns if "javascript" in col.lower()]

print("\nColuna identificada para R:", col_r if col_r else "NÃO ENCONTRADA")

rename_dict = {}
if faixa_sal_col: rename_dict[faixa_sal_col[0]] = "P2h"
if exp_col: rename_dict[exp_col[0]] = "P2i"
if col_sql: rename_dict[col_sql[0]] = "P4d1"
if col_r: rename_dict[col_r[0]] = "P4d2"
if col_python: rename_dict[col_python[0]] = "P4d3"
if col_js: rename_dict[col_js[0]] = "P4d14"

df_brazil = df_brazil.rename(columns=rename_dict)

print("\nColunas após rename automático:")
print(df_brazil.columns.tolist())

# Ajusta dicionário de linguagens para só o que existir no DataFrame
linguagens = {}
if "P4d1" in df_brazil.columns: linguagens["P4d1"] = "SQL"
if "P4d2" in df_brazil.columns: linguagens["P4d2"] = "R"
if "P4d3" in df_brazil.columns: linguagens["P4d3"] = "Python"
if "P4d14" in df_brazil.columns: linguagens["P4d14"] = "JavaScript"

print("\nLinguagens encontradas:", linguagens if linguagens else "Nenhuma encontrada!")

if "P2h" in df_brazil.columns:
    print("\nCategorias detectadas para faixa salarial (P2h):")
    print(df_brazil["P2h"].dropna().unique())

# ---------- ANALISES E GRÁFICOS --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

order_faixa = [
    'Até R$ 1.000', 'R$ 1.001 a R$ 2.000', 'R$ 2.001 a R$ 3.000', 'R$ 3.001 a R$ 4.000',
    'R$ 4.001 a R$ 6.000', 'R$ 6.001 a R$ 8.000', 'R$ 8.001 a R$ 12.000',
    'R$ 12.001 a R$ 16.000', 'R$ 16.001 a R$ 20.000', 'Mais de R$ 20.000',
    'até R$ 1.000', 'mais de R$ 20.000'
]

salario_map = {
    'Até R$ 1.000': 1,
    'R$ 1.001 a R$ 2.000': 2,
    'R$ 2.001 a R$ 3.000': 3,
    'R$ 3.001 a R$ 4.000': 4,
    'R$ 4.001 a R$ 6.000': 5,
    'R$ 6.001 a R$ 8.000': 6,
    'R$ 8.001 a R$ 12.000': 7,
    'R$ 12.001 a R$ 16.000': 8,
    'R$ 16.001 a R$ 20.000': 9,
    'Mais de R$ 20.000': 10,
    'até R$ 1.000': 1,
    'mais de R$ 20.000': 10
}

if "P2h" in df_brazil.columns and linguagens:
    df_langs = df_brazil.copy()
    df_melt = df_langs.melt(id_vars="P2h", value_vars=list(linguagens.keys()),
                            var_name="Linguagem", value_name="Usa")
    df_melt = df_melt[df_melt["Usa"] == "Sim"].copy()
    df_melt["Linguagem"] = df_melt["Linguagem"].map(linguagens)

    # Gráfico de distribuição por faixa salarial
    plt.figure()
    sns.countplot(data=df_melt, x="P2h", order=order_faixa, hue="Linguagem")
    plt.title("Distribuição de Faixa Salarial por Linguagem (Brasil)")
    plt.xlabel("Faixa Salarial")
    plt.ylabel("Número de Profissionais")
    plt.xticks(rotation=45)
    plt.legend(title="Linguagem")
    plt.tight_layout()
    plt.show()

    # Gráfico de pizza com proporção de uso (só exibe se houver dados)
    uso_linguagens = {ling: (df_brazil[col] == "Sim").sum() for col, ling in linguagens.items()}
    valores = list(uso_linguagens.values())
    if sum(valores) > 0:
        plt.figure()
        plt.pie(valores, labels=uso_linguagens.keys(), autopct='%1.1f%%', startangle=140)
        plt.title("Proporção de uso de Linguagens (Brasil)")
        plt.axis('equal')
        plt.show()
    else:
        print("Nenhum valor 'Sim' encontrado nas colunas de linguagem. Pizza não será exibida.")

    # Boxplot de faixa salarial por linguagem
    df_box = df_melt.copy()
    df_box["FaixaNum"] = df_box["P2h"].map(salario_map)
    plt.figure()
    sns.boxplot(data=df_box, x="Linguagem", y="FaixaNum")
    plt.title("Boxplot de Faixa Salarial por Linguagem")
    plt.xlabel("Linguagem")
    plt.ylabel("Faixa Salarial (ordinal)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    # Scatterplot: tempo de experiência vs. faixa salarial (Python)
    if "Python" in linguagens.values() and "P2i" in df_brazil.columns:
        df_disp = df_melt[df_melt["Linguagem"] == "Python"].copy()
        df_disp["FaixaNum"] = df_disp["P2h"].map(salario_map)
        df_disp["TempoExp"] = df_brazil.loc[df_disp.index, "P2i"] if "P2i" in df_brazil.columns else None
        df_disp = df_disp.dropna(subset=["TempoExp", "FaixaNum"])
        plt.figure()
        sns.scatterplot(data=df_disp, x="TempoExp", y="FaixaNum", hue="Linguagem")
        plt.title("Tempo de Experiência vs. Faixa Salarial (Python)")
        plt.xlabel("Tempo de Experiência (anos)")
        plt.ylabel("Faixa Salarial (ordenada)")
        plt.tight_layout()
        plt.show()

# Correlação entre experiência e uso de linguagens
if "P2i" in df_brazil.columns and linguagens:
    df_brazil["P2i"] = pd.to_numeric(df_brazil["P2i"], errors="coerce")
    df_corr = df_brazil.copy()
    for col in linguagens.keys():
        df_corr[col] = df_corr[col].map({"Sim": 1, "Não": 0})
    cols_corr = ["P2i"] + list(linguagens.keys())
    heat_data = df_corr[cols_corr].corr()
    plt.figure()
    sns.heatmap(heat_data, annot=True, cmap="coolwarm")
    plt.title("Correlação entre Tempo de Experiência e Linguagens")
    plt.show()
