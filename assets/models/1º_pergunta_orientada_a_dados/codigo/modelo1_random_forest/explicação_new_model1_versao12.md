# Explicação Detalhada do Código 

Explicação Detalhada do Código de Machine Learning para Predição Salarial
---

# Etapa 0: Configuração Inicial
   
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_curve, auc, balanced_accuracy_score, f1_score, precision_recall_curve
from sklearn.calibration import CalibratedClassifierCV
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import seaborn as sns
import os



**Importações das bibliotecas essenciais:**

- pandas e numpy: Manipulação e processamento de dados

- sklearn: Ferramentas de machine learning, incluindo divisão de dados, algoritmos, métricas e calibração

- matplotlib e seaborn: Visualização de dados e gráficos

- os: Operações do sistema operacional para criação de diretórios

# Criar diretório para salvar os gráficos, se não existir

    output_dir = '/kaggle/working/'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

**Configuração do diretório de saída para salvar os gráficos gerados. O código verifica se o diretório existe e o cria caso necessário.**


# Configurar o estilo dos gráficos para melhor visualização
    
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.labelsize'] = 14

**Configuração global dos gráficos estabelecendo um estilo consistente com:**

- Estilo seaborn: Grade branca para melhor visualização

- Tamanho padrão: 12x8 polegadas

- Fontes: Tamanhos diferenciados para títulos (16), labels (14) e texto geral (12)

# Etapa 1: Carregamento e Pré-processamento dos Dados

    try:
        df = pd.read_csv('/kaggle/input/dataset-clean/dados_limpos.csv')
        print("Dataset carregado do caminho Kaggle.")
    except FileNotFoundError:
        try:
            df = pd.read_csv('dados_limpos.csv') 
            print("Dataset carregado localmente.")
        except FileNotFoundError:
            print("Arquivo 'dados_limpos.csv' não encontrado no caminho Kaggle nem localmente.")
            print("Por favor, certifique-se de que o arquivo está no diretório correto ou ajuste o caminho.")
            exit()

**Sistema de carregamento robusto que tenta múltiplos caminhos:**

- Primeiro: Caminho do Kaggle para execução na plataforma

- Segundo: Caminho local para desenvolvimento

- Tratamento de erro: Mensagem informativa e encerramento seguro se o arquivo não for encontrado

        colunas_features = [
            'Nível de ensino alcançado', 
            'Tempo de experiência na área de dados',
            'Área de formação acadêmica',
            'Nível de senioridade',
            'UF onde mora',
            'Setor de atuação da empresa'
        ]
        coluna_target = 'Faixa salarial mensal'
        colunas_necessarias = colunas_features + [coluna_target]


**Definição das variáveis do modelo expandindo significativamente o conjunto de features em relação a versões anteriores:**

- Features ordinais: Nível de ensino, experiência e senioridade

- Features categóricas: Área de formação, localização geográfica e setor empresarial

- Target: Faixa salarial mensal para classificação binária

        df_limpo = df[colunas_necessarias].copy()
        df_limpo.dropna(subset=colunas_necessarias, inplace=True)

**Limpeza inicial dos dados removendo registros com valores ausentes nas colunas cruciais para garantir qualidade dos dados de entrada.**

# Etapa 2: Engenharia de Features e Criação da Variável Alvo

    nivel_ensino_map = {
        'Estudante de Graduação': 0,
        'Graduação/Bacharelado': 1,
        'Pós-graduação': 2,
        'Mestrado': 3,
        'Doutorado ou Phd': 4
    }
    df_limpo['formacao_academica_encoded'] = df_limpo['Nível de ensino alcançado'].map(nivel_ensino_map)

Mapeamento ordinal para nível educacional criando uma escala numérica que preserva a hierarquia natural dos níveis de formação acadêmica, onde valores maiores representam maior qualificação.
    
    experiencia_map = {
        'Menos de 1 ano': 0,
        'de 1 a 2 anos': 1,
        'de 3 a 4 anos': 2,
        'de 4 a 6 anos': 3,
        'de 5 a 6 anos': 3, 
        'de 7 a 10 anos': 4,
        'Mais de 10 anos': 5
    }
    df_limpo['experiencia_profissional_encoded'] = df_limpo['Tempo de experiência na área de dados'].map(experiencia_map)

Codificação ordinal da experiência profissional com tratamento especial para sobreposições nas faixas (como "de 4 a 6 anos" e "de 5 a 6 anos" recebendo o mesmo valor 3).

    senioridade_map = {
        'Júnior': 0,
        'Pleno': 1,
        'Sênior': 2
    }
    df_limpo['senioridade_encoded'] = df_limpo['Nível de senioridade'].map(senioridade_map)

Mapeamento do nível de senioridade seguindo a progressão natural da carreira em tecnologia.

    salario_map_ordinal = {
        'Menos de R$ 1.000/mês': 0,
        'de R$ 1.001/mês a R$ 2.000/mês': 1,
        'de R$ 2.001/mês a R$ 3.000/mês': 2,
        'de R$ 3.001/mês a R$ 4.000/mês': 3,
        'de R$ 4.001/mês a R$ 6.000/mês': 4,
        'de R$ 6.001/mês a R$ 8.000/mês': 5,
        'de R$ 8.001/mês a R$ 12.000/mês': 6,
        'de R$ 12.001/mês a R$ 16.000/mês': 7,
        'de R$ 16.001/mês a R$ 20.000/mês': 8,
        'de R$ 20.001/mês a R$ 25.000/mês': 9,
        'de R$ 25.001/mês a R$ 30.000/mês': 10,
        'de R$ 30.001/mês a R$ 40.000/mês': 11,
        'Acima de R$ 40.001/mês': 12
    }
    df_limpo['faixa_salarial_encoded'] = df_limpo['Faixa salarial mensal'].map(salario_map_ordinal)

Codificação ordinal detalhada das faixas salariais criando uma escala numérica de 0 a 12 que preserva a ordem crescente dos valores monetários.

    df_limpo['salario_alto'] = df_limpo['faixa_salarial_encoded'].apply(lambda x: 1 if x > 5 else 0)

**Criação da variável alvo binária definindo o ponto de corte em R$ 8.000 (valor 5 na escala ordinal):**

- 0: Salários até R$ 8.000 (baixo/médio)

- 1: Salários acima de R$ 8.000 (alto)

        df_encoded = pd.get_dummies(df_limpo, columns=['Área de formação acadêmica', 'UF onde mora', 'Setor de atuação da empresa'])

Codificação one-hot para variáveis categóricas transformando variáveis categóricas nominais em múltiplas variáveis binárias, permitindo que o modelo capture diferentes padrões para cada categoria.

    X_columns = ['formacao_academica_encoded', 'experiencia_profissional_encoded', 'senioridade_encoded'] + \
                [col for col in df_encoded.columns if col.startswith(('Área de formação acadêmica_', 
                                                                     'UF onde mora_', 
                                                                     'Setor de atuação da empresa_'))]
    X = df_encoded[X_columns]
    y = df_encoded['salario_alto']

Seleção final das features combinando variáveis ordinais codificadas com variáveis dummy criadas pelo one-hot encoding.

# Etapa 3: Validação e Balanceamento dos Dados
    
    if X.shape[0] < 10 or len(y.unique()) < 2:
        print("Não há dados suficientes ou classes suficientes após o pré-processamento para treinar o modelo.")
        print(f"Tamanho de X: {X.shape}, Classes em y: {y.unique()}")
        exit()

Verificação de viabilidade do modelo garantindo que existem dados suficientes e ambas as classes estão representadas.

    class_counts = y.value_counts()
    print("\nDistribuição das classes:")
    print(f"Salário Baixo/Médio (0): {class_counts[0]} ({class_counts[0]/len(y)*100:.2f}%)")
    print(f"Salário Alto (1): {class_counts[1]} ({class_counts[1]/len(y)*100:.2f}%)")

Análise do balanceamento das classes exibindo a distribuição para identificar possível desbalanceamento que pode afetar o desempenho do modelo.


    class_weights = {0: 1.0, 1: class_counts[0] / class_counts[1]}
    sample_weights = np.array([class_weights[cls] for cls in y])

Cálculo de pesos para balanceamento criando pesos inversamente proporcionais à frequência das classes para compensar desbalanceamento sem usar técnicas de reamostragem como SMOTE.

    X_train, X_test, y_train, y_test, sample_weights_train, _ = train_test_split(
        X, y, sample_weights, test_size=0.3, random_state=42, stratify=y
    )

Divisão estratificada dos dados mantendo a proporção das classes nos conjuntos de treino e teste, incluindo os pesos calculados.

# Etapa 4: Desenvolvimento do Modelo com Otimização de Hiperparâmetros

    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20],
        'min_samples_split': [5, 10, 15],
        'min_samples_leaf': [3, 5, 7],
        'class_weight': ['balanced', 'balanced_subsample']
    }

**Grade de hiperparâmetros para otimização definindo múltiplas combinações para:**

- n_estimators: Número de árvores na floresta

- max_depth: Profundidade máxima das árvores (None permite crescimento completo)

- min_samples_split: Mínimo de amostras para dividir um nó

- min_samples_leaf: Mínimo de amostras em folhas

- class_weight: Estratégias de balanceamento automático
