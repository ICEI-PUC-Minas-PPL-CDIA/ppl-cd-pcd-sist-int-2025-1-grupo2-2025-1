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
Importa bibliotecas e define configurações de gráficos (não relacionado à limpeza diretamente).

---

###  3. Selecionar colunas de interesse

```python
colunas_interesse = {
    'faixa_etaria': ('P1_a_1 ', 'Faixa idade'),
    'genero': ('P1_b ', 'Genero'),
    'nao_afetado': ('P1_e_1 ', 'Não acredito que minha experiência profissional seja afetada'),
    'impacto_raca': ('P1_e_2 ', 'Experiencia prejudicada devido a minha Cor Raça Etnia'),
    'impacto_genero': ('P1_e_3 ', 'Experiencia prejudicada devido a minha identidade de gênero'),
    'nivel_ensino': ('P1_l ', 'Nivel de Ensino'),
    'faixa_salarial': ('P2_h ', 'Faixa salarial'),
    'tempo_experiencia': ('P2_i ', 'Quanto tempo de experiência na área de dados você tem?'),
 }
```

>Explicação:
Identificar as colunas de interesse para a análise

---

### 4. Construir DataFrame de Análise

```python
df_analise = pd.DataFrame()
for chave, coluna in colunas_interesse.items():
    if coluna in df.columns:
        df_analise[chave] = df[coluna]
```

>Explicação:
Cria um novo DataFrame contendo apenas as colunas selecionadas.

---

### 5. Tratar valores ausentes

```python
for col in ['faixa_etaria', 'genero', 'nivel_ensino', 'faixa_salarial']:
    if col in df_analise.columns:
        df_analise[col] = df_analise[col].fillna('Não informado')
```

>Explicação:
Tratar valores ausentes (substituir por 'Não informado' para variáveis categóricas)

---

### 6. Converter colunas binárias

```python
for col in ['nao_afetado', 'impacto_raca', 'impacto_genero']:
    if col in df_analise.columns:
        df_analise[col] = df_analise[col].fillna(0).astype(int)
```

>Explicação:
Converter colunas binárias para valores numéricos (0 e 1) e tratar NaN

---

### 7. Define a ordem correta das variaveis

```python
ordem_faixa_etaria = [
    'Menos de 18 anos', '18-24 anos', '25-34 anos', '35-44 anos', 
    '45-54 anos', '55-64 anos', '65 anos ou mais', 'Não informado'
]

ordem_nivel_ensino = [
    'Ensino Fundamental', 'Ensino Médio', 'Ensino Técnico', 
    'Ensino Superior Incompleto', 'Ensino Superior Completo', 
    'Pós-graduação (Especialização)', 'Mestrado', 'Doutorado', 'Não informado'
]

ordem_faixa_salarial = [
    'Até R$ 1.000', 'De R$ 1.001 a R$ 2.000', 'De R$ 2.001 a R$ 3.000', 
    'De R$ 3.001 a R$ 4.000', 'De R$ 4.001 a R$ 6.000', 'De R$ 6.001 a R$ 8.000', 
    'De R$ 8.001 a R$ 12.000', 'De R$ 12.001 a R$ 16.000', 'De R$ 16.001 a R$ 20.000', 
    'De R$ 20.001 a R$ 25.000', 'Acima de R$ 25.000', 'Não informado'
]
```

>Explicação:
Definir a ordem correta para variáveis ordinais

---

### 8. Salvar resultado

```python
df_analise.to_csv('visualizacoes/dados_processados.csv', index=False)

print("\nDados processados e salvos em 'visualizacoes/dados_processados.csv'")
```

>Explicação:
Salvar o DataFrame processado

---

## 📄 `process_data_corrected.py`
**Limpeza + detecção dinâmica de colunas + início de padronização de categorias.**

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
Mesma configuração de bibliotecas e estilo de gráficos

---

### 2. Carregar e converter colunas

```python
df = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')
df.columns = [str(col) for col in df.columns]
```
>Explicação:
Carrega a base e converte todos os nomes de colunas para string, facilitando a busca

---

### 3. Encontrar colunas dinamicamente

```python
colunas_interesse = {
    'faixa_etaria': ('P1_a_1 ', 'Faixa idade'),
    'genero': ('P1_b ', 'Genero'),
    'cor_raca_etnia': ('P1_c ', 'Cor/raca/etnia'),
    'nao_afetado': ('P1_e_1 ', 'Não acredito que minha experiência profissional seja afetada'),
    'impacto_raca': ('P1_e_2 ', 'Experiencia prejudicada devido a minha Cor Raça Etnia'),
    'impacto_genero': ('P1_e_3 ', 'Experiencia prejudicada devido a minha identidade de gênero'),
    'nivel_ensino': ('P1_l ', 'Nivel de Ensino'),
    'faixa_salarial': ('P2_h ', 'Faixa salarial'),
    'tempo_experiencia': ('P2_i ', 'Quanto tempo de experiência na área de dados você tem?')
}
```

>Explicação:
Identificar as colunas de interesse para a análise

---

### 4. Criar DataFrame de Análise

```python
df_analise = pd.DataFrame()
for chave, coluna in colunas_interesse.items():
    df_analise[chave] = df[coluna]
```

>explicação:
Novo DataFrame apenas com as colunas encontradas

---

### 5. Tratar valores ausentes

```python
for col in ['faixa_etaria', 'genero', 'cor_raca_etnia', 'nivel_ensino', 'faixa_salarial', 'tempo_experiencia']:
    df_analise[col] = df_analise[col].fillna('Não informado')
```

>Explicação:
Tratar valores ausentes (substituir por 'Não informado' para variáveis categóricas)

---

### 6. Criar colunas padronizadas

## Faixa etária

```python
faixa_etaria_map = {
    '18-21': '18-24 anos',
    '22-24': '18-24 anos',
    '25-29': '25-34 anos',
    '30-34': '25-34 anos',
    '35-39': '35-44 anos',
    '40-44': '35-44 anos',
    '45-49': '45-54 anos',
    '50-54': '45-54 anos',
    '55-59': '55-64 anos',
    '60-64': '55-64 anos',
    '65+': '65 anos ou mais',
    'Não informado': 'Não informado'
}
df_analise['faixa_etaria_padronizada'] = df_analise['faixa_etaria'].map(faixa_etaria_map)
```
>Explicação:
Agrupa faixas pequenas em faixas padrão.

## Nível de ensino

```python
nivel_ensino_map = {
    'Ensino Fundamental': 'Ensino Fundamental',
    'Ensino Médio': 'Ensino Médio',
    'Ensino Técnico': 'Ensino Técnico',
    'Estudante de Graduação': 'Ensino Superior Incompleto',
    'Graduação/Bacharelado': 'Ensino Superior Completo',
    'Pós-graduação/Especialização': 'Pós-graduação (Especialização)',
    'Mestrado': 'Mestrado',
    'Doutorado ou Phd': 'Doutorado',
    'Não informado': 'Não informado'
}
df_analise['nivel_ensino_padronizado'] = df_analise['nivel_ensino'].map(nivel_ensino_map)
````

>Explicação:
Corrige faixas de salário para um padrão único.

---

### 7. Criar coluna de impacto

```python
df_analise['relata_impacto'] = ((df_analise['impacto_raca'] > 0) | (df_analise['impacto_genero'] > 0)).astype(int)
```

>Explicação:
Criar coluna para identificar pessoas que relataram impacto

---

### 8. Salvar resultado

```python
df_analise.to_csv('visualizacoes/dados_processados.csv', index=False)
```

>Explição:
Exporta o DataFrame final tratado.


---

## 📄 'processar_dados_complementares.py'
**Comparação entre base principal e dados externos (análises de interseccionalidade e região).**

---

### 1. Configuração de ambiente
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12
sns.set_palette("viridis")
```
>Explicacção:
Importação de bibliotecas e ajustes de visualização.

---

### 2. Carregar os dados

```python
df_bq = pd.read_csv('/home/ubuntu/upload/bq-results-20250422-030542-1745291209599.csv')
df_main = pd.read_excel('/home/ubuntu/upload/Main_database.xlsx')
```

>Explicação:
Carrega a base principal e uma base complementar (bq-results,arquivo contendo a PNAD(contínua-2023)).

---

### 3. Mapear valores de gênero e raça

```python
genero_mapping = {
    'Masculino': 'Homem',
    'Feminino': 'Mulher',
    'Outro': 'Outro',
    'Prefiro não informar': 'Não informado'
}
```

>Explicação:
Mapear valores de gênero da Main_database para corresponder aos do bq-results

```python
cor_raca_mapping = {
    'Branca': 'Branca',
    'Preta': 'Preta',
    'Parda': 'Parda',
    'Amarela': 'Amarela',
    'Indígena': 'Indígena',
    'Prefiro não informar': 'Não informado',
    'Outra': 'Outra'
}
```

>Explicação:
Mapear valores de cor/raça da Main_database para corresponder aos do bq-results

---

### 4. Análise de Interseccionalidade

```python
df_bq['interseccao'] = df_bq[genero_bq] + '_' + df_bq[cor_raca_bq]
df_main['interseccao'] = df_main['genero_mapeado'] + '_' + df_main['cor_raca_mapeada']
```

>Explicação:
Criar categorias combinadas no bq-results

---

### 5. Análise Regional

```python
df_bq['regiao'] = df_bq[uf_bq].map(regiao_mapping)
df_main['regiao'] = df_main[uf_main].map(regiao_mapping)
```

>Explicação:
Agrupa os dados pelas grandes regiões do Brasil

---

### 6. Comparações por região

```python
genero_regiao_bq = pd.crosstab(df_bq['regiao'], df_bq[genero_bq], normalize='index') * 100
cor_raca_regiao_bq = pd.crosstab(df_bq['regiao'], df_bq[cor_raca_bq], normalize='index') * 100
```

>Explicação:
Calcula a distribuição de gênero e cor/raça em cada região

---

### 7. Salvar comparações

```python
for nome, df in resultados.items():
    df.to_csv(f'visualizacoes_complementares/{nome}.csv')
```

>Explicação:
Exporta os resultados das análises complementares em arquivos .csv

# 🧹 Resumo dos Arquivos

Arquivo | Função Principal
|:--------------------------------|:----------------------------------|
`process_data.py`                    | Limpeza inicial, seleção de colunas.
`process_data_debug.py`              | Limpeza + busca dinâmica de colunas + início da padronização.
`processar_dados_complementares.py`  | Análises externas de representatividade (interseccionalidade, região).
