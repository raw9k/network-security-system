from datetime import datetime
import os
from networksecurity.constants import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self,timestamp = datetime.now()):
        pass


class DataIngestionConfig:
    def __init__(self, training_pipeline_config):
        pass