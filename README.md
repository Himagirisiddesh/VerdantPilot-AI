<div align="center">

# 🌾 VerdantPilot AI

**A Django-based smart farming dashboard for crop intelligence.**

Combines a Random Forest crop classifier with live weather, fertilizer guidance, soil health scoring, a yield-potential regressor, a bilingual farmer assistant, and a crop-disease upload placeholder — all in one dashboard.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-backend-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Random%20Forest-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Chart.js](https://img.shields.io/badge/Chart.js-visuals-FF6384?logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)
[![Open-Meteo](https://img.shields.io/badge/Weather-Open--Meteo-0EA5E9)](https://open-meteo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## 📖 Overview

VerdantPilot AI is a startup-style agriculture dashboard that turns raw farm data into actionable guidance. A farmer enters their location and soil parameters, and the system returns ranked crop recommendations, a soil health analysis, fertilizer guidance, and a yield forecast — with a fallback climate model that keeps predictions working even when live weather data isn't available.

## ✨ Features

| Category | Details |
|---|---|
| 🌱 **Crop Recommendations** | Top 3 crop suggestions with confidence scores from a Random Forest classifier |
| 🧪 **Soil Health Analysis** | Nutrient warnings based on soil composition |
| 🌿 **Fertilizer Guidance** | Recommendation logic driven by N, P, K, and pH levels |
| 🌦️ **Live Weather Sync** | Auto-fetches weather via city search or browser geolocation |
| 🌍 **Bilingual UI** | Full English and Kannada language support |
| 🤖 **Farmer Assistant** | Rule-based assistant endpoint for guided Q&A |
| 📈 **Yield Forecasting** | Yield-potential prediction via a dedicated regression model |
| 📷 **Disease Scan (placeholder)** | Optional crop image upload, ready to plug in a real CNN model |
| 🛡️ **Weather Fallback** | Dataset-derived climate medians keep predictions working if live weather fails |
| 📊 **Rich Visuals** | Responsive dashboard cards and Chart.js–powered charts |

## 🏗️ Project Structure

```
recommendation/
  views.py           Django page and API views
  services/           Modular service layer:
                       prediction, agronomy, weather, localization,
                       assistant, and disease-scan logic

templates/
  index.html          Dashboard UI

static/
  style.css           Responsive product styling
  script.js            Frontend interactions, translation, charts,
                       assistant, upload flow

train_model.py         Trains and saves both the crop and yield models
app.py                 Convenience launcher
model_metrics.json      Training evaluation metrics
```

## 🚀 Setup

### 1 · Install dependencies

```bash
pip install -r requirements.txt
```

### 2 · Train the models

```bash
python train_model.py
```

### 3 · Run the app

```bash
python manage.py runserver
```

Open **`http://127.0.0.1:8000/`**

## 📝 Notes

- The crop recommender uses the saved classification model in `crop_model.pkl`.
- The yield forecast uses `yield_model.pkl`. If that file is missing, the app can build a surrogate regressor in memory instead.
- Weather is fetched from **Open-Meteo**. If the live lookup fails, the backend falls back to dataset-derived climate medians so predictions keep working.
- The disease-upload flow is a **placeholder** — designed to be swapped for a real CNN model later.
- `app.py` still works as a convenience launcher for the app.

## 📑 Research Paper Alignment

Use this structure in your paper or project report for publishable clarity.

### System Architecture

- **UI layer** — dashboard, charts, assistant
- **API layer** — `/api/predict`, `/api/weather`, `/api/assistant`, `/api/disease`
- **Service layer** — prediction, weather, agronomy
- **Model artifacts** — `crop_model.pkl`, `yield_model.pkl`, `model_metrics.json`

### DFD Level 0

```
Farmer → Smart Farming System → Recommendation / Insights
```

### DFD Level 1

1. Input + location intake
2. Weather retrieval (live / fallback / manual override)
3. Feature engineering and alignment
4. Classification (`predict_proba`, top-3 ranking)
5. Soil / fertilizer / yield post-processing
6. Dashboard + assistant response generation

### Training Pipeline

1. Data cleaning and null filtering
2. One-hot encoding for `soil_type`
3. Stratified train/test split
4. Random Forest training
5. Evaluation logging to `model_metrics.json`
6. Artifact persistence for consistent inference

### Evaluation Metrics

- Accuracy
- Macro / weighted precision
- Macro / weighted recall
- Macro / weighted F1

*(Generated during training, and consumed in prediction responses.)*

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**Himagiri Siddesh**

---

<div align="center">
Built with Django, scikit-learn, and Chart.js
</div>
