import sys,os


from src.pipeline.data_ingestion_pipline import DataIngestionTrainPipline
from src.pipeline.base_model_pipline import BaseModelPipline
from src.pipeline.model_train_pipeline import ModelTrainPipeline
from src.pipeline.model_eval_pipline import EvaluationPipline

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

try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {Stage_Name3} started >>>>>>>>")
        obj=ModelTrainPipeline()
        obj.ModelTrainPipleline()
        logging.info(f">>>>>> stage {Stage_Name3} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise CustomException(sys,e)  

STAGE_NAME4 = "Evaluation stage"
try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME4} started <<<<<<")
        obj = EvaluationPipline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME4} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.info(e)
        raise CustomException(sys,e)  