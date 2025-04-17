from src.TEXT_SUMMARIZATION.exception import CustomException
from src.TEXT_SUMMARIZATION.logger import logging
import sys
from src.TEXT_SUMMARIZATION.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.TEXT_SUMMARIZATION.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
stage_name1 = 'Data_Ingestion'
stage_name2 = 'Data_Validation'
try:
    logging.info(f"{stage_name1}  is started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f"{stage_name1}  is completed")


    #############################################
    logging.info(f"{stage_name2}  is started")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logging.info(f"{stage_name2}  is completed")
except Exception as e:
    raise CustomException(e,sys)
    









