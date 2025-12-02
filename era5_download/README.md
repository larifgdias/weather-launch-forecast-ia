# ERA5 Download – Demonstração

Este módulo contém um script simples para baixar dados do ERA5 usando a 
API do Climate Data Store (CDS).  
Ele foi criado como demonstração prática do pipeline de coleta utilizado 
no projeto **Weather Launch Forecast – IA aplicada a janelas de lançamento 
espacial**.

## 📂 Estrutura do módulo

- `download_era5_sample.py` – Script de teste para baixar dados ERA5 para 
um único lançamento.  
- `launches_geo.csv` – CSV com informações de lançamentos espaciais, 
incluindo latitude, longitude e horário UTC do lançamento.  
- `era5_test_launch.nc` – Arquivo NetCDF gerado pelo script de teste.  
- `README.md` – Este arquivo de documentação.

## Como executar

1. Configure a sua API do CDS no arquivo `~/.cdsapirc` com:
    ```
    url: https://cds.climate.copernicus.eu/api
    key: SUA_API_KEY
    ```
2. Verifique se `launches_geo.csv` está na mesma pasta que o script.  
3. Execute o script de teste:
    ```bash
    python download_era5_sample.py
    ```
4. Após execução bem-sucedida, o arquivo `era5_test_launch.nc` será criado 
na mesma pasta.

## 📦 Dependências

- Python 3.x  
- `pandas`  
- `cdsapi`  

Instale via pip:
```bash
pip install pandas cdsapi

🔗 Referências

Climate Data Store – ERA5

Documentação CDS API

👩‍💻 Autor

Larissa Fernanda Gonçalves Dias
Programa de Capacitação em Inteligência Artificial Aplicada ao Setor 
Aeroespacial – Instituto HBR
Email: larifgdias@gmail.com
