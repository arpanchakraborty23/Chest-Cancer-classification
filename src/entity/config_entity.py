from dataclasses import dataclass
from pathlib import Path


# Configer path data from config yaml

@dataclass
class DataIngestionConfig:
    dir: Path
    source_url: str
    local_data_file:Path
    unzip_dir: Path