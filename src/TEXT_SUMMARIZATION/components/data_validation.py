import os
import sys
from src.TEXT_SUMMARIZATION.logger import logging
from src.TEXT_SUMMARIZATION.entity import DataValidationConfig
from src.TEXT_SUMMARIZATION.exception import CustomException


class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config


    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.All_required_file:
                    validation_status = False
                    with open(self.config.status_file,'w') as f:
                        f.write(f"Validation status of {file}:{validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file,'w') as f:
                        f.write(f"Validation status of {file} : {validation_status}")
            return validation_status
        
        except Exception as e:
            raise CustomException(e,sys)