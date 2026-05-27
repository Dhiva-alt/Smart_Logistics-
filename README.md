# 🚚 Smart Logistics Delivery Dashboard

A complete Smart Logistics Delivery Dashboard developed using Flask, Machine Learning, SQL, Power BI and Weather API integration. The project analyzes logistics operations, predicts delivery time, provides route insights, displays live tracking and generates business analytics dashboards.

---

# 📌 Project Overview

The Smart Logistics system combines:

- Logistics dataset analysis
- Machine Learning prediction
- Weather-based insights
- Live route tracking
- Interactive chatbot
- Power BI dashboards
- Flask backend APIs

The system helps monitor and optimize delivery operations through analytics and prediction.

---

# ✨ Features

### 📊 Analytics Dashboard
- Delivery performance metrics
- Driver score analysis
- Vehicle analysis
- Route insights
- Traffic analysis

### 🤖 AI Chatbot
- Answers logistics questions
- Delivery insights
- Vehicle statistics
- Driver information
- Distance metrics

### 🌤 Weather Integration
- Live weather API
- Temperature
- Humidity
- Wind speed
- Weather condition monitoring

### 📍 Live Tracking
- Real-time route updates
- Simulated moving driver
- Route monitoring
- Traffic status

### 🧠 Machine Learning
Delivery time prediction using:

- Linear Regression
- Feature encoding
- Data preprocessing

Performance:

- MAE = 7.26
- R² Score = 0.88

---

# 🛠 Technology Stack

| Component | Technology |
|------------|------------|
| Backend | Flask |
| ML | Scikit-Learn |
| Data Processing | Pandas |
| Database | SQL |
| Frontend | HTML/CSS/JavaScript |
| Visualization | Power BI |
| Maps | Leaflet |
| APIs | OpenWeather API |
| Deployment | Render |

---

# 📂 Project Structure

```bash
Smart_Logistics_Backend/
│
├── routes/
│   ├── auth_routes.py
│   ├── chatbot_routes.py
│   ├── weather_routes.py
│   ├── predictions_routes.py
│   ├── live_routes.py
│   ├── report_routes.py
│   └── sla_routes.py
│
├── services/
│   ├── chatbot_service.py
│   ├── report_service.py
│   ├── sla_service.py
│
├── templates/
│   └── driver_dashboard.html
│
├── utils/
│
├── app.py
│
├── requirements.txt
│
└── dataset.csv
```

---

# 📈 Dataset Information

Dataset Name:

Smart Logistics Delivery Dataset

Dataset Size:

1000 Records

Features:

- Distance_km
- Weather
- Traffic_Level
- Vehicle_Type
- Driver_Score
- Courier_Experience
- Time_of_Day
- Delivery_Time_min

Preprocessing:

- Data cleaning
- Feature encoding
- Transformation
- Missing value handling

---

# 🧠 Machine Learning Workflow

Dataset

↓

Data Cleaning

↓

Feature Encoding

↓

Train/Test Split

↓

Linear Regression Model

↓

Prediction

↓

Analytics Dashboard

---

# 🔌 API Documentation

## Chatbot API

```http
POST /chat
```

Request:

```json
{
   "message":"total deliveries"
}
```

Response:

```json
{
   "response":"Total deliveries: 1000"
}
```

---

## Prediction API

```http
GET /predictions
```

Returns prediction metrics.

---

## Weather API

```http
GET /weather
```

Returns:

- Temperature
- Humidity
- Wind speed
- Weather condition

---

## Live Tracking API

```http
GET /live-location
```

Response:

```json
{
   "lat":13.08,
   "lon":80.27,
   "status":"On Route"
}
```

---

# 📷 Dashboard Screenshots

## Home Dashboard

![Overview Dashboard] <img width="1345" height="748" alt="Screenshot 2026-05-27 180000" src="https://github.com/user-attachments/assets/93bcfd82-552b-40b0-9dc8-bc3ee13104a2" />


---

## Route Dashboard
![Route Analysis Dashboard] <img width="1359" height="741" alt="Screenshot 2026-05-27 180040" src="https://github.com/user-attachments/assets/e7fd8cb9-bda0-4319-b68d-e12cf07d48a5" />


---

## Vehicle Dashboard

![Vehicle Performance Dashboard]  <img width="1342" height="754" alt="Screenshot 2026-05-27 180101" src="https://github.com/user-attachments/assets/2b18b8bb-2403-4495-8d97-63e11b15f142" />


---

## Prediction Dashboard

![Prediction Dashboard]<img width="1330" height="745" alt="Screenshot 2026-05-27 180126" src="https://github.com/user-attachments/assets/0200b094-f325-4ebd-9c09-1672c1b52c8e" />


---

## Tracking Dashboard

![Tracking Dashboard]  <img width="1342" height="744" alt="Screenshot 2026-05-27 180147" src="https://github.com/user-attachments/assets/279cb842-a9e5-4e8c-b016-54fce7eaeea3" />


---

## Executive Dashboard
![Executive Dashboard] <img width="1339" height="740" alt="Screenshot 2026-05-27 180204" src="https://github.com/user-attachments/assets/7aa664a1-0e45-4f89-8b6e-0ad5bc6ba2aa" />


---

## Weather Dashboard

![weather Dashboard] <img width="1322" height="751" alt="Screenshot 2026-05-27 180231" src="https://github.com/user-attachments/assets/9804dc28-575f-4cc8-8ff8-f7aab363e36e" />


---

# 🏗 System Architecture

![Architecture Diagram]  <img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/e9e24ba3-0552-424e-9406-d928593f0ec2" />
 

---

# ⚙ Installation Guide

Clone repository:

```bash
git clone your_repository_link
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create:

```env
.env
```

Add:

```env
MAIL_USERNAME=your_mail
MAIL_PASSWORD=your_password
JWT_SECRET_KEY=SmartLogisticsSecret
WEATHER_API_KEY=your_api_key
```

Run:

```bash
python app.py
```

Open:

```bash
http://127.0.0.1:5000
```

---

# 🚀 Deployment

Deployed using Render Cloud Platform.

---

# 🔮 Future Enhancements

- GPS-based live tracking
- Deep learning models
- Role-based authentication
- Notifications and alerts
- Real-time IoT integration
- Route optimization algorithms
- Driver performance recommendations

---

# 👩‍💻 Author
Dhivashini R


Smart Logistics Delivery Dashboard Project
