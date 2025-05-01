# Resumo do Modelo Preditivo LightGBM

**Objetivo:** Prever se a experiência profissional de um profissional de dados no Brasil foi prejudicada devido à sua Cor/Raça/Etnia.

**Modelo Utilizado:** LightGBM (Light Gradient Boosting Machine)

**Variável Alvo:** `P1_e_2_Experiencia_prejudicada_devido_a_minha_Cor_Raça_Etnia` (1 = Sim, 0 = Não)

**Atributos (Features) Utilizados:**

*   Faixa etária (`P1_a_1_Faixa_idade`)
*   Gênero (`P1_b_Genero`)
*   Não acredita que a experiência profissional seja afetada (`P1_e_1_...`)
*   Experiência prejudicada devido à identidade de gênero (`P1_e_3_...`)
*   Nível de Ensino (`P1_l_Nivel_de_Ensino`)
*   Faixa Salarial (`P2_h_Faixa_salarial`)
*   Tempo de experiência prévia em TI/Engenharia (`P2_j_...`)

## Principais Resultados (Conjunto de Teste)

*   **Acurácia Global:** 92.65%

*   **Desempenho por Classe:**

    | Classe          | Precisão | Recall | F1-Score |
    |-----------------|----------|--------|----------|
    | 0 (Não Prej.)   | 0.94     | 0.97   | 0.95     |
    | 1 (Prejudicada) | 0.85     | 0.77   | 0.81     |

*   **Variáveis Mais Importantes:**
    1.  Gênero (`P1_b_Genero`)
    2.  Experiência prejudicada devido à identidade de gênero (`P1_e_3_...`)
    3.  Não acredita que a experiência profissional seja afetada (`P1_e_1_...`)
    4.  Tempo de Experiência Prévia em TI/Engenharia (`P2_j_...`)
    5.  Faixa Salarial (`P2_h_Faixa_salarial`)

## Conclusão Breve

O modelo LightGBM, treinado com os 7 atributos especificados, demonstrou boa capacidade preditiva (acurácia de 92.65%). Fatores relacionados a gênero (gênero do profissional e percepção de discriminação por identidade de gênero) foram os mais influentes nas previsões, seguidos por crenças sobre a neutralidade da experiência e fatores de carreira (tempo de experiência prévia, faixa salarial).
