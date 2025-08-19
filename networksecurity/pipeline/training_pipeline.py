import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTranformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

from networksecurity.entity.artifact_entity import(
    DataIngestionArtifacts,
    DataTransformationArtifacts,
    DataValidationArtifacts,
    ModelTrainerArtifacts
)

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_Config = TrainingPipelineConfig()
        
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_Config)
            logging.info("Initiate the data Ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            dataingestionartifact= data_ingestion.initiate_data_ingestion()
            logging.info(f"Data initiation has completed and artifact :{dataingestionartifact} is created")
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_validation(self, dataingestionartifact:DataIngestionArtifacts):
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_Config)
            data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifacts=dataingestionartifact)
            logging.info("Initiate the data Validation")
            data_validation_artifacts =data_validation.initiate_date_validation()
            logging.info("Completed the data Validation")
            return data_validation_artifacts
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)    
    
    
    def start_data_transformation(self,data_validation_artifacts:DataValidationArtifacts):
        try:
            logging.info("Data Transformation Started")
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_Config)
            data_transformation = DataTranformation(data_validation_artifacts=data_validation_artifacts,
                                                data_transformation_config=data_transformation_config)
        
            data_transformation_artifacts  = data_transformation.initiate_data_transformation()
            logging.info("Data Transformation Completed")
            return data_transformation_artifacts
        except Exception as e:
            raise NetworkSecurityException(e,sys)
     
    def start_model_trainer(self,data_transformation_artifacts:DataTransformationArtifacts) -> ModelTrainerArtifacts:
        try:
            self.model_trainer_config: ModelTrainerConfig= ModelTrainerConfig(training_pipeline_config=self.training_pipeline_Config)
            model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config,
                                     data_transformation_artifacts=data_transformation_artifacts)
        
            model_trainer_artifacts = model_trainer.initiate_model_trainer()   
        except Exception as e:
            raise NetworkSecurityException(e,sys)   
        
    def run_pipeline(self):
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validation_artifacts = self.start_data_validation(dataingestionartifact=data_ingestion_artifacts)
            data_transformation_artifacts = self.start_data_transformation(data_validation_artifacts=data_validation_artifacts)
            model_trainer_artifacts = self.start_model_trainer(data_transformation_artifacts=data_transformation_artifacts)
            return model_trainer_artifacts
        except Exception as e:
            raise NetworkSecurityException(e,sys) 