from dataclasses  import dataclass
import sys,os
from src.constant import *
from src.utils.main_utils import read_yaml,create_dir

from src.entity.config_entity import DataIngestionConfig,BaseModelConfig
from src.entity.config_entity import ModelTrainConfig
from src.logging.logger import logging
from src.exception.exception import CustomException

class ConfigManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH) -> None:
        self.config=read_yaml(config_file_path)
        self.param=read_yaml(params_file_path)

        create_dir([self.config.artifacts_root])

    def get_data_ingestion(self)-> DataIngestionConfig:
        config=self.config.data_ingestion

        create_dir([config.dir])

        data_ingestion_config=DataIngestionConfig(
            dir=config.dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    


    def get_base_model_config(self)-> BaseModelConfig:
        try:
            config=self.config.base_model
            logging.info(f'base model {config}')

            create_dir([config.dir])

            base_model_config=BaseModelConfig(
                dir=Path(config.dir),
                base_model=Path(config.base_model_path),
                update_base_model_path=Path(config.update_base_model_path),
                image_size=self.param.IMAGE_SIZE,
                learning_rate=self.param.LEARNING_RATE,
                include_top=self.param.INCLUDE_TOP ,
                weights=self.param.WEIGHTS ,
                classes=self.param.CLASSES
            )

            return base_model_config
        except Exception as e:
            logging.info('error occured ', str(e))
            raise CustomException(sys,e) 
        

    def get_model_train_config(self)->ModelTrainConfig:
        try:
            train=self.config.model_train
            base_model=self.config.base_model
            train_data=os.path.join(self.config.data_ingestion.unzip_dir,"Chest-CT-Scan-data")
            logging.info(f'train_data {train_data}')
            
            create_dir([
                Path(train.dir)
            ])
            train_config=ModelTrainConfig(
                dir=Path(train.dir),
                model_path=Path(train.model_path),
                update_base_model_path=Path(base_model.update_base_model_path),
                train_data=Path(train_data),
                epochs=self.param.EPOCHS,
                batch_size=self.param.BATCH_SIZE,
                augmentation=self.param.AUGMENTATION,
                image_size=self.param.IMAGE_SIZE
            )

            return train_config        
        except Exception as e:
            logging.info('error occured ', str(e))
            raise CustomException(sys,e)             