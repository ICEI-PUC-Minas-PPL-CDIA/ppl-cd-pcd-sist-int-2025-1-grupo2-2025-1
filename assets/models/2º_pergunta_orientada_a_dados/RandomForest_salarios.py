import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# === Passo 1: Carregar os dados ===
state_file = '/content/State_of_data_BR_2023_Kaggle - df_survey_2023 (1).csv' 
edu_file = '/content/MICRODADOS_ED_SUP_IES_2023 (1).CSV'

df_state = pd.read_csv(state_file)
df_edu = pd.read_csv(edu_file, sep=';', encoding='latin1')

# === Passo 2: Pré-processar a base State of Data ===
df_state = df_state[[
"('P2_i ', 'Quanto tempo de experiência na área de dados você tem?')",
"('P2_g ', 'Nivel')",
"('P2_h ', 'Faixa salarial')",
"('P1_i_2 ', 'Regiao onde mora')"
]].copy()
df_state.columns = ['experiencia', 'nivel', 'salario', 'regiao']

# Mapear experiência
exp_map = {
'menos de 1 ano': 0.5,
'de 1 a 2 anos': 1.5,
'de 2 a 3 anos': 2.5,
'de 3 a 4 anos': 3.5,
'de 4 a 5 anos': 4.5,
'de 5 a 6 anos': 5.5,
'de 6 a 7 anos': 6.5,
'de 7 a 8 anos': 7.5,
'de 8 a 9 anos': 8.5,
'de 9 a 10 anos': 9.5,
'de 10 a 11 anos': 10.5,
'de 11 a 12 anos': 11.5,
'de 12 a 13 anos': 12.5,
'de 13 a 14 anos': 13.5,
'de 14 a 15 anos': 14.5,
'15 anos ou mais': 16.0
}
df_state['experiencia_num'] = df_state['experiencia'].map(exp_map)

# Mapear salário
salario_map = {
'de R$ 1.001/mês a R$ 2.000/mês': 1500,
'de R$ 2.001/mês a R$ 3.000/mês': 2500,
'de R$ 3.001/mês a R$ 4.000/mês': 3500,
'de R$ 4.001/mês a R$ 6.000/mês': 5000,
'de R$ 6.001/mês a R$ 8.000/mês': 7000,
'de R$ 8.001/mês a R$ 12.000/mês': 10000,
'de R$ 12.001/mês a R$ 16.000/mês': 14000,
'de R$ 16.001/mês a R$ 20.000/mês': 18000,
'de R$ 20.001/mês a R$ 25.000/mês': 22500,
'de R$ 25.001/mês a R$ 30.000/mês': 27500,
'de R$ 30.001/mês a R$ 40.000/mês': 35000,
'Acima de R$ 40.001/mês': 40000
}
df_state['salario_num'] = df_state['salario'].map(salario_map)

# Codificar nível
le_nivel = LabelEncoder()
df_state['nivel_cod'] = le_nivel.fit_transform(df_state['nivel'].astype(str))

# === Passo 3: Agregar dados regionais da base educacional ===
df_edu_group = df_edu.groupby('NO_REGIAO_IES').agg({
'QT_DOC_TOTAL': 'sum',
'QT_TEC_TOTAL': 'sum',
'QT_DOC_EX_DOUT': 'sum',
'QT_DOC_EX_MEST': 'sum',
'CO_IES': 'nunique'
}).reset_index()

df_edu_group.columns = [
'regiao',
'docentes_regiao',
'tecnicos_regiao',
'docentes_doutorado_regiao',
'docentes_mestrado_regiao',
'num_ies_regiao'
]

# === Passo 4: Merge das bases ===
df_merged = pd.merge(df_state, df_edu_group, on='regiao', how='left')

# === Passo 5: Preparar para modelagem ===
df_model = df_merged[[
'experiencia_num',
'nivel_cod',
'docentes_regiao',
'tecnicos_regiao',
'docentes_mestrado_regiao',
'num_ies_regiao',
'salario_num'
]].dropna()

X = df_model.drop(columns='salario_num')
y = df_model['salario_num']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# === Passo 6: Treinar modelo com hiperparâmetros ajustados ===
model = RandomForestRegressor(
max_depth=None,
max_features='sqrt',
min_samples_leaf=2,
min_samples_split=5,
n_estimators=100,
random_state=42
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# === Passo 7: Avaliar modelo ===
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R²: {r2_score(y_test, y_pred):.2f}")

# Importância das variáveis
importances = model.feature_importances_
for name, imp in zip(X.columns, importances):
    print(f"{name}: {imp:.2%}") # Indented this line
