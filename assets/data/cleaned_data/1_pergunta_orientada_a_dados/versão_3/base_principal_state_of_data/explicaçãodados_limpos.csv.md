## Análise do Processo de Limpeza de Dados: `dados_limpos.csv`

### Etapas de Limpeza de Dados 

O arquivo `dados_limpos.csv` apresenta dados estruturados sobre profissionais da área de dados no Brasil. As seguintes operações de limpeza e transformação foram provavelmente aplicadas:

**1. Seleção e Renomeação de Colunas**
Apenas colunas relevantes para a análise pretendida foram mantidas do dataset original. As colunas presentes em `dados_limpos.csv` foram renomeadas para nomes descritivos e padronizados em português, facilitando a compreensão e o uso. As colunas resultantes são:
*   `id`
*   `Nível de ensino alcançado`
*   `Área de formação acadêmica`
*   `Faixa salarial mensal`
*   `Tempo de experiência na área de dados`
*   `Nível de senioridade`
*   `Gênero do profissional`
*   `Cor/Raça/Etnia`
*   `Setor de atuação da empresa`
*   `UF onde mora`
*   `Cargo atual`
*   `Oportunidade de aprendizado`
*   `Reputação da empresa`

**2. Padronização de Dados Categóricos**
Valores dentro das colunas categóricas foram padronizados para garantir consistência. Exemplos observados em `dados_limpos.csv`:
*   **`Nível de ensino alcançado`**: Categorias como "Graduação/Bacharelado", "Mestrado", "Doutorado ou Phd", "Pós-graduação", "Estudante de Graduação".
*   **`Área de formação acadêmica`**: Consolidação de áreas, por exemplo, "Computação / Engenharia de Software / Sistemas de Informação/ TI" ou "Economia/ Administração / Contabilidade / Finanças/ Negócios". Respostas como "Outra opção" indicam o agrupamento de categorias menos frequentes ou a existência de uma opção para entradas não listadas.
*   **`Faixa salarial mensal`**: Formato consistente como "de R$ X/mês a R$ Y/mês" ou "Acima de R$ X/mês", "Menos de R$ X/mês".
*   **`Tempo de experiência na área de dados`**: Intervalos padronizados como "de 1 a 2 anos", "Menos de 1 ano".
*   **`Nível de senioridade`**: Termos como "Júnior", "Pleno", "Sênior".
*   **`Gênero do profissional`**: Categorias como "Masculino", "Feminino", "Outro", "Prefiro não informar".
*   **`Cor/Raça/Etnia`**: Padronização como "Branca", "Parda", "Preta", "Amarela", "Indígena", "Prefiro não informar".
*   **`Setor de atuação da empresa`**: Nomes de setores padronizados, como "Finanças ou Bancos", "Tecnologia/Fábrica de Software", e uma categoria "Outra Opção".
*   **`UF onde mora`**: Uso de siglas padronizadas para os estados brasileiros (ex: MG, SP, RJ).
*   **`Cargo atual`**: Consolidação e padronização de títulos de cargos, como "Cientista de Dados/Data Scientist" ou "Analista de BI/BI Analyst". A categoria "Outra Opção" também está presente.

**3. Transformação de Dados Booleanos/Binários**
As colunas `Oportunidade de aprendizado` e `Reputação da empresa` no arquivo `dados_limpos.csv` contêm valores numéricos `0.0` e `1.0`. As respostas originais  foram convertidas para um formato binário numérico, onde `1.0` pode representar uma afirmação positiva (ex: "Sim", "Importante") e `0.0` uma negativa ou ausência.

**4. Tratamento de Valores Ausentes (Missing Values)**
Embora a inspeção visual da amostra de `dados_limpos.csv` não revele imediatamente valores ausentes óbvios (como NaN), é uma etapa comum na limpeza de dados. O tratamento pode ter incluído:
*   Remoção de linhas onde dados cruciais estavam faltando.
*   Preenchimento de valores ausentes com uma categoria específica (ex: "Não informado", "Outra Opção", que aparecem em algumas colunas como `Cor/Raça/Etnia` ou `Gênero do profissional`) ou com a moda da coluna.
*   Para as colunas numéricas/binárias, ausências podem ter sido interpretadas como `0.0` ou um valor padrão.

**5. Codificação de Caracteres**
O arquivo `dados_limpos.csv` utiliza caracteres acentuados da língua portuguesa (ex: "Nível de ensino alcançado", "Computação"). Isso indica que o script de limpeza garantiu que os dados fossem lidos e salvos com uma codificação apropriada, como UTF-8.

**6. Manutenção de Identificadores Únicos**
A coluna `id` foi mantida, provavelmente servindo como um identificador único para cada registro no dataset.

### Conclusão
Em resumo, o processo de limpeza inferido transformou os dados brutos em um formato mais estruturado, consistente e pronto para análise, como observado no arquivo `dados_limpos.csv`. As operações incluíram seleção e renomeação de colunas, padronização de categorias, tratamento de valores booleanos e ausentes, limpeza de strings e garantia da correta codificação de caracteres.
