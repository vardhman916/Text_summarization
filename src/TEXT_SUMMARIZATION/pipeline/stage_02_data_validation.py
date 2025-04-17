from src.TEXT_SUMMARIZATION.exception import CustomException
from src.TEXT_SUMMARIZATION.logger import logging
from src.TEXT_SUMMARIZATION.components.data_validation import *
from src.TEXT_SUMMARIZATION.config1.configuration import ConfigurationManager
import sys
class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise CustomException(e,sys)