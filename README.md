# Network Security System (ML Pipeline)

End‑to‑end machine learning pipeline for network intrusion / anomaly detection. It ingests raw records from MongoDB, validates structure, transforms and engineers features, trains multiple classifiers with hyperparameter tuning, computes classification metrics, and persists reproducible artifacts (preprocessor + model) for deployment.

## Project Description
This project demonstrates a modular, timestamped, artifact‑driven ML workflow targeted at detecting malicious or anomalous network activity. Although no specific dataset is bundled here, the design assumes tabular connection / flow / event logs (e.g. features like duration, protocol, byte counts, flags, categorical identifiers). You can plug in any similar schema via MongoDB.

Core goals:
- Reproducibility (every run generates an isolated artifact set)
- Separation of concerns (ingestion, validation, transformation, training)
- Safe persistence (preprocessing object + final model)
- Extensibility (easily add new models, validation checks, or tracking)

## Key Capabilities
- MongoDB -> Pandas -> Feature Store CSV
- Train/test split persisted once per run
- Basic schema size validation (extendable)
- Transformation pipeline (imputation, encoding/scaling placeholder)
- GridSearchCV model selection (Logistic Regression, Tree, RF, GBM, AdaBoost)
- Classification metrics: F1 / Precision / Recall
- Central logging and structured exceptions
- MLflow integration hooks (optional)
- Artifact versioning + optional cleanup utility

## Architecture Overview
1. Data Ingestion: Pulls collection into DataFrame, cleans sentinel values, exports feature store, produces train/test files.
2. Data Validation: Verifies expected column count (add schema + drift logic).
3. Data Transformation: Builds preprocessing object (e.g. imputers, scalers, encoders), fits on train, applies to both, saves numpy arrays + object.
4. Model Training: Hyperparameter search, selects best estimator, wraps with preprocessing, computes metrics, saves model.
5. Tracking (Optional): MLflow run stub (extend to log params/metrics/artifacts).

## Folder Structure
```
Network Security System/
├── main.py
├── requirement.txt
├── networksecurity/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── entity/
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   ├── exception/
│   ├── logging/
│   ├── utils/
│   │   ├── main_utils/
│   │   │   └── utils.py
│   │   └── ml_utils/
│   │       ├── model/
│   │       │   └── estimator.py
│   │       └── metric/
│   │           └── classification_metric.py
├── Artifacts/ (generated)
└── logs/
```

## Pipeline Stages (High Level)
1. Data Ingestion  
   - Reads MongoDB collection → DataFrame → CSV feature store  
   - Train/test split persisted  
2. Data Validation  
   - Column count checks, (extend: schema + drift)  
3. Data Transformation  
   - Imputation, encoding/scaling (as implemented)  
   - Saves transformed numpy arrays + preprocessing object  
4. Model Training  
   - Defines model + param grids  
   - GridSearchCV tuning; best model chosen by score  
   - Metrics computed & logged  
   - Preprocessor + wrapped model saved  
5. Evaluation / Tracking  
   - Classification metrics (F1, Precision, Recall)  
   - MLflow run hook (extend to log params / artifacts)  

## Artifacts
Each run creates:  
```
Artifacts/<timestamp>/
  data_ingestion/
  data_validation/
  data_transformation/
  model_trainer/
```
You can optionally purge older timestamp folders before a new run (add a cleanup utility).

## Installation
```bash
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirement.txt
```

## Environment Variables (.env)
```
MONGO_DB_URL=mongodb+srv://user:pass@host/db
MLFLOW_TRACKING_URI=http://localhost:5000
```
Add any others (e.g. DB name, collection) if not hardcoded in config_entity.

## Running the Pipeline
```bash
python main.py
```
Logs written to logs/<timestamp>. Check console + log file for stage progress.

## Metrics
ClassificationMetricArtifacts holds numeric F1, precision, recall (ensure computation function returns floats, not function objects). Extend with ROC-AUC if needed.

## MLflow (Optional)
Start MLflow server:
```bash
mlflow ui
```
Then ensure track_mlflow logs params, metrics, and model.

## Cleaning Previous Artifacts (Optional Script)
Add a utility to keep only the latest N runs:
```python
import os, shutil
def retain_latest_artifacts(root="Artifacts", keep=1):
    runs = sorted([d for d in os.listdir(root) if os.path.isdir(os.path.join(root,d))])
    for old in runs[:-keep]:
        shutil.rmtree(os.path.join(root, old))
```
Call before TrainingPipelineConfig initialization.

## Error Handling
Custom NetworkSecurityException wraps original exception with file and line context.

## Logging
Central logger writes INFO/ERROR to timestamped log file + console.

## Extending
- Add schema.yaml + robust validation
- Data drift detection (e.g. Evidently)
- Model registry via MLflow
- Dockerization + CI/CD
- REST inference service (FastAPI)

## Troubleshooting
| Issue | Cause | Fix |
|-------|-------|-----|
| PermissionError saving model | Directory created at file path | Ensure only parent dir made |
| Metrics show function refs | Returned functions not values | Call metric functions |
| NoneType on model_report | evaluate_models missing return | Return report dict |
| Duplicate artifact growth | Timestamp accumulation | Add cleanup utility |

## License
Add LICENSE file as needed.

## Disclaimer
For educational / experimental security ML use; not production hardened.
