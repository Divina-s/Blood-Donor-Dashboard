import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import streamlit as st
import sentiment_analysis 

def main():
    st.sidebar.title("Dashboard Navigation")
    page = st.sidebar.radio("Select a Page", ["Sentiment Analysis", "Donor Distribution"])

    if page == "Sentiment Analysis":
        sentiment_analysis.sentiment_analysis_dashboard()  # Call the correct function
    elif page == "Donor Distribution":
        import donors_map  # Ensure donors_map.py exists
        donors_map.run()

if __name__ == "__main__":
    main()
