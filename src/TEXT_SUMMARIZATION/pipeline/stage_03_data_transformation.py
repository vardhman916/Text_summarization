from src.TEXT_SUMMARIZATION.exception import CustomException
from src.TEXT_SUMMARIZATION.logger import logging
from src.TEXT_SUMMARIZATION.components.model_transformation import *
from src.TEXT_SUMMARIZATION.config1.configuration import ConfigurationManager
import sys
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise CustomException(e,sys)