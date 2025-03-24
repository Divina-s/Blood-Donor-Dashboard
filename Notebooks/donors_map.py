import streamlit as st
import folium
from streamlit_folium import folium_static

st.title("Donor Distribution Map")

# Create a map (You should define map_donors before using it)
map_donors = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

# Show map in Streamlit
folium_static(map_donors)