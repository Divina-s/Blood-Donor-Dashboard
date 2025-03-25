import streamlit as st
import joblib
import pandas as pd
import os 

# Load the trained model
model = joblib.load("src/blood_donation_model.pkl")

image_path = os.path.join(os.path.dirname(__file__), "../resources/images/blooddonor.jpeg")
# Define categorical columns used in training
categorical_columns = [
    "Niveau_scolaire", "Genre_", "Situation_Matrimoniale_(SM)", 
    "Profession_", "Arrondissement_de_résidence_", "Quartier_de_Résidence_", 
    "Nationalité_", "Religion_"
]

#  function for prediction
def predict_eligibility(data):
    df = pd.DataFrame([data])

    # Apply one-hot encoding
    df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

    # Ensure it has the same column structure as training data
    df = df.reindex(columns=X.columns, fill_value=0)

    # Make prediction
    prediction = model.predict(df)
    return "✅ Eligible for Donation" if prediction[0] == 1 else "❌ Not Eligible for Donation"

# Streamlit UI
st.set_page_config(page_title="Blood Donation Predictor", page_icon="💉", layout="wide")

st.markdown(
    """
    <h1 style="text-align: center; color: red;">🩸 Blood Donation Eligibility Predictor 🩸</h1>
    <p style="text-align: center;">Enter donor details to check if they're eligible to donate blood.</p>
    """,
    unsafe_allow_html=True
)

st.sidebar.image(image_path, use_column_width=True)

# User input form
with st.form("donor_form"):
    st.subheader("Enter Donor Details")

    age = st.number_input("Age", min_value=18, max_value=65, step=1, value=25)
    niveau_scolaire = st.selectbox("Education Level", [0, 1, 2, 3])
    genre = st.radio("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    situation_matrimoniale = st.selectbox("Marital Status", [0, 1, 2])
    profession = st.text_input("Profession", "Etudiant (e)")
    arrondissement = st.text_input("Arrondissement", "Douala 3")
    quartier = st.text_input("Quarter", "Yassa")
    nationalite = st.text_input("Nationality", "Camerounaise")
    religion = st.text_input("Religion", "Chretien (Catholique)")
    previous_donation = st.radio("Have you donated blood before?", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

    submitted = st.form_submit_button("Check Eligibility")

if submitted:
    user_data = {
        "Age": age,
        "Niveau_scolaire": niveau_scolaire,
        "Genre_": genre,
        "Situation_Matrimoniale_(SM)": situation_matrimoniale,
        "Profession_": profession,
        "Arrondissement_de_résidence_": arrondissement,
        "Quartier_de_Résidence_": quartier,
        "Nationalité_": nationalite,
        "Religion_": religion,
        "A-t-il_(elle)_déjà_donné_le_sang_": previous_donation
    }

    # Make prediction
    result = predict_eligibility(user_data)

    # Display result with styling
    st.markdown(f"<h2 style='text-align: center; color: green;'>{result}</h2>", unsafe_allow_html=True)

    if "Eligible" in result:
        st.success("You are eligible to donate blood! 💉")
    else:
        st.error("You are not eligible to donate blood at this time. ❌")