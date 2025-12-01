Weather Launch Forecast – IA aplicada a janelas de lançamento espacial

Este repositório contém o código, dados e documentação do projeto Predição de Janelas de Lançamento Espacial a partir de Condições Meteorológicas com Modelos de Aprendizado de Máquina, desenvolvido no Programa de Capacitação em Inteligência Artificial Aplicada ao Setor Aeroespacial – Instituto HBR.

Objetivo do projeto

Desenvolver um modelo de aprendizado de máquina capaz de prever, com até 48 horas de antecedência, a viabilidade de uma janela de lançamento espacial com base em variáveis meteorológicas extraídas do conjunto ERA5, integradas a dados históricos de missões.

O objetivo final é apoiar decisões de go/no-go, reduzindo riscos e impactos operacionais associados a lançamentos adiados.

Visão geral da solução

O pipeline inclui:

Coleta de dados de lançamentos espaciais

Extração de variáveis meteorológicas ERA5

Engenharia de atributos

Treinamento de modelos supervisionados

Regressão Logística

Gradient Boosting

XGBoost

Avaliação temporal (time-split)

Interpretação dos modelos via SHAP

Geração do artigo final

O Gradient Boosting apresentou o melhor desempenho geral.

Principais variáveis meteorológicas utilizadas

velocidade do vento

rajadas máximas

precipitação acumulada

tendência da pressão

cobertura de nuvens

📂 Estrutura do repositório
src/
    modeling.ipynb
data/
    README.md
docs/
    artigo_final.pdf
README.md
requirements.txt

Obtenção dos dados ERA5

Os dados meteorológicos utilizados foram extraídos do ERA5 via Climate Data Store (CDS):

https://cds.climate.copernicus.eu/

O arquivo data/README.md contém instruções detalhadas.

Como executar

Clone este repositório:

git clone https://github.com/SEU_USUARIO/weather-launch-forecast-ia


Instale dependências:

pip install -r requirements.txt


Abra o notebook:

jupyter notebook src/modeling.ipynb

Documentação

O artigo final está disponível em:
📄 docs/Dias_2025_Predicao_Janelas_Lancamento_Meteorologia_IA.pdf

🎥 Apresentação (em breve)

Link do vídeo: (a inserir)

👩‍💻 Autor

Larissa Fernanda Gonçalves Dias
Programa de Capacitação em Inteligência Artificial Aplicada ao Setor Aeroespacial – Instituto HBR
