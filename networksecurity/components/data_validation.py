from networksecurity.entity.artifact_entity import DataIngestionArtifacts, DataValidationArtifacts
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.constants.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utils.main_utils.utils import read_yml_file

from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

from scipy.stats import ks_2samp
import os, sys, pandas as pd, numpy as np

class DataValidation:
    def __init__(self,data_ingestion_artifacts:DataIngestionArtifacts,
                 data_validation_artifacts: DataValidationArtifacts):
        try:
            self.data_ingestion_artifacts = data_ingestion_artifacts
            self.data_validation_artifacts = data_validation_artifacts
            self._schema_config = read_yml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    @staticmethod
    def read_data(file_path)-> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def validate_number_of_columns(self,dataframe:pd.DataFrame) -> bool:
        try:
            number_of_columns = len(self._schema_config)
            logging.info(f"Required Number of columns: {number_of_columns}")
            logging.info(f"Data frame has {number_of_columns} columns")
            
            if len(dataframe.columns) == number_of_columns:
                return True
            else:
                return False
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def validate_numerical_columns(self,dataframe:pd.DataFrame) -> bool:
        try:
            if all(np.issubdtype(dtype, np.int64) for dtype in dataframe.dtypes):
                return True
            else:
                return False
                
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
        
    def initiate_date_validation(self) -> DataValidationArtifacts:
        try:
            train_file_path = self.data_ingestion_artifacts.trained_file_path
            test_file_path = self.data_ingestion_artifacts.test_file_path
            
            ## read the data from train and test
            
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)
            
            ## Validate number of columns
            
            status = self.validate_number_of_columns(dataframe=train_dataframe)
            if not status:
                error_message = f" Train dataframe does not contain all columns. \n"
            status = self.validate_number_of_columns(dataframe=test_dataframe)
            if not status:
                error_message = f"Test dataframe does not contain all columns. \n"
            
            
            ## Validate numerical columns
            status = self.validate_numerical_columns(dataframe=train_dataframe)
            if not status:
                error_message = "Train dataframe contains non-numeric columns.\n"
        
            status = self.validate_numerical_columns(dataframe=test_dataframe)
            if not status:
                error_message = "Test dataframe contains non-numeric columns.\n"

                
        except Exception as e:
            raise NetworkSecurityException(e,sys)