from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

import os,sys

from networksecurity.entity.artifact_entity import DataTransformationArtifacts, ModelTrainerArtifacts
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.utils.main_utils.utils import save_object, load_object, load_numpy_aaray_data, evaluate_models
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score

##ML Algo

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier,RandomForestClassifier

import mlflow

class ModelTrainer:
    def __init__(self, model_trainer_config:ModelTrainerConfig, data_transformation_artifacts:DataTransformationArtifacts):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifacts = data_transformation_artifacts
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def track_mlflow(self, best_model,classificationmetric):
        with mlflow.start_run():
            f1_score = classificationmetric.f1_score
            precision_score = classificationmetric.precision_score
            recall_score = classificationmetric.recall_score
    
            mlflow.log_metric("f1_score", f1_score)
            mlflow.log_metric("precision_score", precision_score)
            mlflow.log_metric("recall_score", recall_score)
            mlflow.sklearn.log_model(best_model,"model")
    
    
    def train_model(self, x_train,y_train, x_test,y_test):
        models = {
            "Logistic Regression":LogisticRegression(verbose=1),
            "DecisionTree Classifier":DecisionTreeClassifier(),
            "AdaBoost Classifier":AdaBoostClassifier(),
            "GradientBoosting Classifier":GradientBoostingClassifier(verbose=1),
            "RandomForest Classifier":RandomForestClassifier(verbose=1)
        }
        
        params = {
            "DecisionTree Classifier" :{
                "criterion": ['gini', 'entropy', 'log_loss'],
                "splitter": ['best', 'random'],
                "max_features" : [ 'sqrt', 'log2']
            },
            "RandomForest Classifier":{
                "n_estimators": [8,16,32,64,128,256],
                "criterion": ['gini', 'entropy', 'log_loss'],
                "max_features":['sqrt', 'log2']
            },
            "GradientBoosting Classifier":{
                "loss": ['log_loss', 'exponential'],
                "learning_rate": [1,0.1,0.05,0.01],
                "subsample": [0.6,0.7,0.75,0.8,0.85,0.9],
                "max_features": ['sqrt', 'log2']
            },
            "Logistic Regression":{},
            "AdaBoost Classifier":{
                "n_estimators":[8,16,32,64,128,256],
                "learning_rate": [1,0.1,0.05,0.01]
            }
                
            
        }
        model_report:dict = evaluate_models(
            x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models,param=params
            )
        
        best_model_score = max(sorted(model_report.values()))
        
        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]
        best_model = models[best_model_name]
        y_train_pred = best_model.predict(x_train)
        
        classification_train_metric= get_classification_score(y_true=y_train,y_pred=y_train_pred)
        
        ##Track the mlflow for train metric
        self.track_mlflow(best_model=best_model,classificationmetric=classification_train_metric)
        
        y_test_pred = best_model.predict(x_test)
        classification_test_metric = get_classification_score(y_true=y_test,y_pred=y_test_pred)
        
        ##Track the mlflow for test metric
        self.track_mlflow(best_model=best_model,classificationmetric=classification_test_metric)

        preprocessor = load_object(file_path=self.data_transformation_artifacts.transformed_object_file_path)
        
        model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
        os.makedirs(model_dir_path,exist_ok=True)
        
        Network_Model = NetworkModel(preprocessor=preprocessor,model=best_model)
        save_object(self.model_trainer_config.trained_model_file_path, obj=Network_Model)
        
        
        ##Model Trainer Artifacts
        model_trainer_artifacts=ModelTrainerArtifacts(trained_model_file_path=self.model_trainer_config.trained_model_file_path,
                              train_metric_artifacts=classification_train_metric,
                              test_metric_artifacts=classification_test_metric)  
        
        logging.info(f"Model Trainer Artifacts: {model_trainer_artifacts}")
        
        return model_trainer_artifacts
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
            
            
            model = self.train_model(x_train,y_train,x_test,y_test)
        except Exception as e:
            raise NetworkSecurityException(e,sys)