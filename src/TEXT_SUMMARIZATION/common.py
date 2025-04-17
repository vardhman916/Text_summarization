import sys
import os
from src.TEXT_SUMMARIZATION.exception import CustomException
import yaml
from src.TEXT_SUMMARIZATION.logger import logging
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox: #why we always make yaml file
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file:{path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose= True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok = True)
        if verbose:
            logging.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path:Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"