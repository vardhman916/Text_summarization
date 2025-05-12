from src.TEXT_SUMMARIZATION.exception import CustomException
from src.TEXT_SUMMARIZATION.logger import logging
import sys
from src.TEXT_SUMMARIZATION.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.TEXT_SUMMARIZATION.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.TEXT_SUMMARIZATION.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.TEXT_SUMMARIZATION.pipeline.stage_04_data_trainer import ModelTraininerTrainingPipeline
from src.TEXT_SUMMARIZATION.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


stage_name1 = 'Data_Ingestion'
stage_name2 = 'Data_Validation'
stage_name3 = 'Data_transformation'
stage_name4 = "Model trainer"
stage_name5 = "Model Evaluation"
try:
    #############################################
    # logging.info(f"{stage_name1}  is started")
    # data_ingestion = DataIngestionTrainingPipeline()
    # data_ingestion.main()
    # logging.info(f"{stage_name1}  is completed")


    # #############################################
    # logging.info(f"{stage_name2}  is started")
    # data_validation = DataValidationTrainingPipeline()
    # data_validation.main()
    # logging.info(f"{stage_name2}  is completed")

    # ###############################################
    # logging.info(f"{stage_name3}  is started")
    # data_transformation = DataTransformationTrainingPipeline()
    # data_transformation.main()
    # logging.info(f"{stage_name3}  is completed")

    # ###############################################
    # logging.info(f"{stage_name4}  is started")
    # data_trainer = ModelTraininerTrainingPipeline()
    # data_trainer.main()
    # logging.info(f"{stage_name4}  is completed")

    #################################################
    logging.info(f"{stage_name5}  is started")
    data_trainer = ModelEvaluationTrainingPipeline()
    data_trainer.main()
    logging.info(f"{stage_name5}  is completed")
    
except Exception as e:
    raise CustomException(e,sys)
    









