🌱 VerdantPilot AI  
🚀 Smart Farming Powered by AI & Machine Learning  

> Transforming agriculture with data-driven crop intelligence 🌾  

🌟 Overview  

VerdantPilot AI is an intelligent farming assistant that helps farmers and researchers **predict the best crop** based on soil and environmental conditions using Machine Learning.

It combines:
- 🌾 Crop Recommendation AI  
- 🌦 Weather-aware insights  
- 🧪 Soil analysis  
- 📊 Smart dashboard UI  

🧠 How It Works  

1. User inputs:
   - Nitrogen (N)
   - Phosphorus (P)
   - Potassium (K)
   - Temperature 🌡
   - Humidity 💧
   - pH ⚗
   - Rainfall 🌧  

2. System processes input using ML model  

3. 🎯 Outputs best crop recommendation  


⚙️ Tech Stack  

🔧 Backend
- Python 🐍  
- Django 🌐 :contentReference[oaicite:1]{index=1}  
- Scikit-learn  

🎨 Frontend
- HTML  
- CSS (Glass UI ✨)  
- JavaScript (API calls) :contentReference[oaicite:2]{index=2}  

📊 Machine Learning
- Random Forest Classifier 🌲  
- Dataset-driven training  


🧩 Features  

✨ Clean and modern UI  
✨ Real-time prediction  
✨ ML-based crop suggestion  
✨ Easy input system  
✨ Fast API response  

📦 VerdantPilot-AI
┣ 📂 templates
┣ 📂 static
┣ 📂 recommendation
┣ 📜 train_model.py
┣ 📜 manage.py
┣ 📜 requirements.txt
┗ 📜 model_metrics.json


⚡ Installation & Setup  

1️⃣ Clone Repository
git clone https://github.com/himagirisiddesh/verdantpilot-ai.git
cd verdantpilot-ai
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Train Model
python train_model.py
4️⃣ Run Server
python manage.py runserver
5️⃣ Open Browser
http://127.0.0.1:8000/
🎯 API Example
POST /predict

{
  "N": 90,
  "P": 40,
  "K": 40,
  "temp": 25,
  "humidity": 60,
  "ph": 6.5,
  "rainfall": 100
}
🧪 Future Improvements

🚀 Improve model accuracy
🚀 Add real-time weather API
🚀 Mobile app integration
🚀 Crop disease detection (CNN)
🚀 Multilingual support

🤝 Contribution

Contributions are welcome!
Feel free to fork, improve, and submit PRs.

📜 License

MIT License

💡 Author

Himagiri Siddesh
🎓 AI & ML Enthusiast | Developer

⭐ Show Your Support

If you like this project:
👉 Star ⭐ the repo
👉 Share with others
 

