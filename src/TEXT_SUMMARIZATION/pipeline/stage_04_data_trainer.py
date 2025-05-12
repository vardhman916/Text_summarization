from src.TEXT_SUMMARIZATION.exception import CustomException
from src.TEXT_SUMMARIZATION.logger import logging
from src.TEXT_SUMMARIZATION.components.model_trainer import *
from src.TEXT_SUMMARIZATION.config1.configuration import ConfigurationManager
import sys

class ModelTraininerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config = model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise CustomException(e,sys)