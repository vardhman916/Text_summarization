import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)
project_name = 'TEXT_SUMMARIZATION'

LIST_OF_FILE = {
    f"src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/predict_pipeline.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/config1/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/common.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "app.py",
    "Dockerfile",
    "main.py",
    "setup.py"
}
for file in LIST_OF_FILE:
    file_path = Path(file)
    file_dir,file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True) #exist_ok means it not raise the error when file exist
        logging.info(f"directory path is created for the file name is {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with  open(file_path,'w') as f:
            pass
            logging.info(file)
    else:
        logging.info(f"{file_name} is already exists")

# not os.path.exists(file_path) Checks if the file doesn't exist.
# os.path.getsize(file_path) == 0 Checks if the file exists but is empty (0 bytes).

# os:- os interact with operating system to work with file and folder,check path, create/delete and more

