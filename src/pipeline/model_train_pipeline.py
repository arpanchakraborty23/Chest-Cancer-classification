from src.configuration.config import ConfigManager
from src.components.model_trainer import ModelTraining
from src.logging.logger import logging
from src.exception.exception import CustomException
import os,sys
from pathlib import Path
import tensorflow as tf
from tensorflow import keras

Stage_Name3='Model Train'
class ModelTrainPipeline:
    def __init__(self) -> None:
        pass


    def ModelTrainPipleline(self):
        try:
            config=ConfigManager()
            train_config=config.get_model_train_config()
            train=ModelTraining(config=train_config)
            train.get_base_model()
            train.train_valid_generator()
            train.train()

        except Exception as e:
            logging.info('errorr ',str(e))
            raise CustomException(sys,e)

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