from flask import Flask, request, jsonify, render_template
import joblib
import json
import os
from sklearn.preprocessing import LabelEncoder
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter 

app = Flask(__name__)

# Initialize Prometheus metrics
metrics = PrometheusMetrics(app)


# Load the model from the pickle file
dir_path = os.getcwd()
model_path = os.path.join(dir_path, 'saved_model', 'model.pkl')
print("Model path:", model_path) 

with open(model_path, 'rb') as file: 
    model = joblib.load(file)

print(type(model))

# Load JSON data for dropdowns
locations_path = os.path.join(dir_path,  'locations_data.json')
device_types_path = os.path.join(dir_path,  'device_data.json')
print("Locations JSON path:", locations_path)  
print("Device Types JSON path:", device_types_path)  


# Check if JSON files exist and load them
if os.path.exists(locations_path):
    with open(locations_path) as f:
        locations = json.load(f)
else:
    print("Warning: locations.json file not found.")

if os.path.exists(device_types_path):
    with open(device_types_path) as f:
        device_types = json.load(f)
else:
    print("Warning: device_types.json file not found.")

# Load the LabelEncoders
location_encoder = joblib.load(os.path.join(dir_path, 'saved_model', 'location_encoder.pkl'))
device_type_encoder = joblib.load(os.path.join(dir_path, 'saved_model', 'device_type_encoder.pkl'))

# Define metrics for custom monitoring
predictions_total = Counter('predictions_total', 'Total number of predictions')
errors_total = Counter('errors_total', 'Total number of errors encountered')

# Define the route for the home page
@app.route('/')
def home_page():
    return render_template('form.html', locations=locations, device_types=device_types)

# Define the route for predictions
@app.route('/submit', methods=['POST'])
def predict():
    
    try:
        # Get form data
        data = request.form
        amount = float(data['amount'])
        location = data['location']
        device_type = data['device_type']
        age = int(data['age'])
        income = float(data['income'])
        debt = float(data['debt'])
        credit_score = int(data['credit_score'])

        # Transform the categorical data using the loaded encoders
        location_encoded = location_encoder.transform([location])[0]
        device_type_encoded = device_type_encoder.transform([device_type])[0]

        # Create a feature array for prediction (adjust order based on your model)
        features = [[amount, location_encoded, device_type_encoded, age, income, debt, credit_score]]

        # Make prediction
        prediction = model.predict(features)
        result = "Fraud" if prediction[0] == 1 else "Not Fraud"
        
        # Increment the prediction counter
        predictions_total.inc()

        #return render_template('result.html', prediction=result)
        return jsonify({'prediction': result})
    
    except Exception as e:
        print("Error:", str(e))
        errors_total.inc()  # Increment the error countr 
        return jsonify({'error': 'An error occurred during prediction.'}), 500

# Run app
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=8080)
