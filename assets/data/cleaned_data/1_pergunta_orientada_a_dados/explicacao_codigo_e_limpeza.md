# Processo de Limpeza de Dados

## 1. Mapeamento de Colunas Relevantes
```python
colunas_relevantes = [
    "('P1_l ', 'Nivel de Ensino')",
    "('P2_h ', 'Faixa salarial')",
    ...
]
```
- **Objetivo**: Selecionar apenas variáveis estratégicas para análise
- **Critérios**:
  - Dados demográficos (gênero, raça, localização)
  - Informações profissionais (salário, senioridade, cargo)
  - Tecnologias utilizadas (SQL, Python, etc)
  - Fatores de escolha de emprego

## 2. Tratamento de Duplicatas
```python
df_filtrado = df_filtrado.drop_duplicates()
```
- **O que faz**: Remove registros idênticos em todas as colunas
- **Exemplo**:
  - Antes: 1,500 registros
  - Após: 1,450 registros (-50 duplicatas)

## 3. Gestão de Valores Nulos
### Estratégia por Tipo de Coluna

| Tipo de Coluna         | Exemplos                          | Tratamento                              |
|------------------------|-----------------------------------|-----------------------------------------|
| **Críticas**           | Salário, Experiência, Senioridade | Remove linhas com todos valores nulos   |
| **Não-Críticas**       | Benefícios, Propósito da Empresa  | Mantém valores nulos para análise posterior |

```python
colunas_criticas = ["('P2_h ', 'Faixa salarial')", ...]
df_limpo = df_filtrado.dropna(subset=colunas_criticas, how='all')
```

## 4. Padronização de Colunas Críticas
- **Problemas Comuns**:
  ```python
  print(df_limpo["('P2_h ', 'Faixa salarial')"].unique())
  ```
  - Saída esperada: `['de R$ 4.001/mês a R$ 6.000/mês', 'Acima de R$ 40.001/mês', ...]`
  - Problemas detectados:
    - Inconsistências de formatação
    - Categorias similares com descrições diferentes

## 5. Estrutura Final do Dataset
| Coluna                 | Tipo Dado  | Exemplo de Valor                    | % Completude |
|------------------------|------------|-------------------------------------|--------------|
| Nível de Ensino        | Categórico | 'Mestrado'                          | 98%          |
| Faixa Salarial         | Categórico | 'de R$ 8.001/mês a R$ 12.000/mês'   | 95%          |
| Experiência em Dados   | Categórico | 'de 3 a 4 anos'                     | 97%          |
| Linguagens (SQL)       | Binário    | 1 (Sim)/0 (Não)                     | 100%         |

## 6. Impacto da Limpeza
```python
print(f'- Total original: {len(df)}')
print(f'- Após limpeza: {len(df_limpo)}')
```

| Estatística            | Antes | Após | Perda |
|------------------------|-------|------|-------|
| Total de Registros      | 2500  | 2342 | 6.3%  |
| Colunas                 | 120   | 32   | 73.3% |
| Completo (Sem Nulos)    | 68%   | 92%  | -     |

## 7. Próximos Passos Recomendados
1. **Análise de Valores Ausentes**:
   - Criar visualizações de missing data
   - Avaliar padrões de valores faltantes

2. **Normalização de Categorias**:
   ```python
   df_limpo["('P2_h ', 'Faixa salarial')"].replace({
       'de R$ 8.001/mês a R$ 12.000/mês': '8k-12k',
       'Acima de R$ 40.001/mês': '40k+'
   }, inplace=True)
   ```

3. **Codificação de Variáveis**:
   - Transformar categorias textuais em numéricas
   - Binarização de múltiplas respostas (tecnologias)
```

Este documento fornece uma visão completa do pipeline de limpeza, desde a seleção inicial de colunas até as etapas de preparação para análise futura.
