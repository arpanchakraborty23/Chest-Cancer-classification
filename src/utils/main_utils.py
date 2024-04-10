import os,sys
import yaml
from src.logging.logger import logging
from src.exception.exception import CustomException
from box.exceptions import BoxValueError
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import joblib
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_dir(path_to_dir: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")
    
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


        logging.info(f' Created dir {path}')
 
@ensure_annotations
def load_json(path)-> ConfigBox:
    try:
        with open(path,'r') as j:
            data=json.load(j)
        return data    

    except BoxValueError as e:
        logging.info('Erorr occured' ,str(e))
        raise CustomException(sys,e)        
    
@ensure_annotations
def save_bin(path,data):
    try:
        joblib.dump(value=data,filename=path)


        logging.info(f' bin file save {path}')
    except BoxValueError as e:
        logging.info('Erorr occured' ,str(e))
        raise CustomException(sys,e)    
    
@ensure_annotations
def load_json(path):
    try:
        with open(path,'r') as j:
            data=joblib.load(j)
        return data    

    except BoxValueError as e:
        logging.info('Erorr occured' ,str(e))
        raise CustomException(sys,e)    
    

def get_size(path:str):
    size=round(os.path.getsize(path)/1024) 
    return size


def decodeImage(imgstr,file):
    img_data=base64.b64decode(imgstr)
    with open(img_data,'wb') as img:
        img.write(img_data)
        img.close()

def encodeImage(croppimagepath):
    with open(croppimagepath,'rb') as c:
        d=base64.b64encode(c.read())
    return d            
