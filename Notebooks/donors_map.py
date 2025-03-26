import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap

def run():
    # Load your donor data (assuming it's in a CSV or a dataframe; update this to reflect your actual data source)
    df_sheet1 = pd.read_csv('donor_distribution_results.csv')  # Replace with your data source
    
    # Filter out rows with missing latitude and longitude values
    df_sheet1 = df_sheet1.dropna(subset=['Latitude', 'Longitude'])

    # Sidebar filter options
    st.sidebar.title("Filters")
    arrondissement_filter = st.sidebar.multiselect(
        "Select Arrondissements:",
        options=df_sheet1['Arrondissement_de_résidence_'].unique(),
        default=[]  # No pre-selection
    )
    profession_filter = st.sidebar.multiselect(
        "Select Profession:",
        options=df_sheet1['Profession_'].unique(),
        default=[]  # No pre-selection
    )
    
    # Filter data based on the sidebar selections
    if arrondissement_filter:
        df_filtered = df_sheet1[df_sheet1['Arrondissement_de_résidence_'].isin(arrondissement_filter)]
    else:
        df_filtered = df_sheet1
    
    if profession_filter:
        df_filtered = df_filtered[df_filtered['Profession_'].isin(profession_filter)]
    
    # Title for the Streamlit app
    st.title("Blood Donor Dashboard")
    
    # Display metrics in smaller boxes adjacent to each other
    st.markdown("<h3>Metrics</h3>", unsafe_allow_html=True)
    
    # Total donors
    total_donors = df_filtered.shape[0]
    # Count the number of unique professions and locations (arrondissements)
    unique_professions = df_filtered['Profession_'].nunique()
    unique_locations = df_filtered['Arrondissement_de_résidence_'].nunique()

    # Display the metrics in smaller boxes, horizontally adjacent
    st.markdown(f'''
        <div style="display: flex; justify-content: space-between; gap: 20px; padding: 10px 0;">
            <div style="width: 30%; background-color: #f2f2f2; border: 1px solid #ccc; border-radius: 8px; padding: 20px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <h4>Total Donors</h4>
                <p style="font-size: 24px; font-weight: bold; color: #4CAF50;">{total_donors}</p>
            </div>
            <div style="width: 30%; background-color: #f2f2f2; border: 1px solid #ccc; border-radius: 8px; padding: 20px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <h4>Unique Professions</h4>
                <p style="font-size: 24px; font-weight: bold; color: #2196F3;">{unique_professions}</p>
            </div>
            <div style="width: 30%; background-color: #f2f2f2; border: 1px solid #ccc; border-radius: 8px; padding: 20px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                <h4>Unique Locations</h4>
                <p style="font-size: 24px; font-weight: bold; color: #FF5722;">{unique_locations}</p>
            </div>
        </div>
    ''', unsafe_allow_html=True)
    
    # Add spacing between metrics and the map
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Create a map centered around the mean coordinates of the donors (latitude and longitude)
    map_center = [df_filtered['Latitude'].mean(), df_filtered['Longitude'].mean()]
    map_donors = folium.Map(location=map_center, zoom_start=12)
    
    # Add a heatmap layer to highlight areas with more donations
    donor_coords = [[row['Latitude'], row['Longitude']] for index, row in df_filtered.iterrows()]
    HeatMap(donor_coords).add_to(map_donors)
    
    # Add markers for each donor location with updated popup content
    for index, row in df_filtered.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=(f"Arrondissement: {row['Arrondissement_de_résidence_']}<br>"
                   f"Profession: {row['Profession_']}"),
            icon=folium.Icon(color="blue", icon="info-sign"),
            tooltip="Click for details"
        ).add_to(map_donors)
    
    # Title for the map
    st.markdown("<h3>Map Distribution</h3>", unsafe_allow_html=True)
    
    # Show the map in Streamlit
    folium_static(map_donors)

    # Display the filtered dataframe
    if st.checkbox("Show Filtered Data"):
        st.write(df_filtered)
