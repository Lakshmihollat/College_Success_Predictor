from flask import Flask, render_template, request
import joblib
import numpy as np
from give_recommendation import give_recommendation

app = Flask(__name__)

# Load model and feature names
model = joblib.load('college_gpa_model.pkl')
features = joblib.load('model_features.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    try:
        attendance = int(request.form['attendance'])
        activity = int(request.form['activity_level'])
        math = int(request.form['math_score'])
        reading = int(request.form['reading_score'])
        writing = int(request.form['writing_score'])
        
        # Arrange input in correct order
        input_data = np.array([[math, reading, writing, attendance, activity]])
        prediction = model.predict(input_data)[0]
        prediction = round(prediction, 2)
        if any([
            attendance > 100 or attendance < 0,
            math > 100 or math < 0,
            reading > 100 or reading < 0,
            writing > 100 or writing < 0,
            activity > 5 or activity < 1
        ]):
            return render_template('index.html', prediction="Invalid Input!", recs=["Please enter values between proper ranges only (0-100 for scores, 1-5 for activity)."])

        # Get recommendation
        recs = give_recommendation(attendance, activity, math, reading, writing)
        
        return render_template('index.html', prediction=prediction, recs=recs)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
