from deepClassifier.config import ConfigurationManager
from deepClassifier.components import Evaluation
from deepClassifier import logger

STAGE_NAME = "Evaluation stage"

def main():
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(config = val_config)
    out = evaluation.evaluation() #running evaluation method from our user defined Evaluation class
    evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info(f'\n****************************************************************')
        logger.info(f'>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<')
        main()
        logger.info(f'>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx===============x')
    except Exception as e:
        logger.exception(e)
        raise e