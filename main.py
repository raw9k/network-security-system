from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTranformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig,ModelTrainerConfig

import sys


if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        
        logging.info("Initiate the data Ingestion")
        dataingestionartifact= data_ingestion.initiate_data_ingestion()

        logging.info("Data Initiation Completed")
        
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifacts=dataingestionartifact)
        logging.info("Initiate the data Validation")
        data_validation_artifacts =data_validation.initiate_date_validation()
        logging.info("Completed the data Validation")
        

        
        logging.info("Data Transformation Started")
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTranformation(data_validation_artifacts=data_validation_artifacts,
                                                data_tranformation_config=data_transformation_config)
        
        data_transformation_artifacts  = data_transformation.initiate_data_transformation()

        logging.info("Data Transformation Completed")

        logging.info("Model Trainer Started")
        
        model_trainer_config = ModelTrainerConfig(training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,
                                     data_transformation_artifacts=data_transformation_artifacts)
        
        model_trainer_artifacts = model_trainer.initiate_model_trainer()
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)