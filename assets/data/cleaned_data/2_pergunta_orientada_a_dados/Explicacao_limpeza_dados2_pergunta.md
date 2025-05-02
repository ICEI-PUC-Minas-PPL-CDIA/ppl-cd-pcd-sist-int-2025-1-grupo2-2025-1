## 🧹 **Limpeza de Dados - Profissionais de Dados e Tecnologia (2023)**

---

## 📄 Objetivo

Preparar os dados da pesquisa **State of Data BR 2023** para analisar:

- Relação entre formação acadêmica, senioridade e faixas salariais
- Distribuição geográfica (UF) dos salários
- Impacto de habilidades técnicas (SQL/Python) na remuneração

---

## 🟣 Etapas da Limpeza de Dados

### 1. Importação e Leitura do Arquivo

O arquivo foi lido utilizando `pandas.read_csv` com os parâmetros adequados:

- `encoding='utf-8'` para interpretar corretamente os caracteres especiais.

```python
df = pd.read_csv('dados_limpos.csv', encoding='utf-8')
```



---

### 2. Seleção e Renomeação de Colunas

Foram selecionadas apenas as colunas relevantes para a análise salarial e de perfil profissional.  
Além disso, as colunas foram renomeadas para facilitar o entendimento:

| Coluna Original      | Novo Nome               | Descrição                                      |
|----------------------|-------------------------|------------------------------------------------|
| Nivel_Ensino         | Formacao                | Grau de escolaridade                           |
| Area_Formacao        | Area_Formacao           | Área de formação acadêmica                     |
| Tempo_Experiencia    | Experiencia             | Tempo de experiência no mercado                |
| Nivel_Senioridade    | Senioridade             | Nível hierárquico (Júnior, Pleno, Sênior)      |
| Faixa_Salarial       | Faixa_Salarial          | Intervalo salarial em R$                       |
| UF                   | UF                      | Estado de atuação                              |
| SQL                  | SQL                     | Uso de SQL (0=Não, 1=Sim)                      |
| Python               | Python                  | Uso de Python (0=Não, 1=Sim)                   |
| Salario_Medio        | Salario_Medio           | Média salarial numérica                        |

---

### 3. Tratamento de Valores Ausentes

- Remoção de linhas com UF ausente:
- Preenchimento da coluna `Salario_Medio` usando a média dos valores da faixa salarial textual (exemplo: 'R$ 8.001-12.000' → 10000.5).

---

### 4. Normalização de Categorias

#### a) Senioridade

Padronização dos níveis de senioridade:

mapeamento_senioridade = {
'Júnior': 'Junior',
'Pleno': 'Pleno',
'Sênior': 'Senior'
}
```df['Senioridade'] = df['Senioridade'].map(mapeamento_senioridade)```


#### b) Faixa Salarial para Valor Numérico

Conversão das faixas salariais para um valor médio representativo:

def extrair_media_salarial(faixa):
# Implementação personalizada para converter texto em número
# Exemplo: 'de R$ 8.001/mês a R$ 12.000/mês' -> (8001 + 12000)/2
...
```df['Salario_Medio'] = df['Faixa_Salarial'].apply(extrair_media_salarial)```


---

### 5. Filtragem de Dados Irrelevantes

- Registros com `Formacao = 'Prefiro não informar'` ou `Senioridade = 'Não se aplica'` foram removidos.
- Apenas profissionais com `Salario_Medio > 0` foram mantidos.

---

### 6. Criação de Variáveis Derivadas

#### a) Habilidades Técnicas Combinadas
```df['Habilidades_Tecnicas'] = df['SQL'] + df['Python']```

0 (Nenhuma), 1 (SQL ou Python), 2 (Ambas)


#### b) Agrupamento de Áreas de Formação

Agrupamento de áreas similares:
```df['Area_Agrupada'] = df['Area_Formacao'].replace({
'Computação / Engenharia de Software / Sistemas de Informação/ TI': 'TI/Computação',
'Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais': 'Matemática/Estatística'
})
```

---

### 7. Exportação dos Dados Limpos
```df.to_csv('dados_profissionais_limpos.csv', index=False, encoding='utf-8')```


---

## ✅ Resultado Final

Um dataset pronto para análises variadas, como:

- Salário médio por UF e formação
- Correlação entre habilidades técnicas (SQL/Python) e salário
- Progressão salarial por tempo de experiência e senioridade
- Comparativo de áreas de formação com maior remuneração

> *Exemplo de análise respondível:*  
> "Profissionais de TI com doutorado no estado de SP que usam Python e SQL têm salários acima da média da categoria?"

---




