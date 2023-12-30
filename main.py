from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
import os

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Arshavin023/deep-learning---image-classification-with-CNN.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Arshavin023"
os.environ["MLFLOW_TRACKING_PASSWORD"]="3a6add494bc8a69b0623dd2f8030d353dde15622"

# STAGE_NAME_01 = "Data Ingestion stage"
# try:
#     logger.info(f">>>> {STAGE_NAME_01} started <<<<<")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f">>>>> {STAGE_NAME_01} completed <<<<<<\n\nx========x")
# except Exception as e:
#     logger.exception(e)
#     raise e

STAGE_NAME_02 = "Prepare Base Model"
try:
    logger.info(f">>>> {STAGE_NAME_02} started <<<<<")
    prepare_base_model =PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> {STAGE_NAME_02} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_03 = "Training Model"
try:
    logger.info(f">>>> {STAGE_NAME_03} started <<<<<")
    model_training =ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>> {STAGE_NAME_03} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_04 = "Evaluating the Model"
try:
    logger.info(f">>>> {STAGE_NAME_04} started <<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>> {STAGE_NAME_04} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e