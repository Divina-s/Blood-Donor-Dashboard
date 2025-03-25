from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel

# Load the trained model
model = joblib.load("./models/blood_donation_model.pkl")
feature_columns = joblib.load("./models/feature_columns.pkl")

# Define categorical columns used in training
categorical_columns = ["Niveau_scolaire", "Genre_", "Situation_Matrimoniale_(SM)", 
                       "Profession_", "Arrondissement_de_résidence_", "Quartier_de_Résidence_", 
                       "Nationalité_", "Religion_"]

# Initialize FastAPI app
app = FastAPI(title="Blood Donation Eligibility API")

# Define input schema using Pydantic
class DonorData(BaseModel):
    Age: int
    Niveau_scolaire: int
    Genre_: int
    Situation_Matrimoniale_: int
    Profession_: str
    Arrondissement_de_résidence_: str
    Quartier_de_Résidence_: str
    Nationalité_: str
    Religion_: str
    A_t_il_elle_déjà_donné_le_sang_: int

# Define a function for prediction
def predict_eligibility(new_data):
    new_data_df = pd.DataFrame([new_data.dict()])

    # Check for missing categorical columns
    for col in categorical_columns:
        if col not in new_data_df.columns:
            new_data_df[col] = "Unknown"  # Provide a default value

    # Apply one-hot encoding (ensure it matches training format)
    new_data_df = pd.get_dummies(new_data_df, columns=categorical_columns, drop_first=True)

    # Ensure the DataFrame has the same structure as the trained model
    new_data_df = new_data_df.reindex(columns=feature_columns, fill_value=0)

    # Make prediction
    prediction = model.predict(new_data_df)

    return "Eligible for donation ✅" if prediction[0] == 1 else "Not eligible ❌"

# Define FastAPI endpoint
@app.post("/predict")
def predict(donor: DonorData):
    result = predict_eligibility(donor)
    return {"eligibility": result}

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Blood Donation Eligibility Prediction API"}