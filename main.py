import sys,os
from src.configuration.config import ConfigManager

from src.components.data_ingestion import DataIngestion
from src.components.base_model import BaseModel
from src.components.model_trainer import ModelTraining

from src.pipeline.training_pipeline import DataIngestionTrainPipline
from src.pipeline.base_model_pipline import BaseModelPipline
from src.pipeline.model_train_pipeline import ModelTrainPipeline

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

Stage_Name2='Base Model'
try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {Stage_Name2} started >>>>>>>>")
        obj=BaseModelPipline()
        obj.ModelPipeline()
        logging.info(f">>>>>> stage {Stage_Name2} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise CustomException(sys,e) 

Stage_Name3='Model Train'
if __name__=="__main__":
    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {Stage_Name3} started >>>>>>>>")
        obj=ModelTrainPipeline()
        obj.ModelTrainPipleline()
        logging.info(f">>>>>> stage {Stage_Name3} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(sys,e)    