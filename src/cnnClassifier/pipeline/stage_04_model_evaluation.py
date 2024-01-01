from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import ModelEvaluation
from cnnClassifier import logger
import os


# Pipeline
STAGE_NAME = "Evaluating the Model"

# create new class for preparing base model training pipeline
class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        model_evaluation_config = config.get_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluation()
        # model_evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<x========x")
    except Exception as e:
        logger.exception(e)
        raise e