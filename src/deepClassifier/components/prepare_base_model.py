import os
from pathlib import Path
import tensorflow as tf
from deepClassifier.entity import PrepareBaseModelConfig

#creating prepare base model component
class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig): #takes input in local config variable with i/p datatype as PrepareBaseModelConfig
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape= self.config.params_image_size,
            weights= self.config.params_weights,
            include_top= self.config.params_include_top
        )

        self.save_model(path=self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate): #this method will freeze certain layer and add the top layer
        if freeze_all:
            for layer in model.layers:
                model.trainable =False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output) #This is Functional approach instead of sequential. Here we pass the model output to flatten as input
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in) #here we pass the flatten_in as input to prediction. As it looks like a function hence called functional approach where prediction is a function and flatten_in is its input.

        full_model = tf.keras.models.Model(
            inputs= model.input,
            outputs = prediction
        )

        full_model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate = learning_rate),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ['accuracy']
        )
        full_model.summary()
        return full_model
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            freeze_all = True,
            freeze_till = None, #freeze till which layer
            learning_rate = self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model): #this method does not use self in it as it has no use. so no need to give in constructor as well, just make the method static.
        model.save(path) #no use of self inside


    