import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

# Load processed dataset
df = pd.read_csv("../resources/dataset/sentiment_analysis_results.csv")

# Streamlit Dashboard
st.title(" Dashboard de Sentiment des Donateurs de Sang")

# Blood Donation Sentiment
st.subheader("1️ Sentiment Basé sur l'Historique de Don")

st.bar_chart(df['Sentiment'].value_counts())

# Geographic Sentiment Analysis
st.subheader("2️ Sentiment par Localisation Géographique")
st.write("Heatmap des taux de dons par arrondissement et quartier")

# Example Heatmap
fig, ax = plt.subplots(figsize=(12, 6))
donation_rates = df.pivot_table(index="Arrondissement", columns="Quartier", values="Taux de Don", aggfunc="mean")
sns.heatmap(donation_rates, cmap="coolwarm", annot=True, ax=ax)
st.pyplot(fig)

# Eligibility Sentiment Analysis
st.subheader("3 Sentiment d'Éligibilité au Don")
st.bar_chart(df.groupby('Sentiment')[['Taux d’hémoglobine', 'Poids', 'Taille']].mean())

st.success("Sentiment analysis displayed successfully.")
