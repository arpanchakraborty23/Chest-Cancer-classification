from dataclasses  import dataclass
from src.constant import *
from src.utils.main_utils import read_yaml,create_dir
from src.entity.config_entity import DataIngestionConfig

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