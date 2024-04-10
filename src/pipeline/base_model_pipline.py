from src.configuration.config import ConfigManager
from src.components.base_model import BaseModel
from src.logging.logger import logging
from src.exception.exception import CustomException
import os,sys


Stage_Name2='Base_model'
class BaseModelPipline:
    def __init__(self) -> None:
        pass
    def ModelPipeline(self):
        try:
            config=ConfigManager()
            base_model_config=config.get_base_model_config()
            base_model=BaseModel(config= base_model_config)
            base_model.get_base_model()
            base_model.update_base_model()
        except Exception as e:
                    logging.info('error occured ', str(e))
                    raise CustomException(sys,e) 
        
if __name__=="__main__":
    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {Stage_Name2} started >>>>>>>>")
        obj=BaseModelPipline()
        obj.ModelPipeline()
        logging.info(f">>>>>> stage {Stage_Name2} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(sys,e) 
