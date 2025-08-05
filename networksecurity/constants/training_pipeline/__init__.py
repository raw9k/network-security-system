import os
import sys

"""
Defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME: str ="NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
Data Ingestion related constant should always start with DATA_INESTION_VARIABLE_NAME
"""
DATA_INESTION_COLLECTION_NAME:str = "NetworkData"  # get this from mongodb
DATA_INESTION_DATABASE_NAME:str = "ROUNAK_KUMAR"   # get this from mongodb
DATA_INESTION_DIR_NAME:str = "data_ingestion"           # Folder name
DATA_INESTION_FEATURE_STORE_DIR: str = "feature_store"  # Folder name
DATA_INESTION_INGESTED_DIR:str = "ingested"             # Folder name
DATA_INESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.3