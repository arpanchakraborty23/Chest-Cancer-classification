import tensorflow as tf
from keras.models import load_model
from pathlib import Path
import mlflow
import mlflow.sklearn
import mlflow.keras
import os,sys
import json
from urllib.parse import urlparse

from src.logging.logger import logging
from src.exception.exception import CustomException
from src.entity.config_entity import EvaluationConfig
from src.utils.main_utils import read_yaml,create_dir,save_json


class Evaluation:
    def __init__(self,config:EvaluationConfig) -> None:
        self.config=config

    def valid_genrator_fun(self):
        try:   
            datagenerator_kwargs = dict(
                rescale = 1./255,
                validation_split=0.30
            )

            dataflow_kwargs = dict(
                target_size=self.config.image_size[:-1],
                batch_size=self.config.batch_size,
                interpolation="bilinear"
            )

            valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                **datagenerator_kwargs
            )

            self.valid_generator = valid_datagenerator.flow_from_directory(
                directory=self.config.train_data,
                subset="validation",
                shuffle=False,
                **dataflow_kwargs
            )
        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise CustomException(sys,e)
        
    @staticmethod
    def load_model(path:Path):
         return load_model(path)

    def evaluation(self):
        try:
            self.model=self.load_model(self.config.path_of_model)
            self.valid_genrator_fun()
            self.score=self.model.evaluate(self.valid_generator)

            self.save_score()

        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise CustomException(sys,e)
        
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    def log_to_mlflow(self):
        try:
            mlflow.set_registry_uri('https://dagshub.com/arpanchakraborty23/Chest-Cancer-classification.mlflow')
            track_url_type=urlparse(mlflow.get_tracking_uri()).scheme

            with mlflow.start_run():
                mlflow.log_params(self.config.all_params)
                mlflow.log_metrics(
                    {'loss ':self.score[0], 'accuracy': self.score[1] }
                )
                if track_url_type !='file':
                    mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
                else:
                    mlflow.keras.log_model(self.model, "model")
        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise CustomException(sys,e)
        
