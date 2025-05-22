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

      rf_base = RandomForestClassifier(random_state=42, n_jobs=-1)
      balanced_acc_scorer = 'balanced_accuracy'
      grid_search = GridSearchCV(estimator=rf_base, param_grid=param_grid,
                                cv=5, n_jobs=-1, verbose=1, scoring=balanced_acc_scorer)

**Configuração do GridSearchCV utilizando:**

- Validação cruzada: 5 folds para avaliação robusta

- Métrica balanceada: balanced_accuracy para lidar com desbalanceamento

- Paralelização: n_jobs=-1 para usar todos os cores disponíveis
      
      grid_search.fit(X_train, y_train, sample_weight=sample_weights_train)
      best_rf_model = grid_search.best_estimator_

Treinamento e seleção do melhor modelo aplicando os pesos de amostra durante o treinamento para reforçar o balanceamento.

# Etapa 5: Calibração de Probabilidades

      calibrated_model = CalibratedClassifierCV(
          base_estimator=best_rf_model,
          method='isotonic',
          cv=5
      )
      calibrated_model.fit(X_train, y_train, sample_weight=sample_weights_train)

**Calibração isotônica das probabilidades melhorando a confiabilidade das estimativas de probabilidade do modelo através de:**

- Método isotônico: Mais flexível que calibração sigmoid

- Validação cruzada: 5 folds para calibração robusta

# Etapa 6: Otimização de Limiar de Classificação

      y_pred_proba_test = calibrated_model.predict_proba(X_test)[:, 1]
      thresholds = [0.3, 0.4, 0.5, 0.6, 0.7]
      results = []

Teste de múltiplos limiares avaliando diferentes pontos de corte para otimizar o desempenho em métricas específicas.
Pesos de amostra: Mantendo o balanceamento durante calibração

      for threshold in thresholds:
          y_pred_custom = (y_pred_proba_test >= threshold).astype(int)
    
    acc = accuracy_score(y_test, y_pred_custom)
    bal_acc = balanced_accuracy_score(y_test, y_pred_custom)
    f1 = f1_score(y_test, y_pred_custom)
    
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred_custom).ravel()

**Avaliação abrangente para cada limiar calculando múltiplas métricas:**

- Acurácia simples e balanceada

- F1-score

- Componentes da matriz de confusão

- Precisão e recall por classe


      best_threshold_idx = max(range(len(results)), key=lambda i: results[i]['balanced_accuracy'])
      best_threshold = results[best_threshold_idx]['threshold']
      y_pred_final = (y_pred_proba_test >= best_threshold).astype(int)

Seleção do limiar ótimo baseado na acurácia balanceada, que é mais apropriada para datasets desbalanceados.

# Etapa 7: Avaliação Final e Relatórios
      print("\nRelatório de Classificação Final (com limiar otimizado):")
      print(classification_report(y_test, y_pred_final, target_names=['Salário Baixo/Médio', 'Salário Alto']))

Relatório detalhado de classificação apresentando precisão, recall, F1-score e suporte para cada classe com o limiar otimizado.

# Etapa 8: Geração de Visualizações Avançadas

**8.1 Matriz de Confusão Otimizada**
      
      cm = confusion_matrix(y_test, y_pred_final)
      plt.figure(figsize=(10, 8))
      sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                  xticklabels=['Salário Baixo/Médio', 'Salário Alto'],
                  yticklabels=['Salário Baixo/Médio', 'Salário Alto'],
                  annot_kws={"size": 14})

Visualização da matriz de confusão com formatação profissional usando heatmap do seaborn, incluindo rótulos descritivos e anotações em tamanho legível.

**8.2 Curva ROC com Limiar Otimizado**

      fpr, tpr, _ = roc_curve(y_test, y_pred_proba_test)
      roc_auc = auc(fpr, tpr)
      plt.plot(fpr, tpr, color='darkorange', lw=3, label=f'Curva ROC (AUC = {roc_auc:.2f})')
      plt.axvline(x=fpr[np.argmin(np.abs(tpr - best_threshold))], color='green', linestyle='--', 
                  label=f'Limiar Ótimo = {best_threshold}')

**Curva ROC aprimorada incluindo:**

- Área sob a curva (AUC) como métrica de desempenho

- Linha vertical indicando o limiar otimizado

- Formatação profissional com cores contrastantes e legendas

**8.3 Análise de Importância das Features**

      importances = best_rf_model.feature_importances_
      feature_names = X.columns
      indices = np.argsort(importances)[::-1]
      n_features_to_show = min(20, len(indices))
      top_indices = indices[:n_features_to_show]
Ranking de importância das features limitado às 20 mais relevantes para melhor visualização e interpretabilidade.

      # Agrupar features por prefixo para melhor organização
      prefixes = {}
      for i in indices:
          feature = feature_names[i]
          prefix = feature.split('_')[0] if '_' in feature else feature
          if prefix not in prefixes:
              prefixes[prefix] = []
          prefixes[prefix].append((i, importances[i]))
Agrupamento inteligente por categorias organizando features por prefixos (formação, localização, setor) para análise estruturada da importância por domínio.

**8.4 Agrupamento por Categorias**

      prefixes = {}
      for i in indices:
          feature = feature_names[i]
          prefix = feature.split('_')[0] if '_' in feature else feature
          if prefix not in prefixes:
              prefixes[prefix] = []
          prefixes[prefix].append((i, importances[i]))

Agrupamento inteligente por categorias organizando features por prefixos (formação, localização, setor) para análise estruturada da importância por domínio.

**8.5 Distribuição das Probabilidades Preditas**

      plt.figure(figsize=(12, 8))
      sns.histplot(y_pred_proba_test, bins=50, kde=True)
      plt.axvline(x=best_threshold, color='red', linestyle='--', linewidth=2,
                 label=f'Limiar Ótimo = {best_threshold}')

Análise da distribuição das probabilidades geradas pelo modelo calibrado com marcação do limiar ótimo, permitindo visualizar quantas amostras ficam de cada lado do ponto de corte.

**8.6 Visualização de Árvores de Decisão**
      
      plt.figure(figsize=(24, 18))
      plot_tree(best_rf_model.estimators_[0], 
                feature_names=X.columns, 
                class_names=['Salário Baixo/Médio', 'Salário Alto'],
                filled=True, 
                rounded=True, 
                fontsize=12,
                max_depth=4)

- Visualização detalhada de árvore individual do Random Forest com:

- Tamanho expandido: 24x18 polegadas para máxima legibilidade

- Profundidade controlada: max_depth=4 para mostrar detalhes sem complexidade excessiva

- Formatação aprimorada: Nós preenchidos, bordas arredondadas e fonte de tamanho 12

**8.7 Análise de Interação entre Formação e Experiência**

      pivot_table = pd.crosstab(
          index=df_limpo['formacao_academica_encoded'], 
          columns=df_limpo['experiencia_profissional_encoded'],
          values=df_limpo['salario_alto'],
          aggfunc=np.mean
      )

Tabela cruzada avançada utilizando pd.crosstab para calcular a probabilidade média de salário alto para cada combinação de formação acadêmica e experiência profissional.

      formacao_labels = {v: k for k, v in nivel_ensino_map.items()}
      experiencia_labels = {v: k for k, v in experiencia_map.items()}
      
      pivot_table.index = [formacao_labels.get(i, i) for i in pivot_table.index]
      pivot_table.columns = [experiencia_labels.get(i, i) for i in pivot_table.columns]

Mapeamento reverso dos rótulos convertendo os valores numéricos codificados de volta para suas descrições originais, tornando o heatmap mais interpretável.

**8.8 Visualização das Top 3 Features**

      top3_indices = indices[:3]
      top3_features = [feature_names[i] for i in top3_indices]
      top3_importances = importances[top3_indices]
      
      plt.figure(figsize=(10, 6))
      bars = plt.barh(range(3), top3_importances, align='center', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

Gráfico especializado para as 3 features mais importantes com cores diferenciadas e valores anotados nas barras para facilitar a interpretação.

**8.9 Gráfico de Dispersão das Features Principais**
      
      if len(indices) >= 2:
          top2_indices = indices[:2]
          feature1 = feature_names[top2_indices[0]]
          feature2 = feature_names[top2_indices[1]]
          
          scatter = plt.scatter(X_test[feature1], X_test[feature2], 
                               c=y_pred_proba_test, cmap='coolwarm', 
                               alpha=0.7, s=100, edgecolors='k')

Visualização da relação entre as duas features mais importantes colorido pelas probabilidades preditas, revelando padrões espaciais na classificação e permitindo identificar regiões de alta e baixa probabilidade de salário alto.

**8.10 Finalização e Salvamento**
print(f"\nTodos os gráficos foram salvos no diretório: {output_dir}")


