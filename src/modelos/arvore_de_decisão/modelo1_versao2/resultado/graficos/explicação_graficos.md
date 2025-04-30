# Análise do Gráfico: Importância das Features (LightGBM Gain)
![image](https://github.com/user-attachments/assets/c980c7fc-97ca-416f-bcca-86a0293e724c)


**O que o Gráfico Mostra:**

Este gráfico é um **gráfico de barras horizontais** que visualiza a **importância das features** utilizadas pelo modelo LightGBM treinado para prever o salário (`salarymidpoint`). A importância aqui é medida pelo **"Gain"** (Ganho).

*   **Eixo Y (Vertical):** Lista os nomes das features (variáveis de entrada) que o modelo utilizou. Note que alguns nomes correspondem diretamente a colunas originais (como `nivel_de_ensino`, `nivel`, `python`, `sql`), enquanto outros são variáveis *dummy* criadas durante o pré-processamento para representar categorias específicas de colunas nominais (ex: `uf_onde_mora_SP`, `genero_Masculino`, `cargo_atual_Cientista_de_DadosData_Scientist`, `area_de_formacao_Computacao...`).
*   **Eixo X (Horizontal):** Representa a magnitude da "Importância (Gain)". Valores mais altos indicam que a feature foi mais importante para o modelo.
*   **Barras:** O comprimento de cada barra é proporcional à importância da feature correspondente.
*   **Ordenação:** As features estão ordenadas da mais importante (topo) para a menos importante (base), com base no valor do Gain. O gráfico exibe as 30 features mais importantes encontradas pelo modelo.

**Como Interpretar o "Gain":**

O "Gain" (Ganho) em modelos baseados em árvore como o LightGBM representa a **redução total na função de perda (erro) que é atribuída aos splits (divisões) feitos em uma determinada feature** em todas as árvores do modelo. Features que são usadas para fazer divisões mais eficazes (que separam melhor os dados em relação ao alvo) e/ou que são usadas com mais frequência terão um Gain total maior.

**Principais Observações e Tendências:**

1.  **Fatores Dominantes:**
    *   **`quanto_tempo_de_experiencia_na_area_de_dados_voce_tem` (Experiência):** É, de longe, a feature mais importante segundo o Gain, indicando que o tempo de experiência é o principal fator utilizado pelo modelo para diferenciar os salários.
    *   **`nivel_de_ensino` (Educação):** A segunda mais importante, mostrando o peso significativo da formação acadêmica nas previsões.
    *   **`nivel` (Senioridade):** A terceira mais importante, confirmando que o nível hierárquico (Júnior, Pleno, Sênior) é crucial para o modelo.
2.  **Fatores Contextuais Relevantes:**
    *   **`flexibilidade_de_trabalho_remoto`:** Surpreendentemente alta (4ª), esta é uma das features `P2o` (fatores de escolha de emprego). Sua alta importância *segundo o modelo* sugere que a presença (ou a valorização pelo respondente) deste fator está fortemente correlacionada com as faixas salariais previstas.
    *   **`uf_onde_mora_SP`:** A localização em São Paulo (5ª) se destaca como um importante diferenciador salarial nas previsões do modelo. A presença de `uf_onde_mora_MG` mais abaixo sugere que outras UFs também têm relevância, mas menor que SP.
    *   **`area_de_formacao_Computacao / Engenharia...`:** A área de formação específica (6ª) tem impacto considerável. Outras áreas (`Economia/Adm...`, `Outras Engenharias`) também aparecem, indicando que o background educacional influencia as previsões.
    *   **`plano_de_carreira...`, `oportunidade_de_aprendizado...`, `remuneracaosalario`, `beneficios`:** Outros fatores de escolha de emprego (`P2o`) também aparecem com importância moderada, sugerindo correlações entre essas preferências/condições e os salários previstos.
3.  **Habilidades Técnicas:**
    *   **`sql` (8ª) e `python` (9ª):** Confirmam sua importância como habilidades técnicas valorizadas e utilizadas pelo modelo para prever salários. A flag `nao_utilizo_nenhuma_linguagem` e a presença de `r` e `visual_basicvba` mais abaixo complementam essa visão.
4.  **Perfil Demográfico e Profissional:**
    *   **`genero_Masculino` (10ª):** Sua presença indica que o modelo encontrou uma associação entre este gênero e o salário previsto, em comparação com a(s) outra(s) categoria(s) de gênero.
    *   **`cargo_atual_...`:** Diversas categorias de cargo (Cientista de Dados, Engenheiro/Arquiteto, Analista de Dados, Analista de BI) aparecem na lista, mostrando que a função específica desempenhada é um fator relevante nas previsões.
    *   **`setor_...`:** Setores como Finanças/Bancos, Tecnologia e Indústria também são listados, indicando que a indústria de atuação influencia o salário previsto pelo modelo.

**Conclusão:**

O gráfico de importância baseado no Gain do LightGBM confirma que o modelo considera a **Experiência, Nível de Ensino e Senioridade** como os fatores mais decisivos para prever o salário. Além disso, fatores contextuais como **localização (SP), área de formação, cargo específico, setor e até mesmo preferências/condições de trabalho (flexibilidade, plano de carreira)**, juntamente com **habilidades técnicas (SQL, Python)** e **gênero**, são utilizados pelo modelo para refinar suas previsões.

É importante notar que o "Gain" é uma métrica de importância e não necessariamente indica causalidade direta. Ele reflete quais features o *modelo* achou mais úteis para reduzir seu erro de previsão durante o treinamento. A análise SHAP (nos outros gráficos gerados) fornece uma visão mais detalhada e robusta do impacto de cada feature.

---
# Análise da Árvore de Decisão (LightGBM - Árvore 0)
![image](https://github.com/user-attachments/assets/81b1b498-a7e8-40c5-aa2e-8cdc0655a2d0)

**O que o Gráfico Mostra:**

Este gráfico é a visualização da **primeira árvore de decisão (`tree_index=0`)** construída pelo modelo LightGBM treinado. O LightGBM é um modelo de *ensemble*, o que significa que ele combina as previsões de muitas árvores (neste caso, 400, conforme o hiperparâmetro `n_estimators` otimizado). Esta visualização nos permite entender a **lógica de decisão específica** desta árvore individual para chegar a uma previsão de salário (`salarymidpoint`).

*   **Nós (Nodes):**
    *   **Retângulos (Nós de Decisão/Split Nodes):** Representam pontos onde os dados são divididos com base em uma condição sobre uma feature específica.
    *   **Ovais (Nós Folha/Leaf Nodes):** Representam os pontos finais de um caminho na árvore. Contêm a previsão final do salário (`value`) para as amostras que chegam a essa folha.
*   **Setas/Ramos:** Indicam o caminho a seguir dependendo se a condição no nó de decisão é verdadeira ("yes") ou falsa ("no").

**Como Ler o Gráfico:**

1.  **Início (Nó Raiz):** A árvore começa no nó superior/esquerdo (o nó raiz), que contém a primeira condição de divisão aplicada a todos os dados de treinamento (3559 amostras neste caso).
2.  **Nós de Decisão (Retângulos):** Cada retângulo contém:
    *   **Condição:** A regra usada para dividir os dados (ex: `quanto_tempo_de_experiencia_na_area_de_dados_voce_tem <= 1.4`).
    *   **Gain:** A melhoria (redução no erro) alcançada por esta divisão específica. Quanto maior o `gain`, mais importante foi o split.
    *   **Value:** A previsão média de salário (`salarymidpoint`) para *todas* as amostras que chegam a este nó.
    *   **Count:** O número de amostras de treinamento que chegam a este nó.
3.  **Condições e Codificação:**
    *   **Variáveis Ordinais:** Features como `quanto_tempo_de_experiencia...`, `nivel_de_ensino`, `nivel` foram codificadas numericamente pelo `OrdinalEncoder` (preservando a ordem: 0, 1, 2,...). Por exemplo:
        *   `quanto_tempo... <= 1.4`: Separa quem tem "menos de 1 ano" (codificado como 1) ou "nenhuma experiência" (codificado como 0) dos demais.
        *   `nivel <= 0.7`: Separa "Júnior" (codificado como 0) dos demais (Pleno=1, Sênior=2).
        *   `nivel <= 1.1`: Separa "Júnior" (0) e "Pleno" (1) de "Sênior" (2).
    *   **Variáveis Dummy:** Features como `cargo_atual_Analista_de_BI_BI_Analyst`, `remuneracaosalario`, `flexibilidade_de_trabalho_remoto`, `python` (se for flag 0/1), `uf_onde_mora_SP` são binárias (0 ou 1). A condição `feature <= 0.0` geralmente significa que a amostra *não* pertence àquela categoria (valor 0), enquanto a condição não atendida (ramo "no") significa que a amostra *pertence* à categoria (valor 1).
4.  **Nós Folha (Ovais):**
    *   **Leaf X:** Identificador da folha.
    *   **Value:** A previsão final do `salarymidpoint` feita por *esta árvore específica* para as amostras que terminam nesta folha.
    *   **Count:** O número de amostras de treinamento que terminam nesta folha.

**Análise Detalhada da Lógica da Árvore 0:**

1.  **Primeiro Split (Raiz):** A divisão mais importante (maior `gain`: 670.8) é baseada na **Experiência** (`quanto_tempo... <= 1.4`). Isso separa profissionais com menos de ~2 anos de experiência (ramo "yes", 1083 amostras) daqueles com mais experiência (ramo "no", 2476 amostras). Isso confirma a alta importância geral da experiência vista no gráfico de Feature Importance.
2.  **Ramo "Baixa Experiência" (Experiencia <= 1.4):**
    *   A próxima divisão importante é por **Senioridade** (`nivel <= 0.7`), separando Juniores (ramo "yes") de Plenos/Seniores (ramo "no", embora poucos com baixa experiência devam ser seniores).
    *   Para os *Juniores com baixa experiência*, a árvore segue dividindo por **Cargo** (ex: `cargo_atual_Analista_de_BI... <= 0.0`), separando aqueles que são Analistas de BI dos que não são.
    *   As folhas neste ramo (ex: `leaf 0`, `leaf 3`) tendem a ter valores (`value`) de previsão salarial mais baixos (ex: 10200.5, 9675.5).
3.  **Ramo "Alta Experiência" (Experiencia > 1.4):**
    *   A próxima divisão é novamente por **Senioridade** (`nivel <= 1.1`), separando Plenos (ramo "yes") de Seniores (ramo "no").
    *   Para os *Seniores com alta experiência*, a árvore segue dividindo por um fator de escolha de emprego (`remuneracaosalario <= 0.0`), depois novamente por **Experiência** (`quanto_tempo... <= 3.4`, separando ~3-4 anos de mais tempo), e **Cargo** (`cargo_atual_Analista_de_Dados... <= 0.0`).
    *   Para os *Plenos com alta experiência*, a árvore divide por **Cargo** (ex: `cargo_atual_Cientista_de_Dados...`), **Nível de Ensino** (`nivel_de_ensino <= 0.0`), **Flexibilidade** (`flexibilidade_de_trabalho_remoto <= 0.0`), e novamente **Experiência**.
    *   As folhas neste ramo (ex: `leaf 1`, `leaf 2`, `leaf 15`, `leaf 28`) tendem a ter valores (`value`) de previsão salarial mais altos (ex: 10400.5, 10200.5, 10200.5, 14200.5).

**Principais Observações e Conclusões:**

*   **Hierarquia de Decisão:** Esta árvore específica prioriza a **Experiência** e a **Senioridade** para fazer as primeiras e mais impactantes divisões. Em seguida, utiliza o **Cargo Atual**, **Nível de Ensino**, e até **Fatores de Escolha de Emprego** e **Habilidades** (como `python`, visto mais abaixo) para refinar as previsões.
*   **Combinação de Fatores:** A árvore ilustra como o modelo não usa features isoladamente, mas sim em sequência para segmentar a população. O salário previsto em uma folha é resultado do caminho específico percorrido através dessas condições.
*   **Representatividade Limitada:** É **fundamental** lembrar que esta é apenas **uma árvore** dentre as 400 que compõem o modelo LightGBM final. Cada árvore pode aprender padrões ligeiramente diferentes.
*   **Previsão Final do Modelo:** A previsão final do LightGBM para uma nova amostra não é o valor de uma única folha, mas sim uma **média (ou média ponderada) das previsões de todas as 400 árvores**.
*   **Consistência:** A estrutura desta árvore (priorizando Experiência, Senioridade, Cargo) é consistente com os resultados gerais de importância das features, reforçando a validade desses fatores como preditores chave.

Este gráfico fornece um insight valioso sobre a mecânica interna do modelo, mostrando como ele aprendeu a combinar diferentes características para estimar os salários, mesmo que seja apenas um componente do ensemble final.

---
# Análise do Gráfico: SHAP Summary Plot (Dot / Beeswarm)
![image](https://github.com/user-attachments/assets/56abc66f-f506-40d6-9fa7-dc4f813ca873)


**O que o Gráfico Mostra:**

Este gráfico [1], conhecido como **SHAP Summary Plot do tipo "dot" (pontos)** ou "beeswarm plot", é uma ferramenta poderosa para visualizar o impacto das diferentes features (variáveis de entrada, como experiência, nível de ensino, etc.) nas previsões individuais do modelo LightGBM para o ponto médio da faixa salarial (`salarymidpoint`). Ele resume duas informações cruciais para cada feature em relação a cada profissional no conjunto de teste:

1.  **Magnitude e Direção do Impacto:** Quão fortemente e em que direção (positiva ou negativa) aquela feature influenciou a previsão de salário para um indivíduo específico.
2.  **Relação com o Valor da Feature:** Como o valor original da feature (alto ou baixo) se relaciona com seu impacto na previsão.

**Como Interpretar os Elementos do Gráfico:**

*   **Eixo Y Vertical (Features):**
    *   Lista as variáveis de entrada do modelo. As features estão ordenadas pela sua **importância média global** (calculada como a média do valor absoluto do SHAP para aquela feature em todas as amostras), com as mais importantes no topo.
    *   Inclui variáveis ordinais codificadas (`quanto_tempo_de_experiencia...`, `nivel`, `nivel_de_ensino`), flags binárias (`python`, `sql`, `remuneracaosalario`) e variáveis dummy criadas para categorias nominais (`uf_onde_mora_SP`, `genero_Masculino`, `cargo_atual_Analista de Dados/Data Analyst`, etc.).
*   **Eixo X Horizontal (Valor SHAP - Impacto no Resultado do Modelo):**
    *   Mostra o **valor SHAP** calculado para uma feature específica em uma previsão específica. Este valor representa a contribuição (em Reais, na escala do `salarymidpoint`) daquela feature para deslocar a previsão da média base do modelo.
    *   **Valores Positivos (> 0):** Indicam que o valor daquela feature para aquele profissional **aumentou** a previso de salrio.
    *   **Valores Negativos (< 0):** Indicam que o valor daquela feature **diminuiu** a previso de salrio.
    *   **Valor Zero (= 0.0):** A linha vertical central marca o ponto onde a feature não teve impacto naquela previsão específica.
*   **Pontos Coloridos (Beeswarm):**
    *   **Cada ponto** no gráfico representa o valor SHAP de **uma feature específica** para **um profissional específico** no conjunto de teste.
    *   A **posição horizontal** do ponto mostra o valor SHAP (o impacto) da feature correspondente (eixo Y) para aquele profissional.
    *   A **dispersão vertical** dentro de cada linha de feature serve apenas para visualização, mostrando a densidade dos pontos e evitando sobreposição total.
    *   A **cor do ponto** representa o **valor original da feature** para aquele profissional, conforme a escala da barra de cores à direita:
        *   **Vermelho (High):** Indica um valor **alto** da feature (ex: muitos anos de experiência, nível 'Sênior', nível de ensino 'Doutorado', usa Python=1, mora em SP=1).
        *   **Azul (Low):** Indica um valor **baixo** da feature (ex: pouca experiência, nível 'Júnior', nível de ensino 'Graduação', não usa Python=0, não mora em SP=0).

**Análise Detalhada dos Achados Visuais no Gráfico (Principais Features):**

1.  **`quanto_tempo_de_experiencia...` (Experiência):**
    *   **Padrão:** Feature mais importante (topo). Há uma clara separação horizontal: pontos vermelhos (alta experiência) estão concentrados à direita (SHAP > 0, chegando a +6000), enquanto pontos azuis (baixa experiência) estão concentrados à esquerda (SHAP < 0, chegando a -4000).
    *   **Conclusão:** A experiência tem um impacto muito forte e consistentemente positivo no salário previsto. Quanto maior a experiência, maior o aumento previsto.
2.  **`nivel` (Senioridade):**
    *   **Padrão:** Segunda mais importante. Padrão similar à experiência: pontos vermelhos (Sênior) à direita (SHAP positivo, +3000 a +5000), pontos azuis (Júnior) à esquerda (SHAP negativo, -2000 a -4000). Pontos roxos (Pleno) ficam mais ao centro, em torno de SHAP=0.
    *   **Conclusão:** A senioridade tem um impacto forte e claro. Ser Sênior aumenta significativamente a previsão, enquanto ser Júnior a diminui substancialmente.
3.  **`nivel_de_ensino` (Educação):**
    *   **Padrão:** Terceira mais importante. Há uma tendência visível: pontos vermelhos/roxos (níveis mais altos como Mestrado/Doutorado) tendem a ter SHAP mais alto (mais à direita, +1000 a +2000) do que os pontos azuis (níveis mais baixos como Graduação/Estudante), que têm SHAP negativo ou próximo de zero.
    *   **Conclusão:** Níveis mais altos de educação formal têm um impacto geralmente positivo, embora menos intenso que experiência ou senioridade.
4.  **`uf_onde_mora_SP` (Localização SP):**
    *   **Padrão:** Quarta mais importante. Sendo uma dummy binária: pontos vermelhos (mora em SP = 1) estão majoritariamente à direita (SHAP positivo, até +2000), enquanto pontos azuis (não mora em SP = 0) estão concentrados à esquerda (SHAP negativo).
    *   **Conclusão:** Residir em São Paulo, conforme capturado pelo modelo, está associado a um aumento na previsão salarial em comparação com outras UFs (representadas pelo valor 0).
5.  **`genero_Masculino` (Gênero):**
    *   **Padrão:** Quinta mais importante. Dummy binária: pontos vermelhos (Masculino = 1) mostram uma leve tendência para a direita (SHAP ligeiramente positivo), enquanto pontos azuis (Feminino/Outro = 0) mostram uma leve tendência para a esquerda (SHAP ligeiramente negativo).
    *   **Conclusão:** O modelo associa o gênero masculino a um pequeno aumento na previsão salarial em relação aos outros gêneros presentes no dataset. *Importante: Isso reflete uma correlação encontrada pelo modelo nos dados, não necessariamente uma prova de causalidade ou discriminação direta sem análise mais profunda.*
6.  **Cargos Atuais (`cargo_atual_...`):**
    *   **Padrão:** Várias dummies de cargos aparecem com importância relevante (Analista de Dados, Engenheiro de Dados, Analista de BI, Cientista de Dados, Engenheiro de ML). Para cada um:
        *   Pontos vermelhos (é aquele cargo = 1) mostram seu impacto típico. Ex: `Engenheiro de Dados` parece ter SHAP positivo; `Analista de BI` parece ter SHAP negativo.
        *   Pontos azuis (não é aquele cargo = 0) tendem a se agrupar perto de SHAP=0 para *aquela feature dummy específica*.
    *   **Conclusão:** O cargo específico ocupado é um fator importante que diferencia os salários previstos.
7.  **Habilidades Técnicas (`python`, `sql`, `scala`, `visual_basicvba`, `nao_utilizo_nenhuma_linguagem`):**
    *   **Padrão:** `python` (17ª) e `sql` (27ª) mostram pontos vermelhos (usa=1) tendendo para a direita (SHAP positivo), e azuis (não usa=0) perto de zero ou à esquerda. `scala` e `visual_basicvba` também mostram algum impacto positivo para quem os usa. `nao_utilizo_nenhuma_linguagem` mostra pontos vermelhos (não usa nenhuma=1) claramente à esquerda (SHAP negativo).
    *   **Conclusão:** Usar Python e SQL tem impacto positivo na previsão. Não usar nenhuma linguagem tem impacto negativo. Scala e VBA parecem agregar valor em nichos específicos capturados pelo modelo.
8.  **Outros Fatores (Formação, Setor, Fatores de Escolha):**
    *   Features como `area_de_formacao_Computacao...`, `setor_Financas...`, `remuneracaosalario`, `plano_de_carreira...` também aparecem, indicando que o background educacional, a indústria e até as prioridades do profissional na escolha do emprego estão correlacionadas com o salário previsto pelo modelo, embora com menor impacto médio que os fatores principais.

**Conclusão Geral:**

O SHAP Summary Plot (Dot) fornece uma visão rica e detalhada de como o modelo LightGBM utiliza as informações para prever salários. Ele confirma visualmente a **dominância da Experiência e Senioridade**, seguidas por **Educação, Localização (SP), Gênero e Cargo** como os fatores de maior impacto médio. Habilidades como **Python e SQL** também demonstram impacto positivo consistente. O gráfico revela não apenas a importância geral, mas também a **direção e a variabilidade do impacto** de cada feature para diferentes indivíduos, baseado em seus valores específicos (alto/baixo).

---
# Análise do Gráfico: SHAP Summary Plot (Bar)
![image](https://github.com/user-attachments/assets/e4dd86f2-651c-46bf-9610-67bf0bc76e57)


**O que o Gráfico Mostra:**

Este gráfico [1] é um **SHAP Summary Plot do tipo "bar" (barras)**. Sua função principal é ranquear as features (variáveis de entrada) de acordo com a **magnitude média do seu impacto** nas previsões do modelo LightGBM para o `salarymidpoint`. Diferente do gráfico de pontos (dot plot / beeswarm), este foca apenas na **importância geral** de cada feature, calculada como a média do valor absoluto do SHAP para aquela feature em todas as amostras do conjunto de teste. Ele não mostra a direção (positiva/negativa) ou a distribuição dos impactos individuais.

**Como Interpretar os Elementos do Gráfico:**

*   **Eixo Y Vertical (Features):**
    *   Lista as variáveis de entrada do modelo, ordenadas pela sua importância média global (da mais importante no topo para a menos importante na base).
    *   Inclui variáveis ordinais codificadas (`quanto_tempo_de_experiencia...`, `nivel`, `nivel_de_ensino`), flags binárias (`python`, `sql`, `remuneracaosalario`, `genero_Masculino`) e variáveis dummy criadas para categorias nominais (`uf_onde_mora_SP`, `cargo_atual_Analista de Dados/Data Analyst`, `setor_Financas ou Bancos`, etc.).
*   **Eixo X Horizontal (`mean(|SHAP value|) (average impact on model output magnitude)`):**
    *   Mostra o **valor médio absoluto do SHAP** para cada feature. Isso representa, em média, o quanto o valor daquela feature (seja ele alto ou baixo) desloca a predição do modelo da média base, independentemente da direção.
    *   Valores maiores no eixo X indicam que a feature, em média, tem um impacto maior (seja positivo ou negativo) nas previsões salariais.
*   **Barras Azuis:**
    *   O comprimento de cada barra é diretamente proporcional ao valor médio absoluto do SHAP para a feature correspondente.
    *   **Barras mais longas indicam maior importância média global** da feature para o modelo.

**Análise Detalhada do Ranking de Importância:**

O gráfico confirma a ordem de importância observada no SHAP Summary Plot (dot), destacando quantitativamente a magnitude média do impacto:

1.  **`quanto_tempo_de_experiencia...` (Experiência):** A feature mais importante, com a barra mais longa, indicando que, em média, a experiência tem o maior impacto absoluto nas previsões salariais (`mean(|SHAP value|) ≈ 2700`).
2.  **`nivel` (Senioridade):** A segunda feature mais importante, com um impacto médio absoluto significativo, mas menor que a experiência (`mean(|SHAP value|) ≈ 2200`).
3.  **`nivel_de_ensino` (Educação):** Terceira mais importante, mostrando que a formação acadêmica tem um impacto médio relevante (`mean(|SHAP value|) ≈ 1100`).
4.  **`uf_onde_mora_SP` (Localização SP):** A dummy indicando residência em São Paulo é a quarta mais importante, sugerindo um impacto médio considerável da localização (`mean(|SHAP value|) ≈ 700`).
5.  **`genero_Masculino` (Gênero):** Quinta mais importante, indicando que esta variável dummy tem um impacto médio notável nas previsões do modelo (`mean(|SHAP value|) ≈ 600`).
6.  **`cargo_atual_Analista de Dados/Data Analyst`:** O cargo específico aparece como sexto, com impacto médio similar ao gênero (`mean(|SHAP value|) ≈ 550`).
7.  **`remuneracaosalario` (Fator de Escolha P2o1):** A importância dada à remuneração ao escolher um emprego tem um impacto médio relevante (`mean(|SHAP value|) ≈ 500`).
8.  **Cargos e Contexto:** Seguem-se outras dummies de cargo (`Engenheiro de Dados...`, `Analista de BI...`, `Cientista de Dados...`), a dummy indicando UF não preenchida (`uf_onde_mora_nan` - interessante!), dummies de setor (`Financas...`, `Tecnologia...`) e a linguagem `scala`. Todas com impacto médio decrescente, mas ainda presente.
9.  **Formação, Habilidades e Outros Fatores:** Mais abaixo, aparecem áreas de formação (`Computacao...`, `Economia...`, `Outras Engenharias`), outras preferências de trabalho (`plano_de_carreira...`, `beneficios`, `oportunidade_de_aprendizado...`, `flexibilidade_...`), habilidades (`python`, `nao_utilizo_nenhuma_linguagem`, `visual_basicvba`, `sql`), e características da empresa (`maturidade_...`, `qualidade_dos_gestores...`). Estas têm um impacto médio absoluto menor, mas ainda contribuem para o modelo.

**Conclusão Geral:**

O SHAP Summary Plot (Bar) oferece um ranking claro da **influência média geral** das features no modelo de previsão salarial. Ele confirma que **Experiência, Senioridade e Nível de Ensino** são os fatores com maior poder preditivo médio, seguidos de perto por **Localização (SP), Gênero e Cargo**. O gráfico quantifica essa importância relativa através do `mean(|SHAP value|)`. Embora não mostre a direção do impacto (como o dot plot), ele é útil para rapidamente identificar quais variáveis o modelo mais considera ao fazer suas previsões.


---
# Análise do Gráfico: SHAP Dependence Plot - Experiência vs. Educação
![image](https://github.com/user-attachments/assets/08eb5af5-e46d-4c11-9418-00221d6d5531)


**O que o Gráfico Mostra:**

Este gráfico [1] é um **SHAP Dependence Plot**, uma das visualizações mais importantes para entender as **interações** entre as features no modelo LightGBM. Especificamente, este gráfico mostra:

1.  **O impacto da feature principal (`quanto_tempo_de_experiencia_na_area_de_dados_voce_tem`) no salário previsto:** Como diferentes níveis de experiência influenciam o valor SHAP (a contribuição da *experiência* para a previsão final do `salarymidpoint`).
2.  **A interação com uma segunda feature (`nivel_de_ensino`):** Como o nível de ensino do profissional (representado pela cor) modifica o impacto da experiência no salário.

Ele utiliza os resultados do modelo treinado e os dados do conjunto de teste para ilustrar essas relações complexas.

**Como Interpretar os Elementos do Gráfico:**

*   **Eixo X Horizontal (`quanto_tempo_de_experiencia_na_area_de_dados_voce_tem`):**
    *   Representa a feature principal: **Tempo de Experiência** na área de dados.
    *   Os rótulos no eixo (`nao_tenho_experiencia...`, `menos_de_1_ano`, ..., `mais_de_10_anos`) são as categorias originais desta variável (após a limpeza de texto). O `OrdinalEncoder` transformou essas categorias em valores numéricos (0, 1, 2, ...) para o modelo, mas o gráfico exibe os rótulos originais para melhor legibilidade.
*   **Eixo Y Vertical (`SHAP value for quanto_tempo_de_experiencia...`):**
    *   Mostra o **valor SHAP** associado à feature *Tempo de Experiência* para cada profissional no conjunto de teste.
    *   Representa o **impacto (em Reais)** que o nível de experiência daquele profissional teve na previsão final do seu `salarymidpoint`, comparado à previsão média base do modelo.
    *   **Valores Positivos (> 0):** A experiência daquele profissional **aumentou** a previsão salarial.
    *   **Valores Negativos (< 0):** A experiência daquele profissional **diminuiu** a previsão salarial.
*   **Pontos Coloridos:**
    *   Cada ponto representa **um profissional** no conjunto de teste.
    *   Sua **posição horizontal** indica sua categoria de tempo de experiência.
    *   Sua **posição vertical** indica o impacto SHAP dessa experiência no seu salário previsto.
*   **Cor dos Pontos (`nivel_de_ensino` - Barra de Cores à Direita):**
    *   A cor representa o valor da feature de **interação: Nível de Ensino**.
    *   **Importante:** Os valores na barra de cores (-1.000 a 4.000) são os **valores numéricos codificados pelo `OrdinalEncoder`** para o Nível de Ensino. É necessário consultar o mapeamento usado no código para entender o significado exato:
        *   `-1.000` (ou próximo): Provavelmente 'Desconhecido' ou valor não mapeado.
        *   `0.000` (Azul escuro): 'nao_tenho_graduacao_formal'.
        *   `0.667` a `1.500` (Azul claro/Ciano): 'estudante_de_graduacao', 'graduacaobacharelado'.
        *   `~2.333` (Roxo): 'pos_graduacao'.
        *   `~3.167` (Magenta): 'mestrado'.
        *   `4.000` (Vermelho): 'doutorado_ou_phd' (ou o nível mais alto codificado).
    *   A escala de cores vai do **Azul (Low - Baixo Nível de Ensino)** para o **Vermelho (High - Alto Nível de Ensino)**.

**Análise Detalhada dos Padrões e Interações Visíveis:**

1.  **Efeito Principal da Experiência (Tendência Geral):**
    *   Há uma clara tendência **positiva** entre o tempo de experiência (eixo X) e seu impacto no salário (eixo Y).
    *   Profissionais com "nenhuma experiência" ou "menos de 1 ano" têm um impacto SHAP **negativo** (reduzem a previsão salarial, valores entre -2000 e -4000).
    *   À medida que a experiência aumenta (`de_1_a_2_anos` em diante), o impacto SHAP se torna progressivamente **mais positivo**, chegando a valores altos (acima de +4000 a +6000) para aqueles com "mais de 10 anos".
    *   Isso confirma que a experiência é um forte preditor positivo do salário.
2.  **Efeito da Interação com Educação (Cor dos Pontos):**
    *   Observe a dispersão vertical dos pontos dentro de cada categoria de experiência (a partir de `de_1_a_2_anos`).
    *   **Padrão Chave:** Dentro de uma mesma faixa de experiência, os pontos **vermelhos e roxos** (representando níveis de ensino mais altos como Mestrado, Doutorado, Pós) estão consistentemente **acima** (maior valor SHAP) dos pontos **azuis** (representando níveis de ensino mais baixos como Graduação, Estudante).
    *   **Significado:** Para um *mesmo nível de experiência*, possuir um nível de educação formal mais elevado resulta em um **impacto positivo adicional** (ou um impacto negativo menor) no salário previsto pelo modelo.
    *   **Exemplo:** Compare os pontos em `de_7_a_10_anos`. Os pontos azuis (baixa educação) têm SHAP entre +2000 e +4000, enquanto os pontos vermelhos/roxos (alta educação) têm SHAP entre +4000 e +6000.

**Conclusão Geral:**

Este SHAP Dependence Plot revela uma interação importante aprendida pelo modelo:

*   O **tempo de experiência** tem um forte impacto positivo crescente no salário previsto.
*   Esse impacto positivo da experiência é **potencializado** ou **amplificado** pelo **nível de educação**. O "retorno" financeiro de anos adicionais de experiência é maior para aqueles com maior qualificação acadêmica (Mestrado, Doutorado, Pós-Graduação).

O modelo não apenas identificou que ambas as features são importantes individualmente, mas também que elas interagem de forma sinérgica para influenciar o salário final previsto.


---
# Análise do Gráfico: SHAP Dependence Plot - Senioridade vs. Experiência
![image](https://github.com/user-attachments/assets/d1d9367f-a60f-4eb2-a7c2-c1ad7242e916)


**O que o Gráfico Mostra:**

Este gráfico [1] é um **SHAP Dependence Plot**, focado em visualizar a relação entre a **Senioridade (`nivel`)** e seu impacto na previsão de salário (`salarymidpoint`), além de mostrar como essa relação é influenciada pela **Experiência** (`quanto_tempo_de_experiencia_na_area_de_dados_voce_tem`). Ele utiliza os resultados do modelo LightGBM treinado e os dados do conjunto de teste.

**Como Interpretar os Elementos do Gráfico:**

*   **Eixo X Horizontal (`nivel`):**
    *   Representa a feature principal: **Nível de Senioridade**.
    *   Os rótulos `junior`, `pleno`, `senior` correspondem às categorias desta variável. O `OrdinalEncoder` usado no código transformou essas categorias em valores numéricos (provavelmente 0, 1, 2), que são usados internamente pelo modelo, mas o gráfico exibe os rótulos originais para clareza.
*   **Eixo Y Vertical (`SHAP value for nivel`):**
    *   Mostra o **valor SHAP** associado à feature *Nível de Senioridade* para cada profissional no conjunto de teste.
    *   Representa o **impacto (em Reais)** que o nível de senioridade daquele profissional teve na previsão final do seu `salarymidpoint`, comparado à previsão média base do modelo.
    *   **Valores Positivos (> 0):** A senioridade daquele profissional **aumentou** a previsão salarial.
    *   **Valores Negativos (< 0):** A senioridade daquele profissional **diminuiu** a previsão salarial.
*   **Pontos Coloridos:**
    *   Cada ponto representa **um profissional** no conjunto de teste.
    *   Sua **posição horizontal** indica seu nível de senioridade.
    *   Sua **posição vertical** indica o impacto SHAP dessa senioridade no seu salário previsto.
*   **Cor dos Pontos (`quanto_tempo_de_experiencia...` - Barra de Cores à Direita):**
    *   A cor representa o valor da feature de **interação: Tempo de Experiência**.
    *   **Importante:** Os valores na barra de cores (-1.000 a 6.000) são os **valores numéricos codificados pelo `OrdinalEncoder`** para o Tempo de Experiência. É necessário consultar o mapeamento usado no código para entender o significado exato:
        *   `-1.000` (ou próximo): Provavelmente 'Desconhecido' ou valor não mapeado.
        *   `0.000` (Azul escuro): 'nao_tenho_experiencia_na_area_de_dados'.
        *   `0.750` a `1.625` (Azul claro): 'menos_de_1_ano', 'de_1_a_2_anos'.
        *   `2.500` a `4.250` (Ciano/Roxo): 'de_3_a_4_anos', 'de_4_a_6_anos' (ou 'de_5_a_6_anos').
        *   `5.125` a `6.000` (Magenta/Vermelho): 'de_7_a_10_anos', 'mais_de_10_anos' (ou o nível mais alto codificado).
    *   A escala de cores vai do **Azul (Low - Baixa Experiência)** para o **Vermelho (High - Alta Experiência)**.

**Análise Detalhada dos Padrões e Interações Visíveis:**

1.  **Efeito Principal da Senioridade (Eixo X vs. Eixo Y):**
    *   Há uma clara separação vertical do impacto SHAP com base no nível de senioridade:
        *   **`junior`:** Os pontos estão concentrados em valores SHAP **fortemente negativos** (principalmente entre -2500 e -5000). Ser júnior diminui consideravelmente a previsão salarial.
        *   **`pleno`:** Os pontos estão agrupados mais próximos de SHAP=0, com alguma dispersão (talvez -1000 a +1500). Ser pleno tem um impacto mais neutro ou ligeiramente positivo/negativo dependendo de outros fatores.
        *   **`senior`:** Os pontos estão concentrados em valores SHAP **fortemente positivos** (principalmente entre +1500 e +3000). Ser sênior aumenta consideravelmente a previsão salarial.
    *   **Conclusão:** Existe uma relação positiva muito forte e clara entre o nível de senioridade e seu impacto no salário previsto.
2.  **Efeito da Interação com Experiência (Cor dos Pontos dentro de cada Nível):**
    *   Observe a distribuição vertical das cores *dentro* de cada categoria de senioridade:
        *   **`junior`:** Mesmo entre os juniores (impacto negativo), os pontos **vermelhos/roxos** (mais experiência) estão **acima** (SHAP menos negativo) dos pontos **azuis** (menos experiência, SHAP mais negativo).
        *   **`pleno`:** O mesmo padrão é observado. Pontos **vermelhos/roxos** estão consistentemente **acima** dos pontos **azuis**.
        *   **`senior`:** Novamente, pontos **vermelhos/roxos** estão **acima** dos pontos **azuis**.
    *   **Significado:** Para um *mesmo nível de senioridade*, possuir mais **tempo de experiência** resulta em um **impacto positivo adicional** (ou um impacto negativo menor) no salário previsto pelo modelo.
    *   **Exemplo:** Entre os Seniores, aqueles com mais experiência (vermelho) têm um SHAP value mais alto (ex: +2500 a +3000) do que aqueles com menos experiência (azul, talvez +1500 a +2500).

**Conclusão Geral:**

Este SHAP Dependence Plot revela uma interação significativa entre Senioridade e Experiência:

*   O **nível de senioridade** tem um impacto direto e forte no salário previsto (negativo para Júnior, neutro/positivo para Pleno, fortemente positivo para Sênior).
*   O **tempo de experiência** atua como um **amplificador** desse impacto. Para qualquer nível de senioridade, ter mais experiência aumenta o valor SHAP associado (torna o impacto mais positivo ou menos negativo).

O modelo aprendeu que não basta ser Sênior; ser um Sênior *com mais experiência* resulta no maior impulso salarial previsto, e ser um Júnior *com pouca experiência* resulta na maior penalidade prevista, em comparação com a média. Esta interação sinérgica é um fator chave na determinação do salário previsto pelo modelo.


---
# Análise do Gráfico: SHAP Dependence Plot - Uso de Python vs. Experiência
![image](https://github.com/user-attachments/assets/8115ba39-9c49-4a10-98ac-38d42a0478b6)


**O que o Gráfico Mostra:**

Este gráfico [1] é um **SHAP Dependence Plot**, desenhado para visualizar duas relações importantes sobre o modelo LightGBM treinado:

1.  **O impacto da feature principal (`python` - Uso de Python) no salário previsto:** Como saber/usar Python (valor 0 para "Não Usa" ou 1 para "Usa") influencia o valor SHAP (a contribuição dessa habilidade para a previsão final do `salarymidpoint`).
2.  **A interação com uma segunda feature (`quanto_tempo_de_experiencia_na_area_de_dados_voce_tem`):** Como o tempo de experiência do profissional (representado pela cor) modifica o impacto do uso de Python no salário.

Ele utiliza os resultados do modelo treinado e os dados do conjunto de teste para ilustrar essas relações.

**Como Interpretar os Elementos do Gráfico:**

*   **Eixo X Horizontal (`python`):**
    *   Representa a feature principal: **Uso de Python**.
    *   Os pontos estão concentrados em duas posições:
        *   **"Não Usa" (correspondendo ao valor 0.0):** O profissional não usa Python.
        *   **"Usa" (correspondendo ao valor 1.0):** O profissional usa Python.
*   **Eixo Y Vertical (`SHAP value for python`):**
    *   Mostra o **valor SHAP** associado à feature *Uso de Python* para cada profissional no conjunto de teste.
    *   Representa o **impacto (em Reais)** que usar ou não Python teve na previsão final do `salarymidpoint` daquele profissional, em comparação com a previsão média base do modelo.
    *   **Valores Positivos (> 0):** O uso (ou não uso) de Python **aumentou** a previsão salarial.
    *   **Valores Negativos (< 0):** O uso (ou não uso) de Python **diminuiu** a previsão salarial.
*   **Pontos Coloridos:**
    *   Cada ponto representa **um profissional** no conjunto de teste.
    *   Sua **posição horizontal** indica se ele usa ou não Python.
    *   Sua **posição vertical** indica o impacto SHAP dessa informação no seu salário previsto.
*   **Cor dos Pontos (`quanto_tempo_de_experiencia...` - Barra de Cores à Direita):**
    *   A cor representa o valor da feature de **interação: Tempo de Experiência**.
    *   **Importante:** Os valores na barra de cores (-1.000 a 6.000) são os **valores numéricos codificados pelo `OrdinalEncoder`** para o Tempo de Experiência. A escala vai do **Azul (Low - Baixa Experiência)** para o **Vermelho (High - Alta Experiência)**:
        *   `-1.000` (Azul escuro inferior): 'Desconhecido' ou não mapeado.
        *   `0.000` a `~1.625` (Azul/Ciano): Baixa experiência ('Não tenho', 'Menos de 1 ano', '1-2 anos').
        *   `~2.500` a `~4.250` (Roxo): Experiência intermediária ('3-4 anos', '4-6 anos').
        *   `~5.125` a `6.000` (Magenta/Vermelho): Alta experiência ('7-10 anos', 'Mais de 10 anos').

**Análise Detalhada dos Padrões e Interações Visíveis:**

1.  **Efeito Principal do Uso de Python (Comparação Horizontal):**
    *   **"Não Usa" (X=0):** Os pontos se concentram principalmente em valores SHAP **negativos** (entre 0 e -450), embora haja alguns pontos com SHAP próximo de zero ou ligeiramente positivo. Isso sugere que *não* usar Python geralmente diminui a previsão salarial.
    *   **"Usa" (X=1):** Os pontos se concentram principalmente em valores SHAP **próximos de zero ou positivos** (entre -50 e +200). Isso sugere que *usar* Python geralmente aumenta (ou pelo menos não diminui) a previsão salarial.
    *   **Conclusão:** Há uma clara diferença vertical entre os dois grupos. Usar Python (X=1) está associado a um impacto SHAP mais alto (mais positivo ou menos negativo) do que não usar Python (X=0).
2.  **Efeito da Interação com Experiência (Cor dos Pontos dentro de "Usa"):**
    *   **Foco em "Usa" (X=1):** Observe a distribuição vertical das cores neste cluster.
        *   Os pontos com **maior impacto positivo** (SHAP entre +50 e +200) são predominantemente **vermelhos ou magenta** (indicando **alta experiência**).
        *   Os pontos com impacto próximo de zero ou ligeiramente negativo (SHAP entre -50 e +50) são predominantemente **azuis ou ciano** (indicando **baixa experiência**).
    *   **Significado:** Para os profissionais que *usam Python*, aqueles com **mais experiência** recebem um "impulso" salarial previsto (valor SHAP positivo) significativamente maior devido a essa habilidade do que aqueles com menos experiência.
3.  **Interação em "Não Usa" (X=0):** O padrão de cores aqui é menos distinto. Embora haja pontos azuis e vermelhos em toda a faixa de SHAP negativo, não há uma separação tão clara quanto no grupo "Usa". Isso pode indicar que o impacto negativo de *não* usar Python é menos sensível à experiência, ou que outras interações dominam nesse subgrupo.
4.  **Outliers:** Existem alguns pontos isolados com SHAP muito positivo (>150) mesmo para quem "Não Usa" Python, e alguns com SHAP negativo (< -100) para quem "Usa". Estes podem representar casos individuais onde outras features tiveram um impacto dominante e incomum.

**Conclusão Geral:**

Este SHAP Dependence Plot demonstra uma interação importante entre o uso de Python e o tempo de experiência:

*   **Usar Python** está associado a um impacto geralmente positivo (ou menos negativo) no salário previsto, em comparação com não usar.
*   O **benefício salarial** previsto por usar Python é significativamente **amplificado pelo tempo de experiência**. Profissionais mais experientes que usam Python veem um aumento maior em sua previsão salarial atribuído a essa habilidade, enquanto para profissionais menos experientes, o impacto positivo de usar Python é menor.

O modelo aprendeu que a combinação de **saber Python E ter mais experiência** é particularmente valiosa no mercado de dados, resultando em previsões salariais mais altas.

