# Network Security System (ML Pipeline)

End‑to‑end machine learning pipeline for network security (e.g. intrusion / anomaly detection) using a modular, reproducible, artifact‑driven architecture.

## 1. Features
- Structured pipeline (ingestion → validation → transformation → training → evaluation)
- MongoDB → Feature Store export
- Data validation (schema & drift placeholder)
- Transformation: imputation, preprocessing object persisted
- Model selection via GridSearchCV (multiple classifiers)
- Metrics (F1 / Precision / Recall)
- Centralized exception + logging
- Artifact versioning by timestamp
- MLflow tracking ready (hook points)
- Serialization of preprocessing + model

## 2. Tech Stack
Python, scikit-learn, pandas, numpy, pymongo, PyYAML, dill/pickle, MLflow, dotenv, logging.

## 3. Project Structure
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

## 4. Pipeline Stages (High Level)
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

## 5. Artifacts
Each run creates:  
```
Artifacts/<timestamp>/
  data_ingestion/
  data_validation/
  data_transformation/
  model_trainer/
```
You can optionally purge older timestamp folders before a new run (add a cleanup utility).

## 6. Installation
```bash
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirement.txt
```

## 7. Environment Variables (.env)
```
MONGO_DB_URL=mongodb+srv://user:pass@host/db
MLFLOW_TRACKING_URI=http://localhost:5000
```
Add any others (e.g. DB name, collection) if not hardcoded in config_entity.

## 8. Running the Pipeline
```bash
python main.py
```
Logs written to logs/<timestamp>. Check console + log file for stage progress.

## 9. Metrics
ClassificationMetricArtifacts holds numeric F1, precision, recall (ensure computation function returns floats, not function objects). Extend with ROC-AUC if needed.

## 10. MLflow (Optional)
Start MLflow server:
```bash
mlflow ui
```
Then ensure track_mlflow logs params, metrics, and model.

## 11. Cleaning Previous Artifacts (Optional Script)
Add a utility to keep only the latest N runs:
```python
import os, shutil
def retain_latest_artifacts(root="Artifacts", keep=1):
    runs = sorted([d for d in os.listdir(root) if os.path.isdir(os.path.join(root,d))])
    for old in runs[:-keep]:
        shutil.rmtree(os.path.join(root, old))
```
Call before TrainingPipelineConfig initialization.

## 12. Error Handling
Custom NetworkSecurityException wraps original exception with file and line context.

## 13. Logging
Central logger writes INFO/ERROR to timestamped log file + console.

## 14. Extending
- Add schema.yaml + robust validation
- Data drift detection (e.g. Evidently)
- Model registry via MLflow
- Dockerization + CI/CD
- REST inference service (FastAPI)

## 15. Troubleshooting
| Issue | Cause | Fix |
|-------|-------|-----|
| PermissionError saving model | Directory created at file path | Ensure only parent dir made |
| Metrics show function refs | Returned functions not values | Call metric functions |
| NoneType on model_report | evaluate_models missing return | Return report dict |
| Duplicate artifact growth | Timestamp accumulation | Add cleanup utility |

## 16. License
Add LICENSE file as needed.

## 17. Disclaimer
For educational / experimental security ML use; not production hardened.
