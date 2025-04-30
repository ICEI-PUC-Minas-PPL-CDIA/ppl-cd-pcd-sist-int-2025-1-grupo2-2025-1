# Explicação código *modelo2_remasterizado.ipynb*
### Código em pyhton:
    # --- Etapa 1: Configuração do Ambiente, Upload e Carregamento ---
    
    # Importar bibliotecas necessárias
    import pandas as pd
    import numpy as np
    import re
    import io
    from google.colab import files
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.preprocessing import OrdinalEncoder, StandardScaler
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    import lightgbm as lgb
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    
    # Instalar/Importar bibliotecas opcionais
    try:
        from unidecode import unidecode
    except ImportError:
        print("Instalando unidecode para remover acentos...")
        !pip install unidecode
        from unidecode import unidecode
        print("Unidecode instalado.")
    
    try:
        import shap
    except ImportError:
        print("Instalando shap para interpretação do modelo...")
        !pip install shap
        import shap
        print("Shap instalado.")
    
    try:
        import graphviz
    except ImportError:
        print("Instalando graphviz para visualização de árvore...")
        !apt-get install -qq graphviz > /dev/null # Instala dependência do sistema no Colab
        !pip install graphviz > /dev/null
        import graphviz
        print("Graphviz instalado.")
    
    # Ignorar warnings específicos que podem poluir a saída
    warnings.filterwarnings("ignore", category=UserWarning, module='shap')
    warnings.filterwarnings("ignore", category=FutureWarning)
## Explicação (Etapa 1 - Setup):
### Importações Principais: **Importa as bibliotecas essenciais:**
  - pandas e numpy: **Para manipulação de dados (DataFrames, arrays).**
  - re: **Para expressões regulares (usadas na limpeza).**
  - io, google.colab.files: **Para lidar com upload/leitura de arquivos no Google Colab.**
  - sklearn.model_selection: **Para dividir os dados (train_test_split) e otimizar parâmetros (GridSearchCV).**
  - sklearn.preprocessing: **Para codificar variáveis ordinais (OrdinalEncoder) e escalar dados (StandardScaler).**
  - sklearn.metrics: **Para calcular métricas de avaliação (MAE, RMSE, R²).**
  - lightgbm: **Para usar o algoritmo LightGBM (o modelo principal).**
  - matplotlib.pyplot, seaborn: **Para gerar gráficos.**

### Warnings: 
- Para suprimir mensagens de aviso não críticas.

### Instalação/Importação Opcional: 
- Usa blocos try-except para:

### Importar unidecode. 
- Se falhar (não instalada), imprime uma mensagem, usa !pip install para instalá-la no ambiente Colab e depois importa. Essencial para remover acentos na limpeza de nomes/valores.

### Fazer o mesmo para shap (interpretação do modelo) e graphviz (visualização de árvore). 
- A instalação do graphviz no Colab requer também um comando de sistema (!apt-get).

### Ignorar Warnings: 
Configura para não exibir certos tipos de avisos (UserWarning do shap, FutureWarning) que podem ser informativos mas poluem a saída principal.
