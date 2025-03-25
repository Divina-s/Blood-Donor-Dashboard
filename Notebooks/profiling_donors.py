import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Function to load and process data for Dataset 1
def load_and_process_data1():
    dataset1 = pd.read_csv('profiling_donors_results1.csv')  # Load your dataset1
    dataset1.fillna(method='ffill', inplace=True)  # Data preprocessing
    return dataset1

# Function to load and process data for Dataset 2
def load_and_process_data2():
    dataset2 = pd.read_csv('profiling_donors_results2.csv')  # Load your dataset2
    dataset2.fillna(method='ffill', inplace=True)  # Data preprocessing
    return dataset2

# Streamlit UI
def main():
    st.title("Profiling Ideal Donors")
    
    st.write("""
        This app helps you analyze and visualize donor trends based on demographics. 
        It groups donors by characteristics such as Age, Gender, and Location, and visualizes the trends using clustering techniques.
    """)
    
    # Load and process the data for both datasets
    dataset1 = load_and_process_data1()
    dataset2 = load_and_process_data2()
    
   
    
    
    
    # Visualizations for Dataset 1
    st.subheader("Visualizing Donor Trends - Dataset 1")
    
    # Gender Count Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Genre_', data=dataset1, palette='Set2', ax=ax)
    ax.set_title('Donor Count by Gender (Dataset 1)')
    st.pyplot(fig)

    # Location Count Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Arrondissement_de_résidence_', data=dataset1, palette='Set2', ax=ax)
    ax.set_title('Donor Count by Location (Dataset 1)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)
    
    # Clustering (KMeans) for Dataset 1
    st.subheader("Clustering Donors by Age and Gender (Dataset 1)")
    
    X1 = dataset1[['Age', 'Genre_']]
    X1['Genre_'] = X1['Genre_'].map({'Male': 0, 'Female': 1})  # Label Encoding for 'Genre_'
    
    scaler = StandardScaler()
    X1_scaled = scaler.fit_transform(X1)
    
    kmeans1 = KMeans(n_clusters=3, random_state=42)
    dataset1['Cluster'] = kmeans1.fit_predict(X1_scaled)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=dataset1['Age'], y=dataset1['Genre_'], hue=dataset1['Cluster'], palette='Set1', ax=ax)
    ax.set_title('Clustering Donors by Age and Gender (Dataset 1)')
    st.pyplot(fig)
    
    # PCA for Dataset 1
    pca1 = PCA(n_components=2)
    pca_components1 = pca1.fit_transform(X1_scaled)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=pca_components1[:, 0], y=pca_components1[:, 1], hue=dataset1['Cluster'], palette='Set1', ax=ax)
    ax.set_title('PCA of Clusters (Dataset 1)')
    st.pyplot(fig)

    # Grouping and Analysis for Dataset 2
    st.subheader("Donor Analysis - Dataset 2")
    age_grouped_2 = dataset2.groupby('Age')['Type de donation'].value_counts().unstack().fillna(0)
    st.write("Age Grouped Donors (Dataset 2): ", age_grouped_2)
    
    # Visualizations for Dataset 2
    st.subheader("Visualizing Donor Trends - Dataset 2")
    
    # Donation Type Count Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Type de donation', data=dataset2, palette='Set2', ax=ax)
    ax.set_title('Donor Count by Type of Donation (Dataset 2)')
    st.pyplot(fig)
    
    # Clustering (KMeans) for Dataset 2
    st.subheader("Clustering Donors by Age and Donation Type (Dataset 2)")
    
    X2 = dataset2[['Age', 'Type de donation']]
    dataset2['Type de donation_encoded'] = dataset2['Type de donation'].map({
        'Blood': 0, 'Plasma': 1, 'Platelet': 2
    })
    X2['Type de donation_encoded'] = dataset2['Type de donation_encoded']
    
    scaler2 = StandardScaler()
    X2_scaled = scaler2.fit_transform(X2[['Age', 'Type de donation_encoded']])
    
    kmeans2 = KMeans(n_clusters=3, random_state=42)
    dataset2['Cluster'] = kmeans2.fit_predict(X2_scaled)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=dataset2['Age'], y=dataset2['Type de donation_encoded'], hue=dataset2['Cluster'], palette='Set1', ax=ax)
    ax.set_title('Clustering Donors by Age and Type of Donation (Dataset 2)')
    st.pyplot(fig)
    
    # PCA for Dataset 2
    pca2 = PCA(n_components=2)
    pca_components2 = pca2.fit_transform(X2_scaled)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=pca_components2[:, 0], y=pca_components2[:, 1], hue=dataset2['Cluster'], palette='Set1', ax=ax)
    ax.set_title('PCA of Clusters (Dataset 2)')
    st.pyplot(fig)

    # Add download buttons for saving the processed datasets
    st.subheader("Download Processed Datasets")

    # Save processed dataset1 as CSV
    dataset1.to_csv("data1_processed.csv", index=False)
    st.download_button(
        label="Download Processed Dataset 1",
        data=dataset1.to_csv(index=False).encode('utf-8'),
        file_name="data1_processed.csv",
        mime="text/csv"
    )

    # Save processed dataset2 as CSV
    dataset2.to_csv("data2_processed.csv", index=False)
    st.download_button(
        label="Download Processed Dataset 2",
        data=dataset2.to_csv(index=False).encode('utf-8'),
        file_name="data2_processed.csv",
        mime="text/csv"
    )

# Add the profiling_donors_dashboard function
def profiling_donors_dashboard():
    """
    This function is called in the main_dashboard.py file to trigger the profiling donors page.
    """
    main()

# Run the main function
if __name__ == "__main__":
    main()
