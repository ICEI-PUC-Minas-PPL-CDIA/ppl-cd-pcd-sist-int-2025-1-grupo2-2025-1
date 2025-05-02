import pandas as pd
import numpy as np
import glob
import os
from typing import Dict, List, Optional


class MTEDataProcessor:
    """Classe para processar dados do MTE relacionados a profissionais de tecnologia."""
    
    def __init__(self):
        # Códigos CBO para profissionais de tecnologia/dados
        self.cbo_codes = [
            '212405', '212410', '212415', '212420',  # Analistas de sistemas
            '212305', '212315', '212320',            # Analistas de dados
            '142515', '142520', '142525', '142535',  # Gerentes de TI
            '221105', '221205',                      # Outros 
profissionais relevantes
        ]
        
        # Mapeamentos para transformação de dados
        self.column_mapping = {
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
        
        self.gender_mapping = {
            1: 'Masculino', 
            2: 'Feminino', 
            -1: 'Nao Identificado'
        }
        
        self.race_mapping = {
            1: 'Indigena', 
            2: 'Branca', 
            4: 'Preta', 
            8: 'Amarela', 
            9: 'Parda',
            -1: 'Nao Identificado', 
            6: 'Nao Informado'
        }
         # Colunas a serem lidas do arquivo
        self.columns_to_read = list(self.column_mapping.keys())

    def read_file(self, file_path: str) -> Optional[pd.DataFrame]:
        """Lê um arquivo do MTE e retorna um DataFrame."""
        try:
            print(f"Processando arquivo: {os.path.basename(file_path)}...")
            
            df = pd.read_csv(
                file_path,
                sep=';',
                encoding='latin1',
                usecols=self.columns_to_read,
                decimal=',',
                on_bad_lines='warn'
            )
            
            print(f"  Lidos {len(df)} registros.")
            return df
            
        except Exception as e:
            print(f"Erro ao ler o arquivo {file_path}: {e}")
            return None
    
    def filter_by_cbo(self, df: pd.DataFrame) -> Optional[pd.DataFrame]:
        """Filtra o DataFrame pelos códigos CBO definidos."""
        if df is None or df.empty:
            return None
            
        df.rename(columns=self.column_mapping, inplace=True)
        
        if 'cbo' not in df.columns:
            print("  Aviso: Coluna 'cbo' não encontrada após renomear.")
            return None
            
        df['cbo'] = df['cbo'].astype(str).str.strip()
        filtered_df = df[df['cbo'].isin(self.cbo_codes)]
        
        print(f"  Registros após filtro CBO: {len(filtered_df)}")
        
        if filtered_df.empty:
            print("  Nenhum registro encontrado para os CBOs especificados neste arquivo.")
            return None
            
        return filtered_df
    
    def clean_salary_data(self, df: pd.DataFrame) -> Optional[pd.DataFrame]:
        """Limpa e valida os dados salariais."""
        if df is None or df.empty:
            return None
            
        salary_column = 'salario_medio_nominal'
        
        if salary_column not in df.columns:
            print(f"  Aviso: Coluna salarial '{salary_column}' não encontrada.")
            return df
            
        df[salary_column] = pd.to_numeric(df[salary_column], errors='coerce')
        df.dropna(subset=[salary_column], inplace=True)
        df = df[df[salary_column] > 0]
        
        print(f"  Registros após limpeza de salário: {len(df)}")
        return df
    
    def map_categorical_fields(self, df: pd.DataFrame) -> pd.DataFrame:
        """Mapeia códigos para valores legíveis em campos categóricos."""
        if df is None or df.empty:
            return df
        
       
