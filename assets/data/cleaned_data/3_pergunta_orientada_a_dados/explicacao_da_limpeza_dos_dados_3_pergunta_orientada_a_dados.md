# Explicação Detalhada dos Arquivos de Limpeza de Dados

## 📄 `process_data.py`
**Primeira limpeza, mas sem padronização de categorias.**

---

### 1. Configuração de ambiente

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
```
>Explicação:
Importa bibliotecas e define configurações de gráficos (não relacionado à limpeza diretamente).

---

### 2. Carregar o Excel

```python
df = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')
```

>Explicação:
Carrega a base de dados.

---

### 3. Selecionar colunas de interesse

```python
colunas_interesse = {
    'faixa_etaria': ('P1_a_1 ', 'Faixa idade'),
    'genero': ('P1_b ', 'Genero'),
    # ...
}
df_analise = pd.DataFrame()
for chave, coluna in colunas_interesse.items():
    if coluna in df.columns:
        df_analise[chave] = df[coluna]
```

>Explicação:
Cria um DataFrame apenas com colunas específicas.

---

### 4. Tratar valores ausentes

```python
for col in ['faixa_etaria', 'genero', 'nivel_ensino', 'faixa_salarial']:
    if col in df_analise.columns:
        df_analise[col] = df_analise[col].fillna('Não informado')

for col in ['nao_afetado', 'impacto_raca', 'impacto_genero']:
    if col in df_analise.columns:
        df_analise[col] = df_analise[col].fillna(0).astype(int)
```

>Explicação:
Categóricas recebem "Não informado"; binárias recebem 0.

---

### 5. Definir ordens (mas não aplicar)

```python
ordem_faixa_etaria = [
    'Menos de 18 anos', '18-24 anos', '25-34 anos', '35-44 anos', 
    '45-54 anos', '55-64 anos', '65 anos ou mais', 'Não informado'
]
```

>Explicação:
Só define a ordem esperada, sem aplicar ainda.

---

### 6. Salvar o DataFrame

```python
df_analise.to_csv('visualizacoes/dados_processados.csv', index=False)
```

>Explicação:
Salva os dados limpos.

---

# Explicação Detalhada dos Arquivos de Limpeza de Dados

## 📄 `process_data_corrected.py`
**Versão corrigida: faz limpeza completa e padronização!**

---

### 1. Configuração de ambiente

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
```

>Explicação:
Importa bibliotecas e define configurações de gráficos (não relacionado à limpeza diretamente).

---

### 2. Seleção de colunas

```python
colunas_interesse = {
    'faixa_etaria': ('P1_a_1 ', 'Faixa idade'),
    'genero': ('P1_b ', 'Genero'),
    'cor_raca_etnia': ('P1_c ', 'Cor/raca/etnia'),
    # ...
}
df_analise = pd.DataFrame()
for chave, coluna in colunas_interesse.items():
    df_analise[chave] = df[coluna]
```

>Explicação:
Inclui também "cor_raca_etnia".

---

### 3. Tratamento de valores ausentes

```python

for col in ['faixa_etaria', 'genero', 'cor_raca_etnia', 'nivel_ensino', 'faixa_salarial', 'tempo_experiencia']:
    df_analise[col] = df_analise[col].fillna('Não informado')
```

>Explicação:
>Mais abrangente que o primeiro script.

---

### 4. Padronizar categorias

## Faixa etária:

```python
faixa_etaria_map = {
    '18-21': '18-24 anos',
    '22-24': '18-24 anos',
    '25-29': '25-34 anos',
    # ...
}
df_analise['faixa_etaria_padronizada'] = df_analise['faixa_etaria'].map(faixa_etaria_map)
```

>Explicação:
Agrupa faixas pequenas em faixas padrão.

## Nível de ensino

```python
nivel_ensino_map = {
    'Estudante de Graduação': 'Ensino Superior Incompleto',
    'Graduação/Bacharelado': 'Ensino Superior Completo',
    # ...
}
df_analise['nivel_ensino_padronizado'] = df_analise['nivel_ensino'].map(nivel_ensino_map)
```

>Explicação:
Corrige os nomes de nível de ensino.

## Faixa salarial
```python
faixa_salarial_map = {
    'até R$ 1.000/mês': 'Até R$ 1.000',
    'de R$ 1.001/mês a R$ 2.000/mês': 'De R$ 1.001 a R$ 2.000',
    # ...
}
df_analise['faixa_salarial_padronizada'] = df_analise['faixa_salarial'].map(faixa_salarial_map)
```

>Explicação:
Corrige faixas de salário para um padrão único.

---

### 5. Nova coluna: Relata impacto

```python
df_analise['relata_impacto'] = ((df_analise['impacto_raca'] > 0) | (df_analise['impacto_genero'] > 0)).astype(int)
```

>Explicação:
Marca quem relatou algum impacto.

---

### 6. Salvar

```python
df_analise.to_csv('visualizacoes/dados_processados.csv', index=False)
```

>Explicação:
salva.

---

## 📄 `process_data_debug.py`
**Script para diagnóstico e debug.**

### 1. Conferência de tipos de colunas
```python
for col in df.columns[:10]:
    print(f"- {col}, tipo: {type(col)}")
```

>Explicação:
>Verifica se os nomes de colunas são str ou tuple.

---

### 2. Forçar conversão para string

```python
df.columns = [str(col) for col in df.columns]
```

>Explicação:
Evita erros na busca de colunas.

--- 

### 3.Mapeamento automático de colunas

```python
colunas_mapeamento = {
    'faixa_etaria': 'Faixa idade',
    'genero': 'Genero',
    # ...
}
for chave, texto_parcial in colunas_mapeamento.items():
    colunas_correspondentes = [col for col in df.columns if texto_parcial in col]
```

>Explicação:
Busca coluna

---

### 4. Depois: Tratamento básico

```python
for col in ['faixa_etaria', 'genero', 'nivel_ensino', 'faixa_salarial']:
    df_analise[col] = df_analise[col].fillna('Não informado')
```

>Explicação:
Tratamento de valores ausentes como nos scripts anteriores.

---

### 5. Salvar o DataFrame

```python
df_analise.to_csv('visualizacoes/dados_processados.csv', index=False)
```

>Explicação:
Salva os dados, principalmente para checagem posterior.

# 📊 Resumo Final

| Arquivo                   | O que faz                        | Exemplo chave                                     | Quando usar        |
|:---------------------------|:----------------------------------|:--------------------------------------------------|:-------------------|
| `process_data.py`           | Primeira limpeza                  | Preencher NaN com "Não informado"                 | Rascunho rápido     |
| `process_data_corrected.py` | Limpeza + padronização completa   | Mapear faixas etárias, escolaridade, salários     | ✅ Análise final    |
| `process_data_debug.py`     | Diagnóstico                       | Conferir tipo e nomes de colunas                  | Debug de problemas |
