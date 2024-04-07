import os,sys
import zipfile
import gdown
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.utils.main_utils import get_size
from src.configuration.config import ConfigManager
from src.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config=config

    def download_file(self):
        try:
            logging.info('data ingestion has started ')

            # geting data url
            dataset_url=self.config.source_url

            # create a local data folder
            os.makedirs(self.config.dir,exist_ok=True)

            # download data in local folder
            zip_download=self.config.local_data_file

            prefix='https://drive.google.com/uc?/export=download&id='
            id=dataset_url.split('/')[5]
            print(id)
            gdown.download(prefix+id,zip_download)
            logging.info('Zip data download completed')

        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise CustomException(sys,e)
        

    def ectrat_zip_data(self):
        try:
            unzip_data=self.config.unzip_dir
            os.makedirs(unzip_data,exist_ok=True)

            with zipfile.ZipFile(self.config.local_data_file,'r') as z:
                z.extractall(unzip_data)
        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise CustomException(sys,e)
