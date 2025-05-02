import pandas as pd
import numpy as np
import glob
import os

DATA_PATH_PATTERN = './dados_mte/*.txt'

cbo_codes_dados = [
    '212405',
    '212410',
    '212415',
    '212420',
    '212305',
    '212315',
    '212320',
    '142515',
    '142520',
    '142525',
    '142535',
    '221105',
    '221205',
]

colunas_para_ler = [
    'CBO Ocupação 2002',
    'Vl Remun Média Nom',
    'Vl Remun Dezembro Nom',
    'Sexo Trabalhador',
    'Raça Cor',
    'IBGE Subsetor',
    'UF',
    'Escolaridade após 2005',
    'Idade',
]

novos_nomes_colunas = {
    'CBO Ocupação 2002': 'cbo',
    'Vl Remun Média Nom': 'salario_medio_nominal',
    'Vl Remun Dezembro Nom': 'salario_dezembro_nominal',
    'Sexo Trabalhador': 'genero_cod',
    'Raça Cor': 'raca_cod',
    'IBGE Subsetor': 'cnae_cod',
    'UF': 'uf_cod',
    'Escolaridade após 2005': 'escolaridade_cod',
    'Idade': 'idade',
}

map_genero = {1: 'Masculino', 2: 'Feminino', -1: 'Nao Identificado'}
map_raca = {
    1: 'Indigena', 2: 'Branca', 4: 'Preta', 8: 'Amarela', 9: 'Parda',
    -1: 'Nao Identificado', 6: 'Nao Informado'
}

def limpar_dados_mte(file_path, cbo_list, cols_to_read, new_col_names, map_gen, map_rac):
    try:
        print(f"Processando arquivo: {os.path.basename(file_path)}...")

        df = pd.read_csv(
            file_path,
            sep=';',
            encoding='latin1',
            usecols=cols_to_read,
            decimal=',',
            on_bad_lines='warn'
        )

        print(f"  Lidos {len(df)} registros.")

        df.rename(columns=new_col_names, inplace=True)

        if 'cbo' in df.columns:
             df['cbo'] = df['cbo'].astype(str).str.strip()
             df = df[df['cbo'].isin(cbo_list)]
             print(f"  Registros após filtro CBO: {len(df)}")
             if df.empty:
                 print("  Nenhum registro encontrado para os CBOs especificados neste arquivo.")
                 return None
        else:
            print("  Aviso: Coluna 'cbo' não encontrada após renomear.")
            return None

        coluna_salarial_escolhida = 'salario_medio_nominal'
        if coluna_salarial_escolhida in df.columns:
            df[coluna_salarial_escolhida] = pd.to_numeric(df[coluna_salarial_escolhida], errors='coerce')
            df.dropna(subset=[coluna_salarial_escolhida], inplace=True)
            df = df[df[coluna_salarial_escolhida] > 0]
            print(f"  Registros após limpeza de salário: {len(df)}")
        else:
             print(f"  Aviso: Coluna salarial '{coluna_salarial_escolhida}' não encontrada.")


        if 'genero_cod' in df.columns:
             df['genero'] = df['genero_cod'].map(map_gen).fillna('Nao Mapeado')
        if 'raca_cod' in df.columns:
             df['raca'] = df['raca_cod'].map(map_rac).fillna('Nao Mapeado')

        if 'uf_cod' in df.columns:
             df['uf'] = df['uf_cod'].astype(str).str.strip()

       
