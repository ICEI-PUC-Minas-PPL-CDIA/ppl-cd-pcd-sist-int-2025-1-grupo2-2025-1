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

df = pd.read_csv('dados_limpos.csv', encoding='utf-8')


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
df['Senioridade'] = df['Senioridade'].map(mapeamento_senioridade)


