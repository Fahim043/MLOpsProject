import os
from pathlib import Path

list_of_files=[
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/compenents/__init__.py", # component trainig pipe time DE, EDA, Trainig Etc
    "src/compenents/data_ingestion.py",
    "src/compenents/data_transformation.py",
    "src/compenents/data_trainer.py",
    "src/compenents/data_evaluation.py",
    "src/pipline/__init__.py",
    "src/pipline/traning_pipieline.py",
    "src/pipline/prediction_pipieline.py",
     "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exceptiontests/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        # logging.info(f"Creating directory:{filedir} for file:{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass #crreating an empty file]




