from src.TEXT_SUMMARIZATION.exception import CustomException
from src.TEXT_SUMMARIZATION.logger import logging
from src.TEXT_SUMMARIZATION.components.model_evaluation import *
from src.TEXT_SUMMARIZATION.config1.configuration import ConfigurationManager
import sys

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_data_evaluation_config() 
            model_evaluator = ModelEvaluation(config = model_evaluation_config)
            model_evaluator.evaluate()
        except Exception as e:
            raise CustomException(e,sys)