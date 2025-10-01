import logging
from extract.collector import get_air_pollution_data
from transform.transformer import transform_data
from load.loader import load_data 

# Configura o logging para o pipeline principal

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    logging.info("Iniciando pipiline ETL")

    # E - Extract: Coleta os dados brutos
    raw_data = get_air_pollution_data(lat=23.5505, lon=46.6333)

    # T - Transform: Transforma os dados se a extração foi bem sucedida
    if raw_data:
        transformed_df = transform_data(raw_data)

        # Garante que a transformação retornou um DataFrame com dados

        if not transformed_df.empty:
            logging.info("Amostra dos dados transformados:")
            print(transformed_df.head())

            # L - Load: Carrega os dados transformados no banco de dados

            load_data(transformed_df)
        else:
            logging.warning("Transformação resultou em um DataFrame vazio. Sem dados para carregar")

    else:
        logging.error("Falha na extração de dados. Pipeline encerrado")
    
    logging.info("Pipeline ETL finalizado")