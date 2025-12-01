# Weather Launch Forecast – IA aplicada a janelas de lançamento espacial

Este repositório contém o código, dados e documentação do projeto **Predição de Janelas de Lançamento Espacial a partir de Condições Meteorológicas com Modelos de Aprendizado de Máquina**, desenvolvido no Programa de Capacitação em Inteligência Artificial Aplicada ao Setor Aeroespacial – Instituto HBR.

## 🎯 Objetivo do projeto

Desenvolver um modelo de aprendizado de máquina capaz de **prever, com até 48 horas de antecedência**, a viabilidade de uma janela de lançamento espacial com base em variáveis meteorológicas extraídas do conjunto **ERA5**, integradas a dados históricos de missões.

O objetivo final é apoiar decisões de **go/no-go**, reduzindo riscos e impactos operacionais associados a lançamentos adiados.

## 📊 Visão geral da solução

O pipeline inclui:

1. Coleta de dados de lançamentos espaciais  
2. Extração de variáveis meteorológicas ERA5  
3. Engenharia de atributos  
4. Treinamento de modelos supervisionados  
   - Regressão Logística  
   - Gradient Boosting  
   - XGBoost  
5. Avaliação temporal (time-split)  
6. Interpretação dos modelos via SHAP  
7. Geração do artigo final (`blob/main/Dias_2025_Predicao_Janelas_Lancamento_Meteorologia_IA.pdf`)

O **Gradient Boosting** apresentou o melhor desempenho geral.

## 🧠 Principais variáveis meteorológicas utilizadas

- velocidade do vento  
- rajadas máximas  
- precipitação acumulada  
- tendência da pressão  
- cobertura de nuvens  

## 📂 Estrutura do repositório

weather-launch-forecast-ia/
├── src/
│ └── modeling.ipynb
├── data/
│ └── README.md
├── blob/main/
│ └── Dias_2025_Predicao_Janelas_Lancamento_Meteorologia_IA.pdf
├── README.md
└── requirements.txt


## 📥 Obtenção dos dados ERA5

Os dados meteorológicos utilizados foram extraídos do **ERA5** via Climate Data Store (CDS).

Link: https://cds.climate.copernicus.eu/

O arquivo `data/README.md` contém instruções detalhadas para acesso via API e download manual.

## ▶️ Como executar

1. Clone este repositório:
```
git clone https://github.com/larifgdias/weather-launch-forecast-ia
```
2. Instale dependências:
```
pip install -r requirements.txt
```
3. Execute o notebook:
```
jupyter notebook src/modeling.ipynb
```
📑 Documentação

O artigo técnico final está disponível em:
📄 blob/main/Dias_2025_Predicao_Janelas_Lancamento_Meteorologia_IA.pdf

🎥 Apresentação (em breve)

Link do vídeo: (a inserir)

👩‍💻 Autor

Larissa Fernanda Gonçalves Dias
Programa de Capacitação em Inteligência Artificial Aplicada ao Setor Aeroespacial – Instituto HBR
Email: larifgdias@gmail.com
