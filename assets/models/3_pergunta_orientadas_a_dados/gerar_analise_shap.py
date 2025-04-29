import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import shap
import os
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings('ignore')

# Criar diretório para visualizações adicionais
os.makedirs('visualizacoes_adicionais', exist_ok=True)

def clean_col_name(col_name):
    """Limpa o nome da coluna para ser compatível com LightGBM."""
    import re
    if isinstance(col_name, str) and col_name.startswith("(") and col_name.endswith(")"):
        try:
            evaluated_col = eval(col_name)
            if isinstance(evaluated_col, tuple):
                col_name = f"{evaluated_col[0].strip()}_{evaluated_col[1].strip()}"
        except:
            pass
    
    col_name = str(col_name)
    col_name = re.sub(r"[\W]+(?<!^)", "_", col_name)
    col_name = col_name.strip("_")
    if col_name and col_name[0].isdigit():
        col_name = "_" + col_name
    return col_name

def gerar_analises_adicionais(file_path):
    try:
        # Carregar o modelo treinado
        with open('modelo_lightgbm_especifico.pkl', 'rb') as f:
            model = pickle.load(f)
        
        print("Modelo carregado com sucesso.")
        
        # Carregar a base de dados principal
        df_main = pd.read_excel(file_path)
        print(f"Base de dados carregada: {df_main.shape[0]} linhas, {df_main.shape[1]} colunas")

        # --- Tratamento de Nomes de Colunas ---
        original_columns = df_main.columns.tolist()
        new_columns = [clean_col_name(col) for col in original_columns]
        
        # Verificar duplicatas após limpeza
        if len(new_columns) != len(set(new_columns)):
            print("Aviso: Nomes de colunas duplicados detectados após a limpeza. Renomeando...")
            counts = {}
            final_columns = []
            for col in new_columns:
                if col in counts:
                    counts[col] += 1
                    final_columns.append(f"{col}_{counts[col]}")
                else:
                    counts[col] = 0
                    final_columns.append(col)
            new_columns = final_columns

        df_main.columns = new_columns
        print("Nomes de colunas limpos e renomeados.")

        # Mapeamento dos nomes de colunas específicos solicitados pelo usuário
        col_mapping = {}
        for col in df_main.columns:
            if "P1_a_1" in col or "Faixa_idade" in col or "faixa_etaria" in col:
                col_mapping["faixa_etaria"] = col
            elif "P1_b" in col or "Genero" in col or "genero" in col:
                col_mapping["genero"] = col
            elif "P1_e_1" in col or "Não_acredito" in col or "nao_afetado" in col:
                col_mapping["nao_afetado"] = col
            elif "P1_e_2" in col or "Cor_Raça_Etnia" in col or "impacto_raca" in col:
                col_mapping["target"] = col
            elif "P1_e_3" in col or "identidade_de_gênero" in col or "impacto_genero" in col:
                col_mapping["impacto_genero"] = col
            elif "P1_l" in col or "Nivel_de_Ensino" in col or "nivel_ensino" in col:
                col_mapping["nivel_ensino"] = col
            elif "P2_h" in col or "Faixa_salarial" in col or "faixa_salarial" in col:
                col_mapping["faixa_salarial"] = col
            elif "P2_i" in col or "experiência_na_área" in col or "tempo_experiencia" in col:
                col_mapping["tempo_experiencia"] = col

        print("Mapeamento de colunas específicas:")
        for key, value in col_mapping.items():
            print(f"  {key}: {value}")

        # Verificar se todas as colunas necessárias foram encontradas
        required_cols = ["faixa_etaria", "genero", "nao_afetado", "target", "impacto_genero", 
                         "nivel_ensino", "faixa_salarial", "tempo_experiencia"]
        missing_cols = [col for col in required_cols if col not in col_mapping]
        
        if missing_cols:
            print(f"Erro: Colunas necessárias não encontradas: {missing_cols}")
            return

        # --- Preparação dos Dados ---
        # Remover linhas onde a variável alvo é NaN
        target_col = col_mapping["target"]
        df_main = df_main.dropna(subset=[target_col])
        print(f"Linhas após remover NaN na coluna alvo: {df_main.shape[0]}")

        # Selecionar apenas as colunas específicas
        feature_cols = [col_mapping[col] for col in required_cols if col != "target"]
        X = df_main[feature_cols].copy()
        y = df_main[target_col].astype(int)
        
        print(f"Features selecionadas: {X.columns.tolist()}")

        # Identificar colunas categóricas e numéricas
        categorical_features = X.select_dtypes(include=["object", "category"]).columns.tolist()
        numerical_features = X.select_dtypes(include=np.number).columns.tolist()

        # --- Pré-processamento ---
        # Preencher NaNs em numéricas com a mediana
        for col in numerical_features:
            if X[col].isnull().any():
                median_val = X[col].median()
                X[col] = X[col].fillna(median_val)

        # Converter categóricas para tipo "category" e preencher NaNs
        for col in categorical_features:
            # Converter para categoria primeiro
            if not isinstance(X[col].dtype, pd.CategoricalDtype):
                X[col] = X[col].astype("category")
            
            # Tratar valores ausentes
            if X[col].isnull().any():
                if "Missing" not in X[col].cat.categories:
                    X[col] = X[col].cat.add_categories("Missing")
                X[col] = X[col].fillna("Missing")
        
        print("Pré-processamento concluído.")

        # --- Divisão Treino/Teste ---
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        print(f"Dados divididos em treino ({X_train.shape[0]} amostras) e teste ({X_test.shape[0]} amostras).")

        # --- Análise SHAP ---
        print("Gerando análise SHAP...")
        
        # Criar um explainer SHAP para o modelo
        explainer = shap.TreeExplainer(model)
        
        # Calcular valores SHAP para o conjunto de teste
        shap_values = explainer.shap_values(X_test)
        
        # Gerar gráfico de resumo SHAP
        plt.figure(figsize=(12, 8))
        shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
        plt.title("Importância das Variáveis (SHAP Values)")
        plt.tight_layout()
        plt.savefig('visualizacoes_adicionais/shap_importancia_variaveis.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # Gerar gráfico de resumo SHAP com pontos
        plt.figure(figsize=(12, 10))
        shap.summary_plot(shap_values, X_test, show=False)
        plt.title("Impacto das Variáveis nas Previsões (SHAP Summary)")
        plt.tight_layout()
        plt.savefig('visualizacoes_adicionais/shap_summary_plot.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # --- Análise de Interseccionalidade ---
        print("Gerando análise de interseccionalidade...")
        
        # Criar DataFrame com previsões
        df_results = pd.DataFrame({
            'Genero': df_main.loc[X_test.index, col_mapping["genero"]],
            'Nivel_Ensino': df_main.loc[X_test.index, col_mapping["nivel_ensino"]],
            'Previsao': model.predict(X_test),
            'Real': y_test.values
        })
        
        # Análise de interseccionalidade: Gênero x Nível de Ensino
        plt.figure(figsize=(14, 10))
        intersec = pd.crosstab(
            df_results['Genero'], 
            df_results['Nivel_Ensino'],
            values=df_results['Previsao'],
            aggfunc='mean'
        )
        
        # Plotar heatmap
        sns.heatmap(intersec, annot=True, cmap='YlOrRd', fmt='.2f', cbar_kws={'label': 'Probabilidade de Experiência Prejudicada'})
        plt.title('Probabilidade de Experiência Prejudicada por Gênero e Nível de Ensino')
        plt.tight_layout()
        plt.savefig('visualizacoes_adicionais/interseccionalidade_genero_ensino.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # --- Análise por Faixa Salarial ---
        print("Gerando análise por faixa salarial...")
        
        # Adicionar faixa salarial ao DataFrame de resultados
        df_results['Faixa_Salarial'] = df_main.loc[X_test.index, col_mapping["faixa_salarial"]]
        
        # Calcular taxa de experiência prejudicada por faixa salarial
        faixa_salarial_impact = df_results.groupby('Faixa_Salarial')['Previsao'].mean().sort_values()
        
        plt.figure(figsize=(14, 8))
        ax = sns.barplot(x=faixa_salarial_impact.index, y=faixa_salarial_impact.values)
        plt.title('Probabilidade de Experiência Prejudicada por Faixa Salarial')
        plt.xlabel('Faixa Salarial')
        plt.ylabel('Probabilidade')
        plt.xticks(rotation=45, ha='right')
        
        # Adicionar valores nas barras
        for i, v in enumerate(faixa_salarial_impact.values):
            ax.text(i, v + 0.01, f'{v:.2f}', ha='center')
            
        plt.tight_layout()
        plt.savefig('visualizacoes_adicionais/experiencia_prejudicada_por_faixa_salarial.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # --- Análise por Tempo de Experiência ---
        print("Gerando análise por tempo de experiência...")
        
        # Adicionar tempo de experiência ao DataFrame de resultados
        df_results['Tempo_Experiencia'] = df_main.loc[X_test.index, col_mapping["tempo_experiencia"]]
        
        # Calcular taxa de experiência prejudicada por tempo de experiência
        tempo_exp_impact = df_results.groupby('Tempo_Experiencia')['Previsao'].mean().sort_values()
        
        plt.figure(figsize=(14, 8))
        ax = sns.barplot(x=tempo_exp_impact.index, y=tempo_exp_impact.values)
        plt.title('Probabilidade de Experiência Prejudicada por Tempo de Experiência')
        plt.xlabel('Tempo de Experiência')
        plt.ylabel('Probabilidade')
        plt.xticks(rotation=45, ha='right')
        
        # Adicionar valores nas barras
        for i, v in enumerate(tempo_exp_impact.values):
            ax.text(i, v + 0.01, f'{v:.2f}', ha='center')
            
        plt.tight_layout()
        plt.savefig('visualizacoes_adicionais/experiencia_prejudicada_por_tempo_experiencia.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # --- Análise de Casos Específicos ---
        print("Gerando análise de casos específicos...")
        
        # Caso 1: Profissional com nível de ensino alto
        caso1 = X_test.iloc[0].copy()
        caso1[col_mapping["nivel_ensino"]] = "Doutorado ou Phd"
        caso1[col_mapping["genero"]] = "Masculino"
        caso1_pred = model.predict_proba(pd.DataFrame([caso1]))[0]
        
        # Caso 2: Profissional com nível de ensino médio
        caso2 = X_test.iloc[0].copy()
        caso2[col_mapping["nivel_ensino"]] = "Graduação/Bacharelado"
        caso2[col_mapping["genero"]] = "Feminino"
        caso2_pred = model.predict_proba(pd.DataFrame([caso2]))[0]
        
        # Salvar casos específicos em um arquivo
        with open('visualizacoes_adicionais/casos_especificos.txt', 'w', encoding='utf-8') as f:
            f.write("Análise de Casos Específicos\n\n")
            
            f.write("Caso 1: Profissional com Doutorado (Masculino)\n")
            f.write(f"Probabilidade de Experiência NÃO Prejudicada: {caso1_pred[0]:.2f}\n")
            f.write(f"Probabilidade de Experiência Prejudicada: {caso1_pred[1]:.2f}\n\n")
            
            f.write("Caso 2: Profissional com Graduação (Feminino)\n")
            f.write(f"Probabilidade de Experiência NÃO Prejudicada: {caso2_pred[0]:.2f}\n")
            f.write(f"Probabilidade de Experiência Prejudicada: {caso2_pred[1]:.2f}\n")
        
        print("Análises adicionais geradas com sucesso!")
        
        return {
            'shap_values': shap_values,
            'X_test': X_test,
            'df_results': df_results
        }
        
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {file_path}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    file_path = "Main_database (2).xlsx"
    results = gerar_analises_adicionais(file_path)
