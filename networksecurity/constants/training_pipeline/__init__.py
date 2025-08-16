import os
import sys
import numpy as np
"""
Defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str ="NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yml")
SAVED_MODEL_DIR = os.path.join("saved_models")

"""
Data Ingestion related constant should always start with DATA_INESTION_VARIABLE_NAME
"""
DATA_INESTION_COLLECTION_NAME:str = "NetworkData"  # get this from mongodb
DATA_INESTION_DATABASE_NAME:str = "ROUNAK_KUMAR"   # get this from mongodb
DATA_INESTION_DIR_NAME:str = "data_ingestion"           # Folder name
DATA_INESTION_FEATURE_STORE_DIR: str = "feature_store"  # Folder name
DATA_INESTION_INGESTED_DIR:str = "ingested"             # Folder name
DATA_INESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.3

"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "Validated"
DATA_VALIDATION_INVALID_DIR:str = "Invalidated"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "Drift_Report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "report.yml"

"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# KKN imputer to replace nan values

DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors" :3,
    "weights":"uniform",
}

DATA_TRANSFORMATION_TRAIN_FILE_PATH:str = "train.npy"
DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"


"""
Model Trainer related to constant start with MODEL_TRAINER_VAR_NAME
"""

MODEL_TRAINER_DIR_NAME:str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str = "trained model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE:float = 0.65
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD:float =0.05
MODEL_FILE_NAME:str = "model.pkl"