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

       
