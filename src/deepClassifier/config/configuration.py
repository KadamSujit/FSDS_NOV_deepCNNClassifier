import os
from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier.entity import (
    DataIngestionConfig, 
    PrepareBaseModelConfig, 
    PrepareCallbacksConfig, 
    TrainingConfig
)
from pathlib import Path

class ConfigurationManager:

    def __init__(self, config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath) #reading config file
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
        

    def get_data_ingestion_config(self) -> DataIngestionConfig: #o/p datatype will be DataIngestionConfig
        config = self.config.data_ingestion #passing data to local config variable

        create_directories([config.root_dir]) #creating directory

        data_ingestion_config = DataIngestionConfig( #using named tuple to get o/p datatype as DataIngestionConfig
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig: #o/p datatype will be PrepareBaseModelConfig
        config = self.config.prepare_base_model #passing data to local config variable. This data prepare_base_model comes from config.yaml file

        create_directories([config.root_dir]) #creating directory

        prepare_base_model_config = PrepareBaseModelConfig( #using class tuple to get o/p datatype as PrepareBaseModelConfig
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate = self.params.LEARNING_RATE,
            params_include_top = self.params.INCLUDE_TOP,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )
        return prepare_base_model_config
    

    def get_prepare_callback_config(self) -> PrepareCallbacksConfig: #o/p datatype will be PrepareCallbacksConfig
        config = self.config.prepare_callbacks #passing data to local config variable. This data prepare_callbacks comes from config.yaml file
        
        #creating directory not only for root but for checkpoint and tensorboard logs.
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath) #dirname gives dir filename/filepath for model checkpoint. This data comes from config.yaml file
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ]) 

        prepare_callbacks_config = PrepareCallbacksConfig( #using class tuple to get o/p datatype as PrepareCallbacksConfig
            root_dir = Path(config.root_dir),
            tensorboard_root_log_dir = Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath = Path(config.checkpoint_model_filepath)
        )
        return prepare_callbacks_config
    

    def get_training_config(self) -> TrainingConfig: #o/p datatype will be TrainingConfig
        training = self.config.training #passing data to local config variable. This data training comes from config.yaml file
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir,"PetImages")
        #creating directory for root
        create_directories([Path(training.root_dir)])

        training_config = TrainingConfig( #using class tuple to get o/p datatype as TrainingConfig
            root_dir = Path(training.root_dir),
            trained_model_path = Path(training.trained_model_path),
            updated_base_model_path = Path(prepare_base_model.updated_base_model_path), 
            training_data = Path(training_data),
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_is_augmentation = params.AUGMENTATION,
            params_image_size = params.IMAGE_SIZE
        )
        return training_config