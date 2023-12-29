from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import ModelTraining
from cnnClassifier import logger
import os


# Pipeline
STAGE_NAME = "Training the Model"

# create new class for preparing base model training pipeline
class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        model_training_config = config.get_training_config()
        model_training = ModelTraining(config=model_training_config)
        model_training.get_base_model()
        model_training.train_valid_generator()
        model_training.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<x========x")
    except Exception as e:
        logger.exception(e)
        raise e