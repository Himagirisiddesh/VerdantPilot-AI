<<<<<<< HEAD
# VerdantPilot AI

VerdantPilot AI is a Django-based smart farming dashboard for crop intelligence. It combines a Random Forest crop classifier with live weather, fertilizer guidance, soil health scoring, a yield-potential regressor, a farmer assistant, bilingual UI support, and a crop disease upload placeholder.

## What is included

- Startup-style agriculture dashboard with responsive cards, layered visuals, and Chart.js charts
- Top 3 crop recommendations with confidence scores
- Soil health analysis with nutrient warnings
- Fertilizer recommendation logic based on N, P, K, and pH
- Auto weather sync from city search or browser geolocation
- English and Kannada UI support
- Rule-based farmer assistant endpoint
- Yield potential forecast using a regression model
- Optional crop image upload with a CNN placeholder disease scan
- Weather fallback profile so prediction still works if live weather is unavailable

## Project structure

- `recommendation/views.py`: Django page and API views
- `recommendation/services/`: modular service layer for prediction, agronomy, weather, localization, assistant, and disease scan logic
- `templates/index.html`: dashboard UI
- `static/style.css`: responsive product styling
- `static/script.js`: frontend interactions, translation, charts, assistant, upload flow
- `train_model.py`: trains and saves both crop and yield models

## Setup

1. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

2. Train the models:

   ```powershell
   python train_model.py
   ```

3. Run the Django app:

   ```powershell
   python manage.py runserver
   ```

4. Open `http://127.0.0.1:8000/`

## Notes

- The crop recommender uses the saved crop classification model in `crop_model.pkl`.
- The yield forecast uses `yield_model.pkl`. If that file is missing, the app can still build a surrogate regressor in memory.
- Weather is requested from Open-Meteo. If live lookup fails, the backend falls back to dataset-derived climate medians so the experience still works.
- The disease upload flow is a placeholder designed to be swapped with a real CNN model later.
- `app.py` still works as a convenience launcher.

## Research Paper Alignment

Use this structure in your paper and project report for publishable clarity:

- **System architecture diagram**: show UI layer (dashboard, charts, assistant), API layer (`/api/predict`, `/api/weather`, `/api/assistant`, `/api/disease`), service layer (`prediction`, `weather`, `agronomy`), and model artifacts (`crop_model.pkl`, `yield_model.pkl`, `model_metrics.json`).
- **DFD Level 0**: Farmer -> Smart Farming System -> Recommendation/Insights.
- **DFD Level 1**:
  1) Input + location intake
  2) Weather retrieval (live/fallback/manual override)
  3) Feature engineering and alignment
  4) Classification (`predict_proba`, top-3 ranking)
  5) Soil/fertilizer/yield post-processing
  6) Dashboard + assistant response generation
- **Training pipeline**:
  - Data cleaning and null filtering
  - One-hot encoding for `soil_type`
  - Stratified split
  - Random Forest training
  - Evaluation logging to `model_metrics.json`
  - Artifact persistence for consistent inference
- **Evaluation metrics**:
  - Accuracy
  - Macro/weighted precision
  - Macro/weighted recall
  - Macro/weighted F1
  These are generated in training and consumed in prediction responses.
=======
# VerdantPilot-AI
AI-powered smart farming dashboard using Django and Machine Learning for crop recommendation, soil analysis, weather integration, and yield prediction.
>>>>>>> 17a47b0761182573ed805d71b5cd288a99537fc3
