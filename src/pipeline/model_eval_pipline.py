from src.configuration.config import ConfigManager
from src.components.model_evaluation import Evaluation
from src.logging.logger import logging
from src.exception.exception import CustomException

import sys,os

STAGE_NAME4 = "Evaluation stage"

class EvaluationPipline:
    def __init__(self) -> None:
        
        pass
    def main(self):
        try:
            config=ConfigManager()
            eval_config=config.get_eval_config()
            evaluation=Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.log_to_mlflow()

        except Exception as e:
            logging.info(f'Error occured {str(e)}')
            raise CustomException(sys,e)
        
if __name__ == '__main__':
    try:
        logging.info(f"*******************")
        logging.info(f">>>>>> stage {STAGE_NAME4} started <<<<<<")
        obj = EvaluationPipline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME4} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.info(e)
        raise CustomException(sys,e)
