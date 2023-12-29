from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME_01 = "Data Ingestion stage"

try:
    logger.info(f">>>> {STAGE_NAME_01} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> {STAGE_NAME_01} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_02 = "Prepare Base Model"

try:
    logger.info(f">>>> {STAGE_NAME_02} started <<<<<")
    prepare_base_model =PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> {STAGE_NAME_02} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e