#Written to create all files and folders 

import os
from pathlib import Path #to create system compatible path ['/']
#import logging

lis_of_files = [
    ".github/workflows/.gitkeep", #Github folder will be used for deployemnt, entire configuration for continuos integration and Continuous deployement
    "src/__init__.py", #src folder contains entire source code
    "src/components/__init__.py", #components folder has to be used for different ML components like data ingestion, data transformation, fe, model training, model evaluation
    "src/components/data_ingestion.py", 
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py", #for writing utility methods
    "src/utils/utils.py", #for writing utility methods
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py", #file for unit testing 
    "tests/integration/__init__.py", #file for integration testing
    "init_setup.sh", #to initialize the setup #write Linux commands to be run on command pallet
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml", 
    "tox.ini", #Used for testing project in local developement environment
    "experiment/experiments.ipynb" #Exp folder has to be used for experiement like diff small codes instead of using python kernel
]

for filepath in lis_of_files:
    filepath =Path(filepath)
    filedir,filename=os.path.split(filepath) #getting file directory
    if filedir != "": #checking file directory is it empty or not
        os.makedirs(filedir,exist_ok=True)
        #logging.info(f"Creating directory: {filedir} for file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass #create an empty file