# Network Security System

## 📌 Overview

The **Network Security System** is an end-to-end phishing detection pipeline built with **FastAPI** and modular ML components. It supports on-demand training and batch predictions while rendering results as structured HTML tables. The system demonstrates production-inspired ML engineering practices such as modular pipelines, centralized logging, and containerized deployment.

## ⚙️ Features

* **Training Pipeline**: Retrain the phishing detection model through API.
* **Batch Prediction**: Upload CSV files for predictions; outputs include CSV and HTML visualization.
* **Frontend Integration**: Predictions displayed in tabular format using Jinja2 templates.
* **Database Support**: MongoDB backend connectivity with SSL encryption.
* **Deployment Ready**: Containerized via Docker and served using `uvicorn`.

## 📂 Project Structure

```
Network Security System/
│
├── Network_data/               # Raw dataset and splits
├── networksecurity/            # Core ML pipeline package
│   ├── components/              # Ingestion, validation, transformation, trainer, evaluation
│   ├── config/                  # Configurations and constants
│   ├── entity/                  # Entities for configs and artifacts
│   ├── exception/               # Custom exceptions
│   ├── logging/                 # Logging utilities
│   ├── pipeline/                # Training and prediction orchestration
│   └── utils/                   # Helper and ML utilities
│
├── templates/                  # Jinja2 HTML templates
│   └── table.html               # Table rendering for predictions
│
├── Final_models/               # Serialized model artifacts
├── prediction_output/           # Output predictions
├── app.py                      # FastAPI application entry point
├── Dockerfile                  # Deployment configuration
├── requirements.txt             # Dependencies
└── README.md                    # Documentation (this file)
```

## 🛠️ Tech Stack

* **Programming Language**: Python
* **Frameworks**: FastAPI, Starlette, Jinja2
* **Machine Learning**: scikit-learn, pandas, numpy
* **Database**: MongoDB, pymongo, certifi
* **Deployment**: Docker, Uvicorn

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* MongoDB instance (with connection string in `.env`)
* Docker (optional, for containerized deployment)

### Installation

```bash
git clone <repo_url>
cd network-security-system
pip install -r requirements.txt
```

### Run Locally

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Access API docs at: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

### Docker Deployment

```bash
docker build -t network-security-system .
docker run -p 8000:8000 network-security-system
```

## 📡 API Endpoints

* `GET /` → Redirect to `/docs`
* `GET /train` → Run the training pipeline
* `POST /predict` → Upload CSV, return predictions as HTML table and CSV output

## 📊 Example Workflow

1. Navigate to `/docs` to access Swagger UI.
2. Trigger training via `/train` endpoint.
3. Upload CSV to `/predict` endpoint.
4. View predictions rendered in a browser as a formatted HTML table.

## 🔐 Security & Performance

* SSL-verified MongoDB connections.
* Schema validation during ingestion.
* Efficient batch-oriented predictions.

## 📈 Future Enhancements

* JSON-based single prediction endpoint.
* Interactive web forms for user input.
* Automated retraining and monitoring.
* CI/CD pipeline with unit testing.

## 📝 Conclusion

The **Network Security System** demonstrates a production-ready ML pipeline integrated with FastAPI. With containerization, MongoDB support, and interactive prediction visualization, it can be extended for real-world security domains like **browser plugins, email phishing detection, and enterprise threat monitoring**.
