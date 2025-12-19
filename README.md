<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python" />
  <img src="https://img.shields.io/badge/Framework-FastAPI-green.svg" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Machine%20Learning-scikit--learn-orange.svg" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/Docker-Enabled-blue.svg" alt="Docker" />
</p>

<h1 align="center">🩺 Diabetes Prediction API uding FastAPI</h1>

---

## Project Summary

This repository contains a **machine learning–powered REST API** built using
**FastAPI** to predict the risk of diabetes based on patient health parameters.
A pre-trained classification model is loaded at runtime and exposed through a
clean, production-style API endpoint.

The project is designed as a **reproducible, deployable ML API**, suitable for
learning how to serve machine learning models using FastAPI and Docker.

This repository is intended for **educational, demonstration, and portfolio use**.

---

## 🔧 Features and Components

- RESTful API built using **FastAPI**
- Pre-trained **scikit-learn** classification model
- Input validation using **Pydantic schemas**
- JSON-based prediction endpoint
- Automatic API documentation via Swagger & ReDoc
- Dockerized for easy deployment
- Clean and minimal project structure

---

## 🧰 Project Structure

```bash
diabetes-prediction-api/
│
├── model/                 # Trained ML model (pickle / joblib)
├── app.py                 # FastAPI application entry point
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── .gitignore
└── README.md
```

## 🧠 Model Details

- The prediction model is trained using **scikit-learn**
- It is a supervised classification model trained on a diabetes dataset
- Input features represent common clinical indicators, including:
  - Height
  - Weight
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI (Calculated from weight and height attribute)
  - Diabetes Pedigree Function
  - Age
- The model outputs a **binary classification result**:
  - `0` → Non-Diabetic
  - `1` → Diabetic

> Note: This API performs **risk prediction**, not medical diagnosis.

---

## 🧪 Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- scikit-learn
- pandas
- joblib / pickle

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API Locally

### Clone the repository
```bash
git clone https://github.com/ChiragMinds/diabetes-prediction-api.git
cd diabetes-prediction-api
```

### Start the FastAPI server
```bash
uvicorn app:app --reload
```

---

## 📌 API Endpoint

### POST `/predict`

Predict diabetes risk using patient health parameters.

## 📘 API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs  

---

## 🐳 Docker Support

### Docker Image

The Docker image for this project is available on Docker Hub:

🔗 https://hub.docker.com/r/chirag1415/diabetes-prediction-api

### Pull the Image

```bash
docker pull chirag1415/diabetes-prediction-api:latest
```
### Run the Container

```bash
docker run -p 8000:8000 chirag1415/diabetes-prediction-api
```

---

## ⚠️ Notes and Limitations

- This project is intended for **educational and demonstration purposes only**
- It does **not** replace professional medical advice
- Avoid exposing the API publicly without authentication and rate limiting

---

## Authors and Contact

- **Chirag Chauhan**  
  📧 chiragchauhan1401@gmail.com

