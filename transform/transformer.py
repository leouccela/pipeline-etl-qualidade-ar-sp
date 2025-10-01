import pandas as pd
from datetime import datetime
import logging

# Configuração do logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transform_data(raw_data: dict) -> pd.DataFrame: 
    """
    Transforma os dados brutos da API em um DataFrame limpo e estruturado.
    
    Args: 
        raw_data (dict): Um dicionário contendo a resposta da API.
    
    Returns:
        pd.DataFrame: Um DataFrame do Pandas com os dados tratados.
    """
    processed_data = []
    location_data = raw_data.get("coord", {})

    for item in raw_data.get("list", []):
        data_point = {
            "cidade": "São Paulo", # Este dado não vem da API
            "latitude": location_data.get("lat"),
            "longitude": location_data.get("lon"),
            "data_coleta": datetime.fromtimestamp(item.get("dt")).strftime('%Y-%m-%d %H:%m:%S'),
            "aqi": item.get("main", {}).get("aqi"),
            "co_componente": item.get("components", {}).get ("co"),
            "no_componente": item.get("components", {}).get("no"),
            "no2_componente": item.get("components", {}).get("no2"),
            "o3_componente": item.get("components", {}).get("o3"),
            "so2_componente": item.get("components", {}).get("so2"),
            "pm2_5_componente": item.get("components", {}).get("pm2_5"),
            "pm10_componente": item.get("components", {}).get("pm10"),
            "nh3_componente": item.get("components", {}).get("nh3")
        }
        processed_data.append(data_point)
    
    # DataFrame a partir da lista de dicionários processados

    df = pd.DataFrame(processed_data)
    
    logging.info(f"Dados transformados com sucesso. {len(df)} Registros processados.")

    return df 

# A função de teste abaixo foi transferida para o main.py

if __name__ == "__main__":
    # Para importar a função do script collector
    from extract.collector import get_air_pollution_data

    # 1. Extrai dados brutos para usar como amostra
    logging.info("Iniciando teste do módulo de transformação...")
    sample_raw_data = get_air_pollution_data(lat=23.5505, lon=46.6333)

    # 2. Testa a função de transformação se os dados brutos foram obtidos
    if sample_raw_data:
        transformed_df = transform_data(sample_raw_data)

        print("\n--- Amostra do DataFrame transformado ---")
        print(transformed_df.head()) # .head() mostra as 5 primeiras linhas

        print("\n--- Informações Gerais do DataFrame ---")
        transformed_df.info() # .info() mostra um resumo técnico (tipos de dados, etc.)
    else:
        logging.warning("Não foi possível obter dados brutos para o teste de transformação.")

