from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier.entity import DataIngestionConfig

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