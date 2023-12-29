from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


# Pipeline
STAGE_NAME = "Prepare Base Model"

# create new class for preparing base model training pipeline
class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == '__main__':
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<x========x")
    except Exception as e:
        logger.exception(e)
        raise e