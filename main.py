from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME_01 = "Data Ingestion stage"

try:
    logger.info(f">>>> {STAGE_NAME_01} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME_01} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e