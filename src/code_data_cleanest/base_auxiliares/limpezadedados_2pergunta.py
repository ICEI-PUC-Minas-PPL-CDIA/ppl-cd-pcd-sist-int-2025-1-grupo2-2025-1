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
        
       
