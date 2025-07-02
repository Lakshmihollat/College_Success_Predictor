# 🎓 College Success Predictor

> Predict a student's GPA based on academic scores, attendance, and activity level — and get personalized tips for improvement.

---

## 💡 About the Project

This is a **machine learning + web app** project I built to understand how academic habits influence student success.

It takes in features like:
- 🧮 Math, Reading, Writing Scores
- 📅 Attendance Percentage
- 💼 Activity Level (1–5)

Then it:
- 🎯 Predicts the student's final semester GPA  
- 📌 Gives smart recommendations like "Increase attendance" or "Participate in more activities"  
- 🌐 Displays it all on a **Flask web app** with a clean UI

---

## 🧠 Tech Stack

| Layer         | Tools Used                          |
|---------------|-------------------------------------|
| Data & ML     | pandas, numpy, scikit-learn         |
| Model         | Random Forest Regressor             |
| Frontend      | HTML, CSS                           |
| Backend       | Flask                               |
| Deployment    | Localhost       |

---

## 📊 Dataset

Used a real-world dataset from **Kaggle's Student Performance Data** and added custom fields like attendance & activity level.

---

## ⚙️ How it Works

1. Cleaned and preprocessed dataset  
2. Visualized correlations and selected top features  
3. Trained and tested ML models (Linear Regression, Random Forest)  
4. Saved best model using `joblib`  
5. Built a **Flask web app** that takes user input, predicts GPA, and shows advice  
6. Added validation, error handling, and polished UI  

---

## 🚀 Run Locally

```bash
git clone https://github.com/Lakshmihollat/college-success-predictor.git
cd college-success-predictor
pip install -r requirements.txt
python app.py
