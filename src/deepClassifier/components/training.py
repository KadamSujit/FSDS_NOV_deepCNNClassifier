import os
import tensorflow as tf
import time
from deepClassifier.entity import TrainingConfig
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig): #takes input in local config variable with i/p datatype as TrainingConfig
        self.config = config

    #loading the base model
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
        
    # below function is used for augmentation. i.e it generates training and validation data if required as per conditions given to it.
    # augmentation is done when we have small dataset and we need more data for training purpose.
    # in augumentation, dataset of new images is created by rotating, fliping, streaching, zooming, etc an existing image.
    # hence it much more data, just like random seed. 
    def train_valid_generator(self):

        datagenerator_kwargs = dict( #it is a dictionary
            rescale = 1./255,
            validation_split = 0.20
        )

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

        # we don't need any augmentation for validation data as it is raw data that we want.
        # but for training purpose we need it.
        if self.config.params_is_augmentation: #execute only if augmentation is set to True
            # below function generates data from an image (just like random seed). These can also be kept in parameters file and controlled from there.
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range= 40, #rotate image by 40 radians.
                horizontal_flip=True, #horizantally flipping
                width_shift_range=0.2, # streach image by 20% horizontally by interpolation, means zoom in by 20%
                height_shift_range=0.2,# streach image by 20% vertically by interpolation
                shear_range=0.2, #like shear force, tilt image by 20%
                zoom_range=0.2, #zoom in/out
                **datagenerator_kwargs #also apply params from these dict
            )
        else: #keep the datagenerator same
            training_datagenerator = valid_datagenerator

         # creating training data generator
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model): #this is static method hence doesn't need self.
        model.save(path)

    def train(self, callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size # no of steps per epoch = sample size/batch size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs = self.config.params_epochs,
            steps_per_epoch = self.steps_per_epoch,
            validation_steps = self.validation_steps,
            validation_data = self.valid_generator,
            callbacks = callback_list
        )

        self.save_model(
            path = self.config.trained_model_path,
            model = self.model
        )


