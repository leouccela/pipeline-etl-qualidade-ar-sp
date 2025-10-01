# Importações necessárias

import os
import requests
from dotenv import load_dotenv
import logging

# Configuração básica do logging - para visualizarmos possíveis erros

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_air_pollution_data(lat, lon):
    """Busca dados de poluição do ar da API OpenWeatherMap.
    
    Args:
        lat (float): Latitude da localização
        lon (float): Longitude da localização
        
    Returns:
        dict: Um dicionário com dados da API, ou None se ocorrer um erro.
    """
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        logging.error("Chave de API não encontrada. Verifique seu arquivo .env.")
        return None
    
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"

    # Realizar requisições e tratar erros

    try:
        logging.info(f"Buscando dados para lat={lat}, lon={lon}")
        response = requests.get(url)
        response.raise_for_status() # Caso dê algum erro

        logging.info("Dados recebidos com sucesso.")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na requisição à API: {e}")
        return None
    
if __name__ == "__main__":
    sp_lat = -23.5505
    sp_lon = -46.6333

    air_data = get_air_pollution_data(sp_lat, sp_lon)

    if air_data:
        import json
        print("--- Dados brutos recebidos da API ---")
        print(json.dumps(air_data, indent=4))