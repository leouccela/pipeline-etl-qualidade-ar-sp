import sqlalchemy
import logging
import pandas as pd

# Configuração do logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define o nome do arquivo do banco de dados SQLite

DATABASE_LOCATION = "sqlite:///qualidade.ar.db"
TABLE_NAME = "dados_qualidade_ar"

def load_data(df: pd.DataFrame):
    """
    Carrega um DatFrame em uma tabela no banco de dados SQLite.
    Se a tabela já existir, anexa os novos dados.
    Se não existir, cria a tabela
    """

    # Conexão com o banco de dados

    engine = sqlalchemy.create_engine(DATABASE_LOCATION)

    logging.info(f"iniciando carregamento de dados para a tabela '{TABLE_NAME}'... ")

    try:
        
        #Utiliza o método to_sql do pandas para carregar o DataFrame

        df.to_sql(
            TABLE_NAME,
            engine,
            index=False,
            if_exists='append'
        )

        logging.info(f"Dados carregados com sucesso. {len(df)} Linhas inseridas.")
    
    except Exception as e:
        logging.error(f"Erro ao carregar dados da tabela '{TABLE_NAME}': {e}")
        