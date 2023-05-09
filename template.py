# This file creates files and folders required for almost every project. Hence instead of creating them maually we are writing a code.
import os
from pathlib import Path #used to take care of file/folder paths for different operating systems
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ') #INFO is basic level of logging

package_name="deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep", #it is inside .githup/workflows mainly used for CICD. As empty folders are never uploaded on github, hence we keep this .gitkeep file in it.
    f"src/{package_name}/__init__.py", #__init__.py helps to understand python that it is a package
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",
    "dvc.yaml", # Data Version Control pipeline
    "params.yaml", #contains all our training parameters
    "init_setup.sh", # shell script file help to create environment
    "requirements.txt", #requirements file for libraries
    "requirements_dev.txt", #requirements only for development purpose
    "setup.py", #
    "setup.cfg", # only need if we are creating python packages
    "pyproject.toml", # only need if we are creating python packages
    "tox.ini", # required for doing testing of project locally
    "research/trials.ipynb", #creating jupyter notebook file to test small codes here itself

]

for filepath in list_of_files:
    filepath = Path(filepath) #passing filepath first through Path lib so that it takes care of os issues
    #to iterate through sub-folders
    filedir, filename = os.path.split(filepath) #os.path.split method splits dir and filename and returns it. If there is only file and no directory, then it returns  dir name empty.
    # Creating a directory provided it had dir name
    if filedir !="": 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file {filename}")
    # Creating an empty file. First check if file exists or if its size is zero kb
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # this takes care that we do not overwrite existing file.
        with open(filepath, "w") as f:
            pass # do nothing. i.e create an empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
        
        