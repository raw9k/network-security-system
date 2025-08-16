from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

import os,sys

from networksecurity.entity.artifact_entity import DataTransformationArtifacts, ModelTrainerArtifacts
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.utils.main_utils.utils import save_object, load_object, load_numpy_aaray_data
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score


class ModelTrainer:
    def __init__(self, model_trainer_config:ModelTrainerConfig, data_transformation_artifacts:DataTransformationArtifacts):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifacts = data_transformation_artifacts
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def train_model(self, x_train,y_train):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def initiate_model_trainer(self) -> ModelTrainerArtifacts:
        try:
            train_file_path = self.data_transformation_artifacts.transformed_train_file_path
            test_file_path = self.data_transformation_artifacts.transformed_test_file_path
            
            train_arr = load_numpy_aaray_data(train_file_path)
            test_arr = load_numpy_aaray_data(test_file_path)
            
            x_train, y_train, x_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            
            model = self.train_model(x_train,y_train)
        except Exception as e:
            raise NetworkSecurityException(e,sys)