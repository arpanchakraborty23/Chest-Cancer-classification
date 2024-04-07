import sys,os
from src.configuration.config import DataIngestionConfig,ConfigManager
from src.components.data_ingestion import DataIngestion
from src.logging.logger import logging
from src.exception.exception import CustomException

Stage_Name='Data Ingestion'
class DataIngestionTrainPipline:
    def __init__(self) -> None:
        pass

    def IngestionPipline(self):
        
        try:
            config=ConfigManager()
            data_ingestion_config=config.get_data_ingestion()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.ectrat_zip_data()
            
        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise CustomException(sys,e)
        
if __name__=='__main__':
    try:
        logging.info(f'<<<<<<<<<<<<<<<<{Stage_Name} Started >>>>>>>>>>>>>>>>>')
        object=DataIngestionTrainPipline()
        object.IngestionPipline()
        logging.info(f'------------------{Stage_Name} completed ------------------')
    except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise CustomException(sys,e)      