import os
from deepClassifier.entity import PrepareCallbacksConfig
import tensorflow as tf
import time

#creating callback component
#Callback is a method where we save the model from time to time so that in case our training is stopped by some reason, then we can start with latest model.
#It also maintains tensorflow logs so we get to know the status of training, accuracy and loss status, etc
#Callback examples are checkpoint callbacks, early stopping callbacks, tensorboard logs callbacks, etc.
#Checkpoint callback is similar to autosave after certain iterations/time steps in CFD workflow, whereas early stopping is similar to convergence achieved within certain threshold, and, tensorboard logs is like logfiles of .sim

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig): #takes input in local config variable with i/p datatype as PrepareCallbacksConfig
        self.config = config

    # single _ is used as a nomenclature for hidden method.
    @property #property decorator
    def _create_tb_callbacks(self):
        #creating directories with timestamp
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S") #timestamp use for creating unique directories. dir name will be Year-month-date-hr-min-sec
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}"
            )        
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True #save only best weights
        )

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks, #for this fun we are not using (), bcoz we have decorated this function with @property decorator.
            self._create_ckpt_callbacks
        ]
    