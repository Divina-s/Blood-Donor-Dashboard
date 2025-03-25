# main_dashboard.py

import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import st_dep  # Assuming this is your module with Streamlit code for prediction

# Import profiling donors
import profiling_donors  # Import the script for profiling donors



# Set the page configuration as the very first Streamlit command in your main script
st.set_page_config(page_title="Blood Donation Predictor", page_icon="💉", layout="wide")

def main():
    st.sidebar.title("Dashboard Navigation")
    page = st.sidebar.radio("Select a Page", ["Sentiment Analysis", "Donor Distribution", "Blood Donation Eligibility", "Profiling Donors", "Donor Retention"])

    if page == "Sentiment Analysis":
        import sentiment_analysis
        sentiment_analysis.sentiment_analysis_dashboard()  # Call the correct function
    elif page == "Donor Distribution":
        import donors_map  # Ensure donors_map.py exists
        donors_map.run()
    elif page == "Blood Donation Eligibility":
        # Call the function from st_dep.py to load the UI and handle prediction
        st_dep.blood_donation_predictor()  # Call the Streamlit code for prediction from st_dep.py
    elif page == "Profiling Donors":
        # Link the Profiling Donors functionality
        profiling_donors.profiling_donors_dashboard()  # Call the function for profiling donors from profiling_donors.py
    elif page == "Donor Retention":
        # Link the Donor Retention functionality
        donor_retention.donor_retention_analysis()  # Call the donor retention analysis function

if __name__ == "__main__":
    main()
