import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# ==========================================
# LOAD DATASET
# ==========================================

data = pd.read_csv("churn.csv")

data.drop("customerID", axis=1, inplace=True)

data["TotalCharges"] = pd.to_numeric(
    data["TotalCharges"],
    errors="coerce"
)

data.dropna(inplace=True)


# ==========================================
# KEEP IMPORTANT COLUMNS
# ==========================================

data = data[[
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MonthlyCharges",
    "TotalCharges",
    "Churn"
]]


# ==========================================
# TEXT TO NUMBER
# ==========================================

encoder = LabelEncoder()

data["gender"] = encoder.fit_transform(
    data["gender"]
)

data["Partner"] = encoder.fit_transform(
    data["Partner"]
)

data["Dependents"] = encoder.fit_transform(
    data["Dependents"]
)

data["PhoneService"] = encoder.fit_transform(
    data["PhoneService"]
)

data["Churn"] = encoder.fit_transform(
    data["Churn"]
)


# ==========================================
# INPUT OUTPUT
# ==========================================

X = data.drop("Churn", axis=1)

y = data["Churn"]


# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# CREATE MODEL
# ==========================================

model = Sequential()

model.add(Dense(
    10,
    activation="relu",
    input_shape=(X_train.shape[1],)
))

model.add(Dense(
    5,
    activation="relu"
))

model.add(Dense(
    1,
    activation="sigmoid"
))


# ==========================================
# COMPILE MODEL
# ==========================================

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# ==========================================
# TRAIN MODEL
# ==========================================

print("Training Model...")

model.fit(
    X_train,
    y_train,
    epochs=10
)

print("Training Complete!")


# ==========================================
# SAVE MODEL
# ==========================================

model.save("churn_model.h5")

print("Model Saved Successfully!")