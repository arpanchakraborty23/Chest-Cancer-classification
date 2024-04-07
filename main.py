import sys,os
from src.configuration.config import DataIngestionConfig,ConfigManager
from src.components.data_ingestion import DataIngestion
from src.logging.logger import logging
from src.exception.exception import CustomException



Stage_Name='Data Ingestion'
try:
        logging.info(f'<<<<<<<<<<<<<<<<{Stage_Name} Started >>>>>>>>>>>>>>>>>')
        object = DataIngestionTrainPipline()
        object.IngestionPipline()
        logging.info(
            f'------------------{Stage_Name} completed ------------------')
except Exception as e:
        logging.info(f' Error occured {str(e)}')
        raise CustomException(sys, e)     