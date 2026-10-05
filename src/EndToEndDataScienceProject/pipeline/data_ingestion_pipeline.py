from src.EndToEndDataScienceProject.config.configuration import ConfigrationManager
from src.EndToEndDataScienceProject.components.data_ingestion import DataIngestion
from src.EndToEndDataScienceProject import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        self.config = ConfigrationManager()

    def main(self):
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        data_ingestion_config = self.config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x") 


if __name__ == "__main__":
    try:
        data_ingestion_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_pipeline.main()
    except Exception as e:
        logger.exception(e)
        raise e