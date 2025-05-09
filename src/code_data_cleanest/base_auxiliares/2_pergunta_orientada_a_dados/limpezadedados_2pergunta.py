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

  # Mapear gênero
        if 'genero_cod' in df.columns:
            df['genero'] = df['genero_cod'].map(self.gender_mapping).fillna('Nao Mapeado')
            
        # Mapear raça/cor
        if 'raca_cod' in df.columns:
            df['raca'] = df['raca_cod'].map(self.race_mapping).fillna('Nao Mapeado')
            
        # Ajustar UF
        if 'uf_cod' in df.columns:
            df['uf'] = df['uf_cod'].astype(str).str.strip()
            
        return df
        
    def drop_redundant_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove colunas redundantes após o mapeamento."""
        if df is None or df.empty:
            return df
            
        cols_to_drop = ['genero_cod', 'raca_cod', 'uf_cod']
        present_cols = [col for col in cols_to_drop if col in df.columns]
        
        if present_cols:
            df.drop(columns=present_cols, inplace=True, errors='ignore')
            
        return df
    
    def process_file(self, file_path: str) -> Optional[pd.DataFrame]:
        """Processa um arquivo completo aplicando todas as transformações."""
        try:
            # Etapa 1: Leitura do arquivo
            df = self.read_file(file_path)
            
            # Etapa 2: Filtrar por CBO
            df = self.filter_by_cbo(df)
            
            # Etapa 3: Limpar dados de salário
            df = self.clean_salary_data(df)
            
            # Etapa 4: Mapear campos categóricos
            df = self.map_categorical_fields(df)
            
            # Etapa 5: Remover colunas redundantes
            df = self.drop_redundant_columns(df)

  if df is not None and not df.empty:
                print(f"  Limpeza concluída para este arquivo. Registros finais: {len(df)}")
                
            return df
            
        except Exception as e:
            print(f"Erro ao processar o arquivo {file_path}: {e}")
            return None

    def process_all_files(self, file_pattern: str, output_file: str) -> None:
        """Processa todos os arquivos correspondentes ao padrão e salva o resultado."""
        all_files = glob.glob(file_pattern)
        
        if not all_files:
            print(f"Nenhum arquivo encontrado no padrão: {file_pattern}")
            return
            
        print(f"Arquivos encontrados: {len(all_files)}")
        
        processed_dataframes = []
        
        for file_path in all_files:
            df_processed = self.process_file(file_path)
            if df_processed is not None and not df_processed.empty:
                processed_dataframes.append(df_processed)
        
        if not processed_dataframes:
            print("\nNenhum dado relevante encontrado ou processado nos arquivos fornecidos.")
            return
            
        # Concatenar todos os DataFrames processados
        final_df = pd.concat(processed_dataframes, ignore_index=True)
        print(f"\nProcessamento concluído. Total de registros agregados: {len(final_df)}")
        
        # Salvar o resultado final
        try:
            final_df.to_csv(output_file, index=False, encoding='utf-8')
            print(f"Dados auxiliares limpos salvos em: {output_file}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo CSV final: {e}")


# Ponto de entrada principal
if __name__ == "__main__":
    # Instantiate the processor
    processor = MTEDataProcessor()
    
    # Define file pattern and output file
    DATA_PATH_PATTERN = './dados_mte/*.txt'
    OUTPUT_FILE = 'dados_auxiliares_mte_limpos.csv'
    
    # Process all files
    processor.process_all_files(DATA_PATH_PATTERN, OUTPUT_FILE)
        
       
