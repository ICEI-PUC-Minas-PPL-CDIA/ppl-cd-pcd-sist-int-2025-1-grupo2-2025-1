# 🧹 Limpeza de Dados - Microdados da Educação Superior 2023
[Codigo da limpeza](src/code_data_cleanest/base_auxiliares/limpezadedados_1perguntaorientadadados_baux.ipynb)


## 📄 Objetivo

Preparar os dados brutos da base **MICRODADOS_ED_SUP_IES_2023.CSV** para responder a uma **pergunta orientada a dados**, analisando a **distribuição de docentes por formação e faixa etária** em cada **Unidade da Federação (UF)**.

---

## 🔍 Etapas da Limpeza de Dados

### 1. **Importação e Leitura do Arquivo**
- O arquivo foi lido usando `pandas.read_csv()` com os parâmetros adequados:
  - `sep=';'` para reconhecer o delimitador correto.
  - `encoding='latin-1'` para interpretar corretamente os caracteres especiais.
  - `low_memory=False` para evitar avisos durante a leitura de grandes volumes de dados.

```python
df = pd.read_csv(input_file, sep=';', encoding='latin-1', low_memory=False)
```

---

### 2. **Seleção de Colunas Relevantes**
Foram selecionadas apenas as colunas necessárias para a análise:

| Coluna Original        | Descrição                                      |
|------------------------|------------------------------------------------|
| SG_UF_IES              | Sigla da Unidade Federativa                    |
| NO_UF_IES              | Nome completo da UF                            |
| QT_DOC_EX_GRAD         | Quantidade de docentes com graduação           |
| QT_DOC_EX_ESP          | Quantidade de docentes com especialização      |
| QT_DOC_EX_MEST         | Quantidade de docentes com mestrado            |
| QT_DOC_EX_DOUT         | Quantidade de docentes com doutorado           |
| QT_DOC_EX_30_34 a 60+  | Faixas etárias dos docentes (proxy de idade)   |

---

### 3. **Filtragem e Remoção de Ruído**
Foi criado um novo DataFrame contendo apenas as colunas presentes. Em seguida, aplicadas duas operações de limpeza:
- `.dropna()` → Remove linhas com valores ausentes (NaN).
- `.drop_duplicates()` → Remove linhas duplicadas.

```python
df_filtrado = df[colunas_presentes].copy()
df_limpo = df_filtrado.dropna().drop_duplicates()
```

---

### 4. **Agrupamento por UF**
Os dados foram **agrupados por UF (`SG_UF_IES`)**, somando os totais por nível de formação e faixa etária para cada estado.

```python
df_agrupado = df_limpo.groupby('SG_UF_IES').agg({...}).reset_index()
```

---

### 5. **Renomeação das Colunas**
As colunas foram renomeadas para termos mais compreensíveis e utilizáveis, facilitando a visualização e o uso posterior dos dados.

| Nome Original            | Novo Nome                    |
|--------------------------|------------------------------|
| SG_UF_IES                | UF                           |
| QT_DOC_EX_GRAD           | Docentes_Graduacao           |
| QT_DOC_EX_ESP            | Docentes_Especializacao      |
| QT_DOC_EX_MEST           | Docentes_Mestrado            |
| QT_DOC_EX_DOUT           | Docentes_Doutorado           |
| QT_DOC_EX_30_34          | Docentes_Idade_30_34         |
| ...                      | ...                          |
| QT_DOC_EX_60_MAIS        | Docentes_Idade_60_mais       |

---

### 6. **Exportação dos Dados Limpinhos**
O DataFrame final foi salvo como **arquivo CSV**, pronto para ser analisado, visualizado ou utilizado em painéis.

```python
df_agrupado.to_csv('microdados_agrupados_por_uf.csv', index=False)
```

---

## ✅ Resultado Final

Um arquivo `.csv` contendo a quantidade consolidada de docentes por formação e idade em cada UF, pronto para responder a perguntas como:

> "Quais estados concentram mais docentes com doutorado?"  
> "Como está distribuída a experiência (idade) dos docentes por região?"

---
