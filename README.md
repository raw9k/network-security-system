# 🛡️ Network Security System

## 📌 Overview
The **Network Security System** is an end-to-end **phishing detection pipeline** built with **FastAPI** and modular ML components.  
It allows users to either:  
1. **Upload a CSV file** for batch phishing detection (results shown in an HTML table).  
2. **Use the REST API** endpoints programmatically for training and prediction.  

The system demonstrates **production-style ML engineering practices**, including modular pipelines, centralized logging, Docker-based deployment, and integration with cloud platforms (Azure).

---

## 🚀 Live Demo  

🌐 Web App: https://networksecurity-h4hsc3bph3fmevfq.centralus-01.azurewebsites.net  
📦 Docker Hub: https://hub.docker.com/r/raw9k/network-security-app  

---

## ⚙️ Features

- **Training Pipeline**: Retrain the phishing detection model via API (`/train`).  
- **Batch Prediction**: Upload CSVs for phishing detection; results saved as CSV and rendered as HTML tables.  
- **Dual Usage**: Accessible both through a **browser-based interface** and **API clients** (e.g., Postman, curl).  
- **Optional Database Support**: MongoDB integration for ingestion (can be disabled in deployment).  
- **Cloud-Ready Deployment**: Containerized with Docker, deployed on **Azure Web App for Containers**.  
---

## 🧑‍💻 Usage  

### 1. Web Interface  
- Go to the deployed Azure app.  
- Upload a CSV file containing URL features.  
- Receive phishing detection results in a **styled HTML table** with summary statistics.  

### 2. API Endpoints:  
- `GET /` → Redirects to API docs.  
- `POST /predict` → Upload a CSV file for predictions (returns results as JSON or HTML).  
- `GET /train` → Retrains the ML pipeline (requires MongoDB).

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+  
- **Backend**: FastAPI, Starlette, Uvicorn  
- **Machine Learning**: Scikit-learn, Pandas, Numpy  
- **Deployment**: Docker, Azure Web App  
- **Optional Storage**: MongoDB (for ingestion + retraining)  
- **Templating**: Jinja2 + Bootstrap (UI for CSV upload & results)  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+  
- Docker (optional, for containerized deployment)  
- MongoDB instance *(only required if you want retraining from raw data ingestion)*  

### Installation

```bash
git clone https://github.com/raw9k/network-security-system.git
cd network-security-system
pip install -r requirements.txt
```
### Run Locally
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
Now you can access the system:

API Docs → http://127.0.0.1:8000/docs

Home Page → http://127.0.0.1:8000/

### 🐳 Docker Deployment
Build and run the Docker container:
```bash
docker build -t network-security-system .
docker run -p 8000:8000 network-security-system
```
### 📊 Example Workflow

1. Open the home page in browser: http://localhost:8000
2. Upload a CSV file of URL features for batch analysis.
3. View phishing predictions in a styled HTML table.
4. Or, go to /docs for Swagger UI to interact with the API.

### ☁️ Deployment on Azure

1. Built into a Docker image and deployed to Azure Web App for Containers.
2. Supports both batch file uploads and REST API usage.
3. CI/CD integration possible via GitHub Actions.

---

## 📝 Conclusion

The Network Security System combines machine learning, REST APIs, and cloud deployment into a single project.
With its modular design, Docker support, and Azure deployment, it serves as a strong prototype for real-world phishing detection systems, suitable for browser plugins, secure email gateways, and enterprise security monitoring.
