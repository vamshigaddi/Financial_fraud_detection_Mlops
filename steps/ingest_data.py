import logging
import pandas as pd
from logs.logging_config import setup_logging

# Setup logging
setup_logging()

# Create a logger for this file
logger = logging.getLogger(__name__)

class IngestData:
    """
    Ingesting the data from data_path
    """
    def __init__(self, data_path: str):
        """
        Args:
            data_path: path to the data
        """
        self.data_path = data_path
        
    def get_data(self):
        """
        Ingesting the data from the data_path 
        """
        logger.info(f'Ingesting data from {self.data_path}')
        return pd.read_csv(self.data_path)
    

def ingest_df(data_path: str) -> pd.DataFrame:

    """
    Ingesting the data from the dataframe
    
    Args: 
        data_path: path to the data
    
    Returns: 
        pd.DataFrame: the ingested data

            pd.DataFrame: the ingested data
    """
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logger.error(f'Error while ingesting the data:{e}')
        raise e
