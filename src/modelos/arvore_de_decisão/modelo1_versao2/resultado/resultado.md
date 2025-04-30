Dataset Survey carregado. Shape: (4746, 36)

Dataset Microdados carregado. Shape: (27, 12)

Nomes das colunas do Survey (APÓS LIMPEZA REFINADA):

Verificando colunas selecionadas...
Coluna target encontrada: 'faixa_salarial'

Aviso: As seguintes features esperadas não foram encontradas após limpeza refinada: ['ccc', 'corracaoetnia', 'entre_as_linguagens_listadas_abaixo_qual_a_que_voce_mais_utiliza_no_trabalho']
  => Verifique a lista 'feature_columns_expected_clean' ou a função de limpeza.

Features válidas finais (32) a serem usadas: ['nivel_de_ensino', 'area_de_formacao', 'quanto_tempo_de_experiencia_na_area_de_dados_voce_tem', 'nivel', 'sql', 'r', 'python', 'net', 'java', 'julia', 'sasstata', 'visual_basicvba', 'scala', 'matlab', 'rust', 'php', 'javascript', 'nao_utilizo_nenhuma_linguagem', 'genero', 'setor', 'uf_onde_mora', 'cargo_atual', 'remuneracaosalario', 'beneficios', 'proposito_do_trabalho_e_da_empresa', 'flexibilidade_de_trabalho_remoto', 'ambiente_e_clima_de_trabalho', 'oportunidade_de_aprendizado_e_trabalhar_com_referencias_na_area', 'plano_de_carreira_e_oportunidades_de_crescimento_profissional', 'maturidade_da_empresa_em_termos_de_tecnologia_e_dados', 'qualidade_dos_gestores_e_lideres', 'reputacao_que_a_empresa_tem_no_mercado']
Shape inicial df_model: (4746, 33)

Removidas 0 linhas por não conseguir calcular 'salarymidpoint'.
Shape após tratar variável alvo: (4746, 34)

Tratando valores nulos...
Tratamento de nulos concluído.

Codificando variáveis categóricas CORRETAMENTE...
Verificando e aplicando OrdinalEncoder...
  Processando coluna ordinal: nivel_de_ensino
    Aviso: Categorias predefinidas não encontradas: ['graduacaobacharelado']
    Aviso: Categorias extras encontradas (serão -1): ['graduacao_bacharelado', 'prefiro_nao_informar']
    Ordem final usada: ['nao_tenho_graduacao_formal', 'estudante_de_graduacao', 'pos_graduacao', 'mestrado', 'doutorado_ou_phd']
  Processando coluna ordinal: quanto_tempo_de_experiencia_na_area_de_dados_voce_tem
    Aviso: Categorias extras encontradas (serão -1): ['de_5_a_6_anos']
    Ordem final usada: ['nao_tenho_experiencia_na_area_de_dados', 'menos_de_1_ano', 'de_1_a_2_anos', 'de_3_a_4_anos', 'de_4_a_6_anos', 'de_7_a_10_anos', 'mais_de_10_anos']
  Processando coluna ordinal: nivel
    Aviso: Categorias extras encontradas (serão -1): ['nan']
    Ordem final usada: ['junior', 'pleno', 'senior']

OrdinalEncoder aplicado com sucesso.

Aplicando One-Hot Encoding (get_dummies) nas colunas nominais (5).
Shape após One-Hot Encoding: (4746, 108)

Features finais para o modelo (106): ['nivel_de_ensino', 'quanto_tempo_de_experiencia_na_area_de_dados_voce_tem', 'nivel', 'sql', 'r', 'python', 'net', 'java', 'julia', 'sasstata', 'visual_basicvba', 'scala', 'matlab', 'rust', 'php', 'javascript', 'nao_utilizo_nenhuma_linguagem', 'remuneracaosalario', 'beneficios', 'proposito_do_trabalho_e_da_empresa', 'flexibilidade_de_trabalho_remoto', 'ambiente_e_clima_de_trabalho', 'oportunidade_de_aprendizado_e_trabalhar_com_referencias_na_area', 'plano_de_carreira_e_oportunidades_de_crescimento_profissional', 'maturidade_da_empresa_em_termos_de_tecnologia_e_dados', 'qualidade_dos_gestores_e_lideres', 'reputacao_que_a_empresa_tem_no_mercado', 'area_de_formacao_Ciências Biológicas/ Farmácia/ Medicina/ Área da Saúde', 'area_de_formacao_Ciências Sociais', 'area_de_formacao_Computação / Engenharia de Software / Sistemas de Informação/ TI', 'area_de_formacao_Economia/ Administração / Contabilidade / Finanças/ Negócios', 'area_de_formacao_Estatística/ Matemática / Matemática Computacional/ Ciências Atuariais', 'area_de_formacao_Marketing / Publicidade / Comunicação / Jornalismo', 'area_de_formacao_Outra opção', 'area_de_formacao_Outras Engenharias', 'area_de_formacao_Química / Física', 'area_de_formacao_nan', 'genero_Feminino', 'genero_Masculino', 'genero_Outro', 'genero_Prefiro não informar', 'setor_Agronegócios', 'setor_Educação', 'setor_Entretenimento ou Esportes', "setor_Filantropia/ONG's", 'setor_Finanças ou Bancos', 'setor_Indústria', 'setor_Internet/Ecommerce', 'setor_Marketing', 'setor_Outra Opção', 'setor_Seguros ou Previdência', 'setor_Setor Alimentício', 'setor_Setor Automotivo', 'setor_Setor Farmaceutico', 'setor_Setor Imobiliário/ Construção Civil', 'setor_Setor Público', 'setor_Setor de Energia', 'setor_Tecnologia/Fábrica de Software', 'setor_Telecomunicação', 'setor_Varejo', 'setor_Área da Saúde', 'setor_Área de Consultoria', 'uf_onde_mora_AL', 'uf_onde_mora_AM', 'uf_onde_mora_AP', 'uf_onde_mora_BA', 'uf_onde_mora_CE', 'uf_onde_mora_DF', 'uf_onde_mora_ES', 'uf_onde_mora_GO', 'uf_onde_mora_MA', 'uf_onde_mora_MG', 'uf_onde_mora_MS', 'uf_onde_mora_MT', 'uf_onde_mora_PA', 'uf_onde_mora_PB', 'uf_onde_mora_PE', 'uf_onde_mora_PI', 'uf_onde_mora_PR', 'uf_onde_mora_RJ', 'uf_onde_mora_RN', 'uf_onde_mora_RO', 'uf_onde_mora_RS', 'uf_onde_mora_SC', 'uf_onde_mora_SE', 'uf_onde_mora_SP', 'uf_onde_mora_TO', 'uf_onde_mora_nan', 'cargo_atual_Analista de BI/BI Analyst', 'cargo_atual_Analista de Dados/Data Analyst', 'cargo_atual_Analista de Inteligência de Mercado/Market Intelligence', 'cargo_atual_Analista de Negócios/Business Analyst', 'cargo_atual_Analista de Suporte/Analista Técnico', 'cargo_atual_Analytics Engineer', 'cargo_atual_Cientista de Dados/Data Scientist', 'cargo_atual_DBA/Administrador de Banco de Dados', 'cargo_atual_Data Product Manager/ Product Manager (PM/APM/DPM/GPM/PO)', 'cargo_atual_Desenvolvedor/ Engenheiro de Software/ Analista de Sistemas', 'cargo_atual_Economista', 'cargo_atual_Engenheiro de Dados/Arquiteto de Dados/Data Engineer/Data Architect', 'cargo_atual_Engenheiro de Machine Learning/ML Engineer/AI Engineer', 'cargo_atual_Estatístico', 'cargo_atual_Outra Opção', 'cargo_atual_Outras Engenharias (não inclui dev)', 'cargo_atual_Professor/Pesquisador', 'cargo_atual_nan']
Número final de features: 106

Shape de X: (4746, 106), Shape de y: (4746,)
Shapes: X_train: (3559, 106), X_test: (1187, 106), y_train: (3559,), y_test: (1187,)

Escalonando features...
Escalonamento concluído.

--- Treinamento e Otimização com GridSearchCV ---
Iniciando GridSearchCV...
Fitting 3 folds for each of 32 candidates, totalling 96 fits
[LightGBM] [Warning] Found whitespace in feature_names, replace with underlines
[LightGBM] [Info] Auto-choosing row-wise multi-threading, the overhead of testing was 0.002043 seconds.
You can set `force_row_wise=true` to remove the overhead.
And if memory is not enough, you can set `force_col_wise=true`.
[LightGBM] [Info] Total Bins 258
[LightGBM] [Info] Number of data points in the train set: 3559, number of used features: 82
[LightGBM] [Info] Start training from score 10000.500000
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
[LightGBM] [Warning] No further splits with positive gain, best gain: -inf
GridSearchCV concluído.

--- Avaliação do Modelo Otimizado ---
Melhores parâmetros: {'learning_rate': 0.05, 'max_depth': 10, 'min_child_samples': 30, 'n_estimators': 400, 'num_leaves': 31}

Desempenho no Teste:
MAE: R$ 3,336.52
RMSE: R$ 5,184.42
R²: 0.5747 (57.47%)

--- Interpretação do Modelo Otimizado ---

7.1 Importância Geral das Features (Gain):
![image](https://github.com/user-attachments/assets/5bc57622-8925-44b4-a4f5-52663b491c16)


7.2 Visualização de Árvore Individual (Exemplo: Árvore 0):
![image](https://github.com/user-attachments/assets/435d5c16-aaf4-495d-9fdb-c934473b28a8)




--- 7.3 Interpretação SHAP ---
Calculando SHAP values...
Cálculo SHAP concluído.

Plotando Resumo SHAP (dot)...
<ipython-input-1-db0d2f3ce3ee>:544: UserWarning: Tight layout not applied. The left and right margins cannot be made large enough to accommodate all Axes decorations.
  plt.tight_layout()
![image](https://github.com/user-attachments/assets/d4dd142c-6ae2-42a4-8238-7e150b17140a)


Plotando Resumo SHAP (bar)...
<ipython-input-1-db0d2f3ce3ee>:552: UserWarning: Tight layout not applied. The left and right margins cannot be made large enough to accommodate all Axes decorations.
  plt.tight_layout()

![image](https://github.com/user-attachments/assets/27eb071c-a17d-44c6-9daf-01608a027310)


Plotando SHAP Dependence Plots (exemplos)...

Plotando Dependência SHAP: 'quanto_tempo_de_experiencia_na_area_de_dados_voce_tem' vs Salário (colorido por 'nivel_de_ensino')
<Figure size 640x480 with 0 Axes>
  
![image](https://github.com/user-attachments/assets/05fad183-240e-47e5-9636-3c6a4d72395b)


Plotando Dependência SHAP: 'nivel' vs Salário (colorido por 'quanto_tempo_de_experiencia_na_area_de_dados_voce_tem')
<Figure size 640x480 with 0 Axes>
  
![image](https://github.com/user-attachments/assets/f33b65f8-a198-4195-b1fe-acd8260c0b4f)


Plotando Dependência SHAP: 'python' (Uso Python) vs Salário (colorido por 'quanto_tempo_de_experiencia_na_area_de_dados_voce_tem')
<Figure size 640x480 with 0 Axes>
  
![image](https://github.com/user-attachments/assets/405aa63e-9df2-4d77-ba1a-2def0db40259)


--- Fim da Análise ---
