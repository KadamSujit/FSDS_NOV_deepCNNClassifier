import os
import urllib.request as request #to work on url (while downloading)
from zipfile import ZipFile # for zip
from deepClassifier.entity import DataIngestionConfig
from deepClassifier import logger
from deepClassifier.utils import get_size
from tqdm import tqdm #tqdm is a lib that gives us prompt
from pathlib import Path

#creating data ingestion component
class DataIngestion:
    def __init__(self, config: DataIngestionConfig): #takes input in local config variable with i/p datatype as DataIngestionConfig
        self.config = config
    
    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file): #check if file is present or not, if not only then download
            logger.info("Download started...")
            filename, headers = request.urlretrieve ( #request method helps to download the file. It also returns filename and headers(metadata)
                url= self.config.source_URL, #download from here
                filename = self.config.local_data_file #keep download file here
            )
            logger.info(f"{filename} download with the following info: \n{headers}")
        else: #if file is present
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}") #logging file presence with its size


    def _getupdated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)] # list comprehension for selecting only .jpg files(condition1) with cat or dog name in its file path (condition 2)

    #Any method starting with _ is hidden method(naming convention). e.g _getupdated_list_of_files, _preprocess. They are internal methods which can be updated later. These methods are not supposed to be used by user as they get changed from time to time.
    def _preprocess(self, zf:ZipFile, f:str, working_dir:str):
        target_filepath = os.path.join(working_dir, f)
        #first extract the files and then check for their size
        if not os.path.exists(target_filepath): #if this file does not exists, then only do extraction
            zf.extract(f, working_dir) #extracts from f to working dir

        if os.path.getsize(target_filepath) == 0:
            logger.info(f"removing file {target_filepath} of size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath) #del 0kb files

    def unzip_and_clean(self): #cleaning here means we take only required ".jpg" files. Also we will have to eliminate 0kb size files
        logger.info(f"unzipping file and removing unwanted files")
        with ZipFile (file=self.config.local_data_file, mode ="r") as zf:
            list_of_files = zf.namelist() #to get names of all the files
            updated_list_of_files = self._getupdated_list_of_files(list_of_files)
            #now we will preprocess to check if files are present at the location and also there file size not to be zero
            for f in tqdm(updated_list_of_files): #tqdm is a lib that gives us prompt
                self._preprocess(zf, f, self.config.unzip_dir)
            
    def create_test_data(self):
        '''separate 30% data into test data'''
        pass
    