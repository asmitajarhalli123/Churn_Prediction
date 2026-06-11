from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load trained model
model = load_model("churn_model.h5")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    # Convert values
    gender = 1 if data["gender"] == "male" else 0
    senior = 1 if data["senior"] == "yes" else 0
    partner = 1 if data["partner"] == "yes" else 0
    dependents = 1 if data["dependents"] == "yes" else 0
    phone = 1 if data["phone"] == "yes" else 0

    customer = np.array([[

        gender,
        senior,
        partner,
        dependents,
        data["tenure"],
        phone,
        data["monthlyCharges"],
        data["totalCharges"]

    ]])

    prediction = model.predict(customer)

    probability = float(prediction[0][0])

    result = (
        "Customer Will Churn"
        if probability > 0.5
        else "Customer Will Stay"
    )

    return jsonify({
        "prediction": result,
        "probability": probability
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)