import cdsapi
import pandas as pd
from datetime import timedelta

# ---- CONFIG ----
CSV_FILE = "launches_geo.csv"

# Carrega o CSV e escolhe o primeiro lançamento para teste
df = pd.read_csv(CSV_FILE)
row = df.iloc[0]

lat = float(row["latitude"])
lon = float(row["longitude"])
t_launch = pd.to_datetime(row["launch_time_utc"])

# Janela T-48h até T
start_time = (t_launch - timedelta(hours=48)).strftime("%Y-%m-%d")
end_time = t_launch.strftime("%Y-%m-%d")

# ---- DOWNLOAD ----
c = cdsapi.Client()

c.retrieve(
    "reanalysis-era5-single-levels",
    {
        "product_type": "reanalysis",
        "variable": [
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "2m_temperature",
            "2m_dewpoint_temperature",
            "surface_pressure",
            "total_cloud_cover",
            "total_precipitation",
        ],
        "year": str(t_launch.year),
        "month": f"{t_launch.month:02d}",
        "day": [f"{(t_launch - timedelta(hours=h)).day:02d}" for h in range(48, -1, -1)],
        "time": [f"{hour:02d}:00" for hour in range(24)],
        "area": [
            lat + 0.25,  # north
            lon - 0.25,  # west
            lat - 0.25,  # south
            lon + 0.25,  # east
        ],
        "data_format": "netcdf",  # corrigido de 'format'
    },
    "era5_test_launch.nc",
)

print("Download concluído: era5_test_launch.nc")

