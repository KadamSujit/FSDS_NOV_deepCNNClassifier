from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier.entity import DataIngestionConfig, PrepareBaseModelConfig
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