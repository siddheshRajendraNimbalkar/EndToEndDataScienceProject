from src.EndToEndDataScienceProject import logger
from src.EndToEndDataScienceProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
logger.info("Starting the End to End Data Science Project")

status = DataIngestionTrainingPipeline().main()
status = "Data Ingestion Completed Successfully" if status else "Data Ingestion Failed"
