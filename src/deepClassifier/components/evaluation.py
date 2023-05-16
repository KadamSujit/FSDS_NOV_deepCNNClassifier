import os
import tensorflow as tf
import time
from deepClassifier.entity import EvaluationConfig
from deepClassifier.utils import save_json
from pathlib import Path

class Evaluation:
    def __init__(self, config: EvaluationConfig): #takes input in local config variable with i/p datatype as TrainingConfig
        self.config = config
    
    #creating generator
    def _valid_generator(self):

        datagenerator_kwargs = dict( #it is a dictionary
            rescale = 1./255,
            validation_split = 0.30
        )

        # for image resizing
        dataflow_kwargs = dict( #it is a dictionary
            target_size = self.config.params_image_size [:-1], #channel info of image is not required, hence we take -1, means all rows and coloumns except last.
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs #passing the dict as kwargs to this function. This helps to pass multiple args at once
        )

        # creating validation data generator
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model: #this is static method hence doesn't need self.
        return tf.keras.models.load_model(path)

    def evaluation(self):
        model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = model.evaluate(self.valid_generator) # evaluate method returns accuracy and metrics information after evaluating the model
    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]} #dict with evaluation results. i.e loss and accuracy
        save_json(path = Path("scores.json"), data = scores) #storing in root dir by not specifying full path, so that dvc can track it easily.

