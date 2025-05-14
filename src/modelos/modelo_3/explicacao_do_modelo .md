## Explicação Detalhada do Código (Principais Etapas no `train_classification_model_salary_range_v7_final`)

### Pergunta orientada a dados : **Como fatores como formalidade no emprego e características demográficas (gênero e raça) interagem com a proficiência técnica para influenciar as disparidades salariais entre profissionais de dados no Brasil?**
  * O fluxo de execução do código principal pode ser resumido nas seguintes etapas:

1.  **Carregamento e Preparação Inicial dos Dados**:
    * Leitura do arquivo Excel (`Main_database (2).xlsx`).
    * Limpeza dos nomes das colunas para remover caracteres especiais e espaços (função `clean_col_name`).
    * Mapeamento heurístico de colunas importantes (faixa salarial original, experiência, senioridade, etc.) para nomes padronizados internos (armazenados em `col_mapping`).
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, f1_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import RFECV
import lightgbm as lgb
import optuna
import warnings
import re
import pickle
import time
import traceback

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=optuna.exceptions.ExperimentalWarning)

# Certifique-se de que a pasta para salvar visualizações existe
os.makedirs('visualizacoes_classificacao_salario_v7_rfecv', exist_ok=True)
```

2.  **Engenharia da Variável Alvo (`target_col_agrupada_name`)**:
    * A coluna da faixa salarial original (ex: `P2_h`) é processada para extrair um valor numérico (`salary_numeric_lower_bound`) usando `extract_salary_lower_bound`.
    * **Divisão em Duas Categorias**: Um **ponto de corte fixo** (`point_of_cut_fixed`, que você estava ajustando, por exemplo, para R$7.500,00 na última execução) é usado para dividir `salary_numeric_lower_bound` em "Salário Baixo" e "Salário Alto" usando `pd.cut`. Esta etapa inclui lógica para lidar com casos onde o ponto de corte é extremo (menor/igual ao mínimo ou maior/igual ao máximo) e um fallback para `pd.qcut` (divisão pela mediana) se o `pd.cut` falhar.
    * A distribuição de `salary_numeric_lower_bound` é plotada para auxiliar na escolha/ajuste do `point_of_cut_fixed`.
    * Amostras com valor nulo na nova variável alvo são removidas.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)

        # ... (Após mapeamento de colunas e limpeza da coluna de experiência) ...

        original_salary_col_name = col_mapping["target_original_salary_range"]
        df_main_processed = df_main.dropna(subset=[original_salary_col_name]).copy()
        if df_main_processed.empty: print(f"Erro: DataFrame vazio após NaNs na faixa salarial original."); return None

        # Extrai o limite inferior numérico da faixa salarial
        df_main_processed['salary_numeric_lower_bound'] = df_main_processed[original_salary_col_name].apply(extract_salary_lower_bound)
        df_main_processed.dropna(subset=['salary_numeric_lower_bound'], inplace=True)

        if df_main_processed.empty:
            print(f"Erro: DataFrame vazio após remover NaNs de 'salary_numeric_lower_bound'."); return None

        # --- CRIAÇÃO DA VARIÁVEL ALVO COM 2 CATEGORIAS E PONTO DE CORTE FIXO ---
        salary_group_labels = ["Salário Baixo", "Salário Alto"]
        target_col_agrupada_name = col_mapping["target"] # Definido anteriormente no mapeamento

        if df_main_processed.shape[0] < 2:
            print(f"Erro: Dados insuficientes ({df_main_processed.shape[0]}) para criar faixas."); return None

        min_salary = df_main_processed['salary_numeric_lower_bound'].min()
        max_salary = df_main_processed['salary_numeric_lower_bound'].max()

        if min_salary == max_salary:
            print(f"Aviso: Todos os valores de 'salary_numeric_lower_bound' são iguais ({min_salary}). Apenas uma categoria ('{salary_group_labels[0]}') será criada.")
            df_main_processed[target_col_agrupada_name] = salary_group_labels[0]
        else:
            # AJUSTE ESTE VALOR PARA CONTROLAR A DISTRIBUIÇÃO DAS CLASSES
            # Se "Salário Baixo" tiver muitas amostras, DIMINUA este valor.
            # Se "Salário Baixo" tiver poucas amostras, AUMENTE este valor.
            # Exemplos baseados no seu histograma: 7500, 8000, 9000.
            point_of_cut_fixed = 7500.0  # <-- PONTO DE CORTE AJUSTÁVEL

            print(f"Info: Usando ponto de corte fixo para salários: {point_of_cut_fixed:.2f}")
            print(f"       Salários <= {point_of_cut_fixed:.2f} serão '{salary_group_labels[0]}' (Salário Baixo)")
            print(f"       Salários >  {point_of_cut_fixed:.2f} serão '{salary_group_labels[1]}' (Salário Alto)")

            final_bins = []
            final_labels = []

            if point_of_cut_fixed <= min_salary:
                print(f"Aviso: Ponto de corte fixo ({point_of_cut_fixed:.2f}) é <= ao mínimo ({min_salary:.2f}). Todos os dados cairão em '{salary_group_labels[1]}'.")
                final_bins = [min_salary, max_salary]
                final_labels = [salary_group_labels[1]]
            elif point_of_cut_fixed >= max_salary:
                print(f"Aviso: Ponto de corte fixo ({point_of_cut_fixed:.2f}) é >= ao máximo ({max_salary:.2f}). Todos os dados cairão em '{salary_group_labels[0]}'.")
                final_bins = [min_salary, max_salary]
                final_labels = [salary_group_labels[0]]
            else:
                final_bins = [min_salary, point_of_cut_fixed, max_salary]
                final_labels = salary_group_labels

            unique_sorted_bins = sorted(list(set(final_bins)))

            if len(unique_sorted_bins) < 2:
                print(f"Erro crítico: Não foi possível definir pelo menos 2 bins únicos ({unique_sorted_bins}) com o ponto de corte fixo."); return None

            # Ajuste para o caso de unique_sorted_bins ter apenas 2 elementos e final_labels ter 2 labels
            # Isso pode acontecer se o ponto de corte for igual ao min ou max, ou muito próximo.
            if len(unique_sorted_bins) == 2 and len(final_labels) == 2:
                print(f"Aviso: Ponto de corte fixo resultou em apenas 2 bins efetivos ({unique_sorted_bins}). Será criada apenas 1 categoria.")
                # Decide qual label usar baseado na posição do ponto de corte
                if point_of_cut_fixed <= min_salary + 1e-9: # Se o corte é no mínimo ou abaixo, todos são "Alto"
                    final_labels = [salary_group_labels[1]]
                elif point_of_cut_fixed >= max_salary - 1e-9: # Se o corte é no máximo ou acima, todos são "Baixo"
                    final_labels = [salary_group_labels[0]]
                else: # Se o corte está entre min e max mas resultou em 1 categoria (devido a 'duplicates=drop' ou bins muito próximos)
                      # Tenta inferir a categoria predominante ou a que faz mais sentido.
                      # Aqui, uma heurística simples: se o ponto de corte está mais perto do mínimo,
                      # significa que a maior parte dos dados está acima, então seriam "Salário Alto".
                      # Se está mais perto do máximo, a maioria é "Salário Baixo".
                      # Isso é uma simplificação e pode precisar de ajuste mais fino dependendo do caso de uso.
                    if (point_of_cut_fixed - min_salary) < (max_salary - point_of_cut_fixed):
                        # Ponto de corte mais próximo do mínimo -> maioria é Alto
                        final_labels = [salary_group_labels[1]]
                    else:
                        # Ponto de corte mais próximo do máximo -> maioria é Baixo
                        final_labels = [salary_group_labels[0]]


            bins_to_use = unique_sorted_bins
            labels_to_use = final_labels

            try:
                df_main_processed[target_col_agrupada_name] = pd.cut(
                    df_main_processed['salary_numeric_lower_bound'],
                    bins=bins_to_use,
                    labels=labels_to_use,
                    include_lowest=True, # Garante que o valor mínimo seja incluído no primeiro bin
                    duplicates='drop'    # Remove bins duplicados se existirem
                )
            except Exception as e:
                print(f"Erro durante pd.cut com ponto de corte fixo: {e}")
                print(f"  Bins usados: {bins_to_use}, Labels usados: {labels_to_use}")
                print("  Tentando fallback para divisão pela mediana (pd.qcut)...")
                try:
                    df_main_processed[target_col_agrupada_name] = pd.qcut(
                        df_main_processed['salary_numeric_lower_bound'],
                        q=2, labels=salary_group_labels, duplicates='drop'
                    )
                    num_qcut_cats = len(df_main_processed[target_col_agrupada_name].cat.categories)
                    if num_qcut_cats < 2: # Se qcut também falhar em criar 2 categorias
                        print("Fallback com qcut também resultou em menos de 2 categorias. Agrupando em uma única categoria.")
                        df_main_processed[target_col_agrupada_name] = salary_group_labels[0] # Ou a categoria mais apropriada
                except Exception as e_qcut_fallback:
                     print(f"Erro no fallback com pd.qcut: {e_qcut_fallback}. Não foi possível criar a variável alvo."); return None

        print(f"Nova coluna alvo '{target_col_agrupada_name}' criada. Contagens no DataFrame processado completo:\\n{df_main_processed[target_col_agrupada_name].value_counts(dropna=False).sort_index()}")

        print("\nDiagnóstico da distribuição de 'salary_numeric_lower_bound':")
        print(df_main_processed['salary_numeric_lower_bound'].describe())
        plt.figure(figsize=(10,4))
        sns.histplot(df_main_processed['salary_numeric_lower_bound'], kde=True, bins=50)
        plt.title("Distribuição de 'salary_numeric_lower_bound'")
        plt.savefig('visualizacoes_classificacao_salario_v7_rfecv/distribuicao_salario_numerico.png')
        # plt.show() # Removido ou comentado para execução em lote/sem interface gráfica
        plt.close()

        df_main_processed.dropna(subset=[target_col_agrupada_name], inplace=True)
        if df_main_processed.empty:
            print("Erro: DataFrame vazio após remover NaNs na coluna alvo agrupada. Verifique a criação das categorias."); return None
        print(f"Linhas após remover NaN na coluna alvo AGRUPADA: {df_main_processed.shape[0]}")
        # --- FIM DAS MODIFICAÇÕES NA VARIÁVEL ALVO ---
```
3.  **Preparação das Features (`X_initial`) e Codificação do Alvo (`y_full`)**:
    * As features relevantes (idade, gênero, UF, ensino, cargo, senioridade, experiência) são selecionadas.
    * A coluna 'UF' é transformada na feature 'Regiao\_Mapeada'.
    * A variável alvo (`target_col_agrupada_name`) é codificada numericamente (0 e 1) usando `LabelEncoder`, e é determinado se o problema é de classificação binária.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a engenharia da variável alvo e remoção de NaNs na coluna alvo agrupada) ...

        # Seleciona as colunas de features iniciais com base no mapeamento
        # required_cols_internal_for_features foi definido anteriormente como:
        # ["faixa_etaria", "genero", "nivel_ensino", "tempo_experiencia_P2i", 
        #  "nivel_senioridade_P2g", "uf_mora_P1i1", "cargo_atual_P2f"]
        feature_cols_to_use_initial = [
            col_mapping[col_internal] for col_internal in required_cols_internal_for_features 
            if col_internal in col_mapping and col_mapping[col_internal] in df_main_processed.columns
        ]
        X_initial = df_main_processed[feature_cols_to_use_initial].copy()

        # Mapeia UF para Região e remove a coluna original de UF
        uf_col_original_name_mapped = col_mapping.get("uf_mora_P1i1")
        if uf_col_original_name_mapped and uf_col_original_name_mapped in X_initial.columns:
            X_initial['Regiao_Mapeada'] = map_uf_to_region(X_initial[uf_col_original_name_mapped])
            X_initial.drop(columns=[uf_col_original_name_mapped], inplace=True)

        # Codifica a variável alvo
        # 'le' e 'is_binary_classification' são declaradas como globais para serem acessadas
        # pela função objective_optuna_cv que é definida no escopo global do script,
        # mas chamada dentro desta função principal.
        global le, is_binary_classification 
        le = LabelEncoder()
        y_full = pd.Series(le.fit_transform(df_main_processed[target_col_agrupada_name]), index=df_main_processed.index)
        
        print(f"Alvo AGRUPADA '{target_col_agrupada_name}' codificada. Classes: {list(le.classes_)} -> {list(le.transform(le.classes_))}")

        if len(le.classes_) < 2:
            print(f"ERRO CRÍTICO: A variável alvo final tem menos de 2 classes ({len(le.classes_)}: {list(le.classes_)}). Não é possível treinar o modelo de classificação."); return None
        
        is_binary_classification = len(le.classes_) == 2

        if is_binary_classification:
            print("Classificação Binária Detectada.")
        else:
            print(f"Classificação Multiclasse Detectada ({len(le.classes_)} classes).")

        initial_feature_columns_after_region = X_initial.columns.tolist()
        print(f"Features para processamento inicial (antes RFECV): {initial_feature_columns_after_region}")
```
4.  **Pré-processamento das Features**:
    * **Valores Ausentes**:
        * Features numéricas (como tempo de experiência): imputados com a mediana.
        * Features categóricas: imputados com a string "Missing\_Val\_Cat".
    * **Outliers**: Para features numéricas, outliers são identificados usando o critério de 1.5\*IQR e as linhas contendo outliers são removidas.
    * **Codificação de Categóricas**: Features categóricas são convertidas para o tipo `category` do pandas.
    * **Escalonamento**: Features numéricas são padronizadas usando `StandardScaler`.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a preparação de X_initial e y_full) ...

        # Identifica features numéricas e categóricas em X_initial
        # initial_feature_columns_after_region já contém os nomes das colunas em X_initial
        numerical_features_initial = X_initial.select_dtypes(include=np.number).columns.tolist()
        categorical_features_initial = X_initial.select_dtypes(exclude=np.number).columns.tolist()

        print(f"Features numéricas identificadas: {numerical_features_initial}")
        print(f"Features categóricas identificadas: {categorical_features_initial}")

        # Tratamento de Ausentes (Features Numéricas)
        for col in numerical_features_initial:
            if X_initial[col].isnull().sum() > 0:
                print(f"Imputando NaNs na feature numérica '{col}' com a mediana.")
                X_initial.loc[:, col] = X_initial[col].fillna(X_initial[col].median())

        # Tratamento de Outliers (Features Numéricas)
        outliers_indices = pd.Series(False, index=X_initial.index)
        if numerical_features_initial:
            print("Processando outliers para features numéricas...")
            for col in numerical_features_initial:
                Q1 = X_initial[col].quantile(0.25); Q3 = X_initial[col].quantile(0.75); IQR = Q3 - Q1
                lim_inf = Q1 - 1.5 * IQR; lim_sup = Q3 + 1.5 * IQR
                col_outliers = (X_initial[col] < lim_inf) | (X_initial[col] > lim_sup)
                if col_outliers.sum() > 0: print(f"  Feature '{col}': {col_outliers.sum()} outliers detectados.")
                outliers_indices = outliers_indices | col_outliers # Acumula os índices de outliers de todas as colunas numéricas
            
            if outliers_indices.sum() > 0:
                print(f"Total de amostras com outliers: {outliers_indices.sum()}")
                # Remove as linhas (amostras) que contêm outliers
                X_initial = X_initial[~outliers_indices]; 
                y_full = y_full[~outliers_indices] # Mantém y_full sincronizado com X_initial
                print(f"Shape de X_initial e y_full após remover outliers: {X_initial.shape}, {y_full.shape}")
                if X_initial.empty: print("ERRO: Todos os dados removidos como outliers."); return None
            else: print("Nenhum outlier encontrado em features numéricas.")
        else: print("Nenhuma feature numérica para checar outliers.")

        # Tratamento de Ausentes (Features Categóricas) e conversão para tipo 'category'
        for col_name in categorical_features_initial:
            if col_name not in X_initial.columns: continue # Caso a coluna tenha sido removida (pouco provável aqui)
            
            # Converte para string para facilitar a busca por valores ausentes textuais
            processed_series = X_initial[col_name].astype(str) 
            missing_vals = ['nan', 'none', '<na>', '', 'missing', 'missing_category_value', 'missing_val_cat', 'null']
            temp_lower_stripped = processed_series.str.lower().str.strip()
            
            # Identifica tanto NaNs originais quanto strings que representam ausência
            is_missing = temp_lower_stripped.isin(missing_vals) | X_initial[col_name].isnull() 
            
            if is_missing.any():
                # Usa .loc para evitar SettingWithCopyWarning e garantir a modificação no DataFrame original
                X_initial.loc[is_missing, col_name] = "Missing_Val_Cat" 
            
            # Converte a coluna para o tipo 'category' do pandas
            X_initial[col_name] = X_initial[col_name].astype("category")

        # Escalonamento (Features Numéricas)
        # O scaler é inicializado como scaler_rfecv, mas ele é ajustado aqui nos dados X_initial (que ainda não foram divididos)
        # e será usado posteriormente.
        scaler_rfecv = StandardScaler()
        # Re-identifica as features numéricas caso alguma tenha sido removida ou alterada
        numerical_features_present_after_outliers = [col for col in numerical_features_initial if col in X_initial.columns]
        
        if numerical_features_present_after_outliers:
             # Usa .loc para garantir a atribuição correta e evitar warnings
             X_initial.loc[:, numerical_features_present_after_outliers] = scaler_rfecv.fit_transform(X_initial[numerical_features_present_after_outliers])
             print(f"Features numéricas ({numerical_features_present_after_outliers}) em X_initial escalonadas.")
        else:
            print("Nenhuma feature numérica presente em X_initial para escalonar.")

        # Verifica novamente se y_full tem classes suficientes após a remoção de outliers
        if y_full.nunique() < 2:
            print(f"ERRO CRÍTICO: A variável alvo final tem menos de 2 classes únicas ({y_full.nunique()}: {y_full.unique()}) após processamento. Não é possível treinar o modelo."); return None
```
5.  **Divisão Treino-Teste Principal**:
    * Os dados processados (`X_initial`, `y_full`) são divididos em 75% para treino/otimização (`X_train_optuna`, `y_train_optuna`) e 25% para teste final (`X_test`, `y_test`), de forma estratificada.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após o pré-processamento completo de X_initial e y_full) ...

        # Verifica se y_full ainda tem classes suficientes para estratificação após todos os processamentos anteriores
        if y_full.nunique() < 2:
            print(f"ERRO CRÍTICO: A variável alvo final tem menos de 2 classes únicas ({y_full.nunique()}: {y_full.unique()}) "
                  "antes da divisão treino-teste. Não é possível treinar o modelo.")
            return None

        # Divisão dos dados em conjuntos de treino para Optuna/RFECV e conjunto de teste
        # test_size=0.25 significa 75% para treino e 25% para teste.
        # random_state=42 garante a reprodutibilidade da divisão.
        # stratify=y_full garante que a proporção das classes da variável alvo seja mantida
        # tanto no conjunto de treino quanto no de teste.
        X_train_optuna, X_test, y_train_optuna, y_test = train_test_split(
            X_initial, y_full, 
            test_size=0.25, 
            random_state=42, 
            stratify=y_full
        )
        
        print(f"Dados divididos em treino ({X_train_optuna.shape[0]}) e teste ({X_test.shape[0]})")
```
6.  **Seleção de Features com RFECV**:
    * As features categóricas no conjunto de treino do RFECV são convertidas para códigos numéricos.
    * `RFECV` é aplicado usando `lgb.LGBMClassifier` e `StratifiedKFold` (3 folds) para encontrar o subconjunto ótimo de features baseado na acurácia.
    * `X_train_optuna` e `X_test` são atualizados para conter apenas as features selecionadas.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a divisão treino-teste principal) ...

        print("\nIniciando Seleção de Features com RFECV...")
        start_time_rfecv = time.time()
        
        # Cria uma cópia de X_train_optuna para o RFECV para não modificar o original ainda
        X_train_optuna_for_rfecv = X_train_optuna.copy()
        
        # Identifica colunas categóricas que precisam ser codificadas para o RFECV
        categorical_cols_for_rfecv_encoding = X_train_optuna_for_rfecv.select_dtypes(include='category').columns
        print(f"Colunas categóricas para codificação numérica no RFECV: {list(categorical_cols_for_rfecv_encoding)}")
        
        # Codifica as features categóricas para o RFECV usando .cat.codes
        # Isso transforma as categorias em inteiros (0, 1, 2, ...)
        for col in categorical_cols_for_rfecv_encoding:
            X_train_optuna_for_rfecv[col] = X_train_optuna_for_rfecv[col].cat.codes

        # Define o estimador para o RFECV
        estimator_rfecv = lgb.LGBMClassifier(random_state=42, n_jobs=-1, verbose=-1)
        
        # Define a estratégia de validação cruzada para o RFECV
        # rfecv_folds é um parâmetro da função, por padrão 3
        cv_rfecv = StratifiedKFold(n_splits=rfecv_folds, shuffle=True, random_state=42)
        
        # Inicializa o RFECV
        # step=rfecv_step (padrão 1) indica quantas features remover a cada iteração.
        # scoring=rfecv_scoring (padrão 'accuracy') é a métrica para avaliar o subconjunto de features.
        # min_features_to_select=1 garante que pelo menos uma feature seja selecionada.
        # verbose=1 mostra o progresso.
        rfecv_selector = RFECV(
            estimator=estimator_rfecv, 
            step=rfecv_step, 
            cv=cv_rfecv,
            scoring=rfecv_scoring, 
            min_features_to_select=1, 
            n_jobs=-1, # Usa todos os processadores disponíveis
            verbose=1
        )

        # Ajusta o RFECV aos dados de treino (com features categóricas codificadas)
        rfecv_selector.fit(X_train_optuna_for_rfecv, y_train_optuna)

        end_time_rfecv = time.time()
        print(f"RFECV concluído em {(end_time_rfecv - start_time_rfecv):.2f} segundos.")
        print(f"Número ótimo de features selecionadas: {rfecv_selector.n_features_}")

        # Obtém os nomes das features selecionadas pelo RFECV
        # rfecv_selector.support_ é uma máscara booleana das features selecionadas
        selected_features_names = X_train_optuna.columns[rfecv_selector.support_].tolist()
        print(f"Features selecionadas: {selected_features_names}")

        if not selected_features_names:
            print("ERRO CRÍTICO: Nenhuma feature selecionada pelo RFECV."); return None

        # Atualiza X_train_optuna e X_test para conter apenas as features selecionadas
        # Mantém os dtypes originais de X_train_optuna (com 'category' para categóricas)
        X_train_optuna_selected = X_train_optuna[selected_features_names].copy()
        X_test_selected = X_test[selected_features_names].copy() # Aplica a mesma seleção ao conjunto de teste

        print(f"Features finais (selecionadas) para modelagem: {X_train_optuna_selected.columns.tolist()}")
        print(f"Dtypes de X_train_optuna_selected:\\n{X_train_optuna_selected.dtypes}")
```
7.  **Otimização de Hiperparâmetros com Optuna**:
    * A função `objective_optuna_cv` é definida para avaliar cada conjunto de hiperparâmetros sugeridos pelo Optuna.
    * Esta função utiliza `StratifiedKFold` (padrão de 5 folds, se possível) para treinar e validar o `lgb.LGBMClassifier`.
    * O Optuna executa `n_optuna_trials` (padrão 100) para encontrar os hiperparâmetros que maximizam a acurácia média da validação cruzada.
    * Os parâmetros `objective` e `metric` do LightGBM são ajustados para `'binary'` e `'binary_logloss'` respectivamente, pois a classificação é binária.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a seleção de features com RFECV e criação de X_train_optuna_selected, X_test_selected) ...

        # Determina o número de folds para a validação cruzada interna do Optuna
        # Limita o número de folds pela contagem da classe minoritária em y_train_optuna
        min_class_count_cv = y_train_optuna.value_counts().min()
        n_cv_folds_optuna = min(5, min_class_count_cv) if min_class_count_cv >= 2 else 1
        
        if n_cv_folds_optuna < 2 and X_train_optuna_selected.shape[0] > 10:
             print(f"Aviso: Classe minoritária ({min_class_count_cv}) impede CV com mais de 1 fold. Optuna rodará sem CV interno robusto.")
             n_cv_folds_optuna = 1 # Garante que seja pelo menos 1 para o lambda
        elif X_train_optuna_selected.shape[0] <=10: # Muito poucos dados para treinar
             print("ERRO CRÍTICO: Dados de treino insuficientes após seleções/processamento."); return None
        if n_cv_folds_optuna == 0: n_cv_folds_optuna = 1 # Prevenção caso min_class_count_cv seja 0 ou 1

        # A função objective_optuna_cv foi definida anteriormente no script.
        # Ela usa as variáveis globais 'is_binary_classification' e 'le' que foram
        # definidas após a codificação da variável alvo y_full.

        study_name = f'LGBM_Salary_Clf_Optuna_CV_v7_final_rfecv_trials{n_optuna_trials}'
        study = optuna.create_study(direction='maximize', study_name=study_name)
        
        if n_cv_folds_optuna >=2:
            print(f"\nIniciando otimização com Optuna ({n_optuna_trials} trials) e {n_cv_folds_optuna}-Fold CV...")
        else:
            print(f"\nIniciando otimização com Optuna ({n_optuna_trials} trials) e validação simples (holdout)...")

        # Executa a otimização
        # A função lambda passa os dados e o número de folds para objective_optuna_cv
        study.optimize(
            lambda trial: objective_optuna_cv(
                trial, 
                X_train_optuna_selected, # Usa as features selecionadas pelo RFECV
                y_train_optuna, 
                n_cv_splits_internal=n_cv_folds_optuna
            ),
            n_trials=n_optuna_trials, 
            timeout=optuna_timeout
        )

        print("\nOtimização com Optuna concluída!")
        best_optuna_score = study.best_trial.value if study.best_trial else -1.0
        print(f"Melhor Acurácia Média no CV/Val do Optuna: {best_optuna_score:.4f}")
        best_params_optuna = study.best_trial.params if study.best_trial else {}
        print(f"Melhores hiperparâmetros (Optuna): {best_params_optuna}")
```
8.  **Treinamento do Modelo Final**:
    * O conjunto `X_train_optuna_selected` é dividido em um conjunto de treino final (80%) e um conjunto de validação interna (20%).
    * O modelo `lgb.LGBMClassifier` é treinado nesses dados usando os melhores hiperparâmetros encontrados pelo Optuna e `early_stopping` (25 rodadas de paciência) para evitar overfitting, usando o conjunto de validação interna.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a otimização com Optuna e obtenção de best_params_optuna) ...

        # Divide X_train_optuna_selected e y_train_optuna em conjuntos finais de treino e validação interna
        # Esta validação interna é para o early stopping do modelo final.
        X_train_final, X_val_internal, y_train_final, y_val_internal = train_test_split(
            X_train_optuna_selected, y_train_optuna, 
            test_size=0.20, # 20% para validação interna, 80% para treino final
            random_state=42, 
            stratify=y_train_optuna # Mantém a proporção das classes
        )

        # Define o objetivo e a métrica para o modelo final, baseado se é binário ou multiclasse
        lgbm_final_objective = 'binary' if is_binary_classification else 'multiclass'
        lgbm_final_metric = 'binary_logloss' if is_binary_classification else 'multi_logloss'

        # Cria a instância final do LGBMClassifier com os melhores parâmetros do Optuna
        best_lgbm = lgb.LGBMClassifier(
            objective=lgbm_final_objective, 
            metric=lgbm_final_metric,
            random_state=42, 
            n_jobs=-1, 
            verbose=-1, # Suprime a maioria dos logs do LightGBM durante o fit
            **best_params_optuna # Desempacota os melhores hiperparâmetros encontrados
        )
        
        # Se for multiclasse, define o número de classes explicitamente
        if not is_binary_classification:
            best_lgbm.set_params(num_class=len(le.classes_)) # le.classes_ vem do LabelEncoder

        print("Treinando o modelo final com early stopping...")
        # Treina o modelo final
        # eval_set é usado para early stopping
        # callbacks=[lgb.early_stopping(25, verbose=False)] para o treinamento se a métrica em
        # X_val_internal não melhorar por 25 rodadas. verbose=False para não imprimir logs do early stopping.
        best_lgbm.fit(
            X_train_final, y_train_final, 
            eval_set=[(X_val_internal, y_val_internal)],
            eval_metric=lgbm_final_metric, 
            callbacks=[lgb.early_stopping(25, verbose=False)] 
        )

        # Obtém o número de árvores efetivamente usado pelo modelo final (devido ao early stopping)
        final_model_iter = best_lgbm.best_iteration_ if hasattr(best_lgbm, 'best_iteration_') and best_lgbm.best_iteration_ is not None else best_params_optuna.get('n_estimators')
        print(f"Modelo final treinado. Número de árvores: {final_model_iter}")

        # Avalia a acurácia do modelo final no seu próprio conjunto de treinamento (para referência)
        y_pred_train_final = best_lgbm.predict(X_train_final)
        accuracy_train_final = accuracy_score(y_train_final, y_pred_train_final)
        print(f"Acurácia do Modelo Final no seu Conjunto de Treinamento (X_train_final): {accuracy_train_final:.4f}")
```
9.  **Avaliação do Modelo Final**:
    * O modelo treinado é usado para fazer previsões no conjunto de teste (`X_test_selected`).
    * São calculadas e exibidas diversas métricas: acurácia, relatório de classificação (precisão, recall, F1-score por classe), matriz de confusão e ROC AUC.
    * A matriz de confusão normalizada e um gráfico de importância das features do modelo final são plotados e salvos.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após o treinamento do modelo final, best_lgbm) ...

        print("\nAvaliação do modelo final no conjunto de teste (com features selecionadas)...")
        
        # Faz previsões no conjunto de teste
        y_pred_test = best_lgbm.predict(X_test_selected)
        
        # Faz previsões de probabilidade para todas as classes (necessário para ROC AUC)
        y_pred_proba_all_classes_test = best_lgbm.predict_proba(X_test_selected)

        # Calcula as métricas
        accuracy_test = accuracy_score(y_test, y_pred_test)
        f1_test = f1_score(y_test, y_pred_test, average='weighted') # Ponderado para levar em conta desbalanceamento

        # Gera o relatório de classificação como dicionário e string
        report_dict_test = classification_report(y_test, y_pred_test, target_names=le.classes_, zero_division=0, output_dict=True)
        report_str_test = classification_report(y_test, y_pred_test, target_names=le.classes_, zero_division=0)

        conf_matrix_test = confusion_matrix(y_test, y_pred_test)
        
        roc_auc_test = 0.0
        if len(le.classes_) >= 2: # ROC AUC só faz sentido com pelo menos 2 classes
            if is_binary_classification:
                # Para binário, usa a probabilidade da classe positiva (geralmente a classe 1)
                roc_auc_test = roc_auc_score(y_test, y_pred_proba_all_classes_test[:, 1]) if y_pred_proba_all_classes_test.shape[1] == 2 else 0.0
            else:
                # Para multiclasse, usa 'ovr' (One-vs-Rest) e média ponderada
                 roc_auc_test = roc_auc_score(y_test, y_pred_proba_all_classes_test, multi_class='ovr', average='weighted')

        # Extrai precisões do relatório para resumo
        macro_avg_precision_test = report_dict_test.get('macro avg', {}).get('precision', 0.0)
        weighted_avg_precision_test = report_dict_test.get('weighted avg', {}).get('precision', 0.0)

        print(f"\n--- Resultados da Avaliação no CONJUNTO DE TESTE (v7 - Final - {'Binário' if is_binary_classification else 'Multiclasse'}) ---")
        print(f"Acurácia no Teste: {accuracy_test:.4f}")
        print(f"Precisão Média (Macro Avg) no Teste: {macro_avg_precision_test:.4f}")
        print(f"Precisão Média (Weighted Avg) no Teste: {weighted_avg_precision_test:.4f}")
        print(f"F1-Score (Ponderado) no Teste: {f1_test:.4f}")
        print(f"ROC AUC ({'Binário' if is_binary_classification else 'Ponderado OVR'}) no Teste: {roc_auc_test:.4f}")
        print("\nRelatório de Classificação (Teste):\n", report_str_test)

        # Plotagem e salvamento da Matriz de Confusão Normalizada
        conf_matrix_normalized_test = None
        # Verifica se a normalização é possível (evita divisão por zero se uma classe não tiver amostras verdadeiras)
        if len(le.classes_) > 1 and conf_matrix_test.sum(axis=1, keepdims=True).all() > 0 :
            conf_matrix_normalized_test = conf_matrix_test.astype('float') / conf_matrix_test.sum(axis=1, keepdims=True)
            plt.figure(figsize=(max(8, len(le.classes_)*1.5), max(6, len(le.classes_)*1.2)))
            sns.heatmap(conf_matrix_normalized_test, annot=True, fmt=".2%", cmap="Blues", xticklabels=le.classes_, yticklabels=le.classes_)
            plt.title(f'Matriz de Confusão Normalizada (Teste - v7 Final - {"Binário" if is_binary_classification else "Multiclasse"})')
            plt.ylabel('Classe Verdadeira'); plt.xlabel('Classe Prevista')
            plt.savefig('visualizacoes_classificacao_salario_v7_rfecv/matriz_confusao_norm_v7_final_teste.png')
            plt.show() # No notebook, isso exibe o gráfico
            plt.close()
        elif len(le.classes_) > 1:
            print("Aviso: Não foi possível normalizar a matriz de confusão (alguma classe pode não ter amostras verdadeiras no conjunto de teste).")

        # Plotagem e salvamento da Importância das Features
        feature_importance_df = None
        if hasattr(best_lgbm, 'feature_importances_') and X_train_final.shape[1] > 0: # X_train_final tem as features selecionadas
            feature_importance_df = pd.DataFrame({
                'feature': X_train_final.columns, # Nomes das features usadas no modelo final
                'importance': best_lgbm.feature_importances_
            }).sort_values(by='importance', ascending=False)
            
            print("\nImportância das Features (após RFECV, modelo Optuna com ES):\n", feature_importance_df.head(min(15, len(X_train_final.columns))))
            
            plt.figure(figsize=(10, max(6, len(feature_importance_df.head(min(15, len(X_train_final.columns)))) * 0.5)))
            sns.barplot(x='importance', y='feature', data=feature_importance_df.head(min(15, len(X_train_final.columns))))
            plt.title(f'Top {min(15, len(X_train_final.columns))} Features (v7 Final - {"Binário" if is_binary_classification else "Multiclasse"})')
            plt.tight_layout()
            plt.savefig('visualizacoes_classificacao_salario_v7_rfecv/feature_importance_v7_final.png')
            plt.show() # No notebook, isso exibe o gráfico
            plt.close()
```
10. **Salvamento de Resultados e Modelo**:
    * Um arquivo de texto com os resultados detalhados e os parâmetros é salvo.
    * O modelo treinado, o `LabelEncoder`, as features selecionadas e o `StandardScaler` são salvos em um arquivo `.pkl` usando `pickle` para uso futuro (ex: previsões em novos dados ou análises adicionais).

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após a avaliação do modelo final) ...

        results_filename_txt = "modelo_classificacao_faixa_salarial_v7_final_rfecv_resultados.txt"
        model_filename_pkl = 'modelo_lgbm_classificacao_faixa_salarial_v7_final_rfecv.pkl'
        
        with open(results_filename_txt, "w", encoding="utf-8") as f:
            f.write(f"Modelo: LightGBM (Optuna, RFECV, ES) para classificação de Faixa Salarial (v7 Final - {'Binário' if is_binary_classification else f'Multiclasse ({len(le.classes_)} classes)'})\\n")
            f.write(f"Coluna Alvo Agrupada: {target_col_agrupada_name} com classes: {list(le.classes_)}\\n")
            # initial_feature_columns_after_region contém as features antes do RFECV, após mapeamento de UF
            f.write(f"Features Iniciais para processamento ({len(initial_feature_columns_after_region)}): {initial_feature_columns_after_region}\\n")
            f.write(f"Features Selecionadas pelo RFECV ({rfecv_selector.n_features_}): {selected_features_names}\\n\\n")
            
            f.write(f"Melhores parâmetros (Optuna): {best_params_optuna}\\n")
            f.write(f"Número de árvores usadas pelo modelo final: {final_model_iter}\\n\\n")
            
            f.write(f"Acurácia Média CV/Val (Optuna): {best_optuna_score:.4f}\\n")
            f.write(f"Acurácia do Modelo Final no seu Conjunto de Treinamento (X_train_final): {accuracy_train_final:.4f}\\n\\n")
            
            f.write(f"RESULTADOS NO CONJUNTO DE TESTE:\\n")
            f.write(f"  Acurácia no Teste: {accuracy_test:.4f}\\n")
            f.write(f"  Precisão Média (Macro Avg) no Teste: {macro_avg_precision_test:.4f}\\n")
            f.write(f"  Precisão Média (Weighted Avg) no Teste: {weighted_avg_precision_test:.4f}\\n")
            f.write(f"  F1-Score (Ponderado) no Teste: {f1_test:.4f}\\n")
            f.write(f"  ROC AUC ({'Binário' if is_binary_classification else 'Ponderado OVR'}) no Teste: {roc_auc_test:.4f}\\n\\n")
            
            f.write("Relatório de Classificação (Teste):\\n"); f.write(report_str_test)
            f.write("\\nMatriz de Confusão (Teste - Absoluta):\\n"); f.write(str(conf_matrix_test)) # Salva a matriz de confusão absoluta
            
            if feature_importance_df is not None:
                 f.write("\\n\\nImportância das Features:\\n"); f.write(feature_importance_df.to_string())

        # Salva o modelo e outros objetos necessários para inferência/análise futura
        with open(model_filename_pkl, 'wb') as f: 
            pickle.dump({
                'model': best_lgbm, 
                'label_encoder': le, 
                'selected_features': selected_features_names,
                'scaler_rfecv_fitted_on_initial_numerical': scaler_rfecv, # O scaler ajustado em X_initial
                'original_columns_for_scaler': numerical_features_present_after_outliers, # Colunas em que o scaler foi ajustado
                'is_binary_classification': is_binary_classification,
                'target_col_name': target_col_agrupada_name
            }, f)
        print(f"Modelo e metadados salvos em {model_filename_pkl}")

        # Retorna um dicionário com os principais resultados
        return {
            'accuracy_train_final': accuracy_train_final,
            'optuna_best_cv_score': best_optuna_score,
            'accuracy_test': accuracy_test,
            'macro_avg_precision_test': macro_avg_precision_test,
            'weighted_avg_precision_test': weighted_avg_precision_test,
            'f1_score_test': f1_test,
            'roc_auc_test': roc_auc_test,
            'selected_features_count': rfecv_selector.n_features_,
            'selected_features_names': selected_features_names,
            'best_params': best_params_optuna, 
            'model_object_path': model_filename_pkl,
            'final_model_best_iteration': final_model_iter,
            'classification_report_dict_test': report_dict_test,
            'is_binary_classification': is_binary_classification,
            'target_classes': list(le.classes_)
        }

    except Exception as e:
        print(f"Ocorreu um erro inesperado na função principal: {e}")
        traceback.print_exc(); return None
```
11. **Retorno de Resultados**:
    * A função retorna um dicionário contendo as principais métricas e informações da execução.

```python
# (Dentro da função train_classification_model_salary_range_v7_final)
        # ... (Após o salvamento do modelo e dos resultados em arquivo) ...

        # Retorna um dicionário com os principais resultados e informações da execução
        return {
            'accuracy_train_final': accuracy_train_final,
            'optuna_best_cv_score': best_optuna_score,
            'accuracy_test': accuracy_test,
            'macro_avg_precision_test': macro_avg_precision_test,
            'weighted_avg_precision_test': weighted_avg_precision_test,
            'f1_score_test': f1_test,
            'roc_auc_test': roc_auc_test,
            'selected_features_count': rfecv_selector.n_features_,
            'selected_features_names': selected_features_names,
            'best_params': best_params_optuna, 
            'model_object_path': model_filename_pkl, # Caminho para o arquivo .pkl salvo
            'final_model_best_iteration': final_model_iter, # Número de árvores do modelo final
            'classification_report_dict_test': report_dict_test, # Relatório de classificação como dicionário
            'is_binary_classification': is_binary_classification, # Flag se é binário
            'target_classes': list(le.classes_) # Nomes das classes do alvo
        }

    # Bloco try-except principal da função
    except Exception as e:
        print(f"Ocorreu um erro inesperado na função principal: {e}")
        traceback.print_exc()
        return None # Retorna None em caso de erro para indicar falha na execução
```
Este processo estruturado visa garantir que o modelo seja treinado de forma eficiente, otimizado para o melhor desempenho possível nos dados disponíveis e avaliado de maneira justa em dados não vistos, fornecendo insights sobre a importância das features no problema de classificação da faixa salarial.
