from src.TEXT_SUMMARIZATION.exception import CustomException
from src.TEXT_SUMMARIZATION.logger import logging
import sys
from src.TEXT_SUMMARIZATION.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
stage_name = "Data Ingestion"
try:
    logging.info(f"{stage_name}  is started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f"{stage_name}  is completed")
except Exception as e:
    raise CustomException(e,sys)
    









