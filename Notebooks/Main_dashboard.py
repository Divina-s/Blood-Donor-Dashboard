import sys
import os
# Add the path to the 'src' folder to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import sentiment_analysis
import st_dep  # Now you can import st_dep from the src folder

def main():
    st.sidebar.title("Dashboard Navigation")
    page = st.sidebar.radio("Select a Page", ["Sentiment Analysis", "Donor Distribution", "Blood Donation Eligibility"])

    if page == "Sentiment Analysis":
        sentiment_analysis.sentiment_analysis_dashboard()  # Call the correct function
    elif page == "Donor Distribution":
        import donors_map  # Ensure donors_map.py exists
        donors_map.run()
    elif page == "Blood Donation Eligibility":
        st_dep.st_dep_dashboard()  # Call the Streamlit code from st_dep.py for prediction

if __name__ == "__main__":
    main()
