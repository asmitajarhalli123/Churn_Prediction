from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load trained model
model = load_model("churn_model.h5")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    # Convert text to number
    gender = 1 if data["gender"] == "male" else 0
    senior = 1 if data["senior"] == "yes" else 0
    partner = 1 if data["partner"] == "yes" else 0
    dependents = 1 if data["dependents"] == "yes" else 0
    phone = 1 if data["phone"] == "yes" else 0

    # Convert string to float
    tenure = float(data["tenure"])
    monthly = float(data["monthlyCharges"])
    total = float(data["totalCharges"])

    # Create customer array
    customer = np.array([[
        gender,
        senior,
        partner,
        dependents,
        tenure,
        phone,
        monthly,
        total
    ]], dtype=np.float32)

    # Predict
    prediction = model.predict(customer)

    probability = float(prediction[0][0])

    # Result
    if probability > 0.5:
        result = "Customer Will Churn"
    else:
        result = "Customer Will Stay"

    confidence = round(
        probability * 100,
        2
    )

    return jsonify({
        "prediction": result,
        "confidence": confidence
    })


if __name__ == "__main__":
    app.run(
        port=5000,
        debug=True
    )