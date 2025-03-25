import streamlit as st   
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Blood Donor Dashboard", page_icon="", layout="wide")

# Custom CSS for enhanced visual appearance
st.markdown("""
    <style>
        .css-ffhzg2 { 
            background-color: #f0f4f7; 
            color: #333333; 
            border-radius: 10px; 
            padding: 20px;
            margin-top: 0; /* Remove top margin to eliminate space above title */
        }
        .sidebar .sidebar-content {
            background-color: #f7f7f7;
            color: #333333;
        }
        .stButton>button {
            background-color: #ff6347; 
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }
        .stButton>button:hover {
            background-color: #ff4500;
        }
        .stTitle {
            font-family: "Arial", sans-serif;
            color: #2d3e50;
            margin-top: 0; /* Remove top margin */
        }
        .stSubheader {
            font-family: "Arial", sans-serif;
            color: #4d5b63;
            font-size: 20px;
        }
        .section-divider {
            border-bottom: 1px solid #ddd;
            margin: 30px 0;
        }
        .metrics-boxes {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            gap: 20px;
            margin-top: 20px;
            margin-bottom: 30px;
        }
        .metric {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 25px;
            text-align: center;
            width: 200px;
            height: 160px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: center; /* Center the text vertically */
            align-items: center; /* Center the text horizontally */
            border: 2px solid #e5e5e5;
        }
        .metric h4 {
            margin-bottom: 12px;
            color: #333333;
            font-weight: bold;
            font-size: 16px;
        }
        .metric p {
            font-size: 28px;
            font-weight: bold;
            color: #4CAF50;
            margin: 0; /* Remove any extra margin */
        }
        .metric:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
        }
        .stGraph {
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Function for the sentiment analysis dashboard
def sentiment_analysis_dashboard():
    # Load processed dataset
    df = pd.read_csv("sentiment_analysis_results.csv")

    # Streamlit Dashboard with a clean, bold design
    st.title("Blood Donor Dashboard")

    # Sidebar with a modern design (kept the sidebar intact)
    st.sidebar.header("Filters")
    st.sidebar.markdown("""<div style="background-color: #fafafa; padding: 15px; border-radius: 10px;">Use the filters to adjust the data.</div>""", unsafe_allow_html=True)

    # Multi-select for arrondissement with a unique key
    arrondissements = df["Arrondissement de résidence"].unique()
    selected_arrondissement = st.sidebar.multiselect("Select an arrondissement", arrondissements, key="arrondissement_multiselect_unique")

    # Apply arrondissement filter
    if selected_arrondissement:
        df = df[df["Arrondissement de résidence"].isin(selected_arrondissement)]

    # Sliders for health factors with unique keys
    st.sidebar.subheader("Health Factor Filters")
    
    if "Taux d’hémoglobine" in df.columns:
        min_hb, max_hb = float(df["Taux d’hémoglobine"].min()), float(df["Taux d’hémoglobine"].max())
        hb_range = st.sidebar.slider("Taux d’hémoglobine", min_hb, max_hb, (min_hb, max_hb), key="hb_slider_unique")
        df = df[(df["Taux d’hémoglobine"] >= hb_range[0]) & (df["Taux d’hémoglobine"] <= hb_range[1])]

    if "Poids" in df.columns:
        min_weight, max_weight = float(df["Poids"].min()), float(df["Poids"].max())
        weight_range = st.sidebar.slider("Poids (kg)", min_weight, max_weight, (min_weight, max_weight), key="weight_slider_unique")
        df = df[(df["Poids"] >= weight_range[0]) & (df["Poids"] <= weight_range[1])]

    if "Taille" in df.columns:
        min_height, max_height = float(df["Taille"].min()), float(df["Taille"].max())
        height_range = st.sidebar.slider("Taille (cm)", min_height, max_height, (min_height, max_height), key="height_slider_unique")
        df = df[(df["Taille"] >= height_range[0]) & (df["Taille"] <= height_range[1])]

    # Download Button with better styling
    st.sidebar.subheader("Download Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button("Download CSV", data=csv, file_name="filtered_data.csv", mime="text/csv")

    # Directly display the metrics after the title and space
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    # Title for the metrics section with space below it
    st.subheader("Blood Donor Sentiment Analysis")

    # Add space before metrics
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # Metrics Box Display (OUTSIDE THE WHITE BOX)
    col1, col2, col3, col4 = st.columns(4)  # 4 columns for metrics boxes

    # Metrics for display
    total_donors = df.shape[0]
    positive_donors = df[df["Sentiment de Don"] == "Positive"].shape[0]
    negative_donors = df[df["Sentiment de Don"] == "Negative"].shape[0]
    neutral_donors = df[df["Sentiment de Don"] == "Neutral"].shape[0]

    # Place metrics in each column
    with col1:
        st.markdown(f"""
            <div class="metric">
                <h4>Total Donors</h4>
                <p>{total_donors}</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="metric">
                <h4>Positive Sentiment</h4>
                <p>{positive_donors}</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class="metric">
                <h4>Negative Sentiment</h4>
                <p>{negative_donors}</p>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
            <div class="metric">
                <h4>Neutral Sentiment</h4>
                <p>{neutral_donors}</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # Three Graphs: Sentiment Based on Blood Donation History, Geographic Sentiment Analysis, and Health Factor Analysis
    col1, col2= st.columns(2)

    # Sentiment Based on Blood Donation History (Graph 1)
    with col1:
        st.subheader("Sentiment Based on Donation History")
        if 'Sentiment de Don' in df.columns:
            sentiment_counts = df['Sentiment de Don'].value_counts()
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="Set2", ax=ax)
            ax.set_title("Sentiment of Donors")
            ax.set_ylabel("Count")
            ax.set_xlabel("Sentiment")
            ax.tick_params(axis='x', rotation=45)

            st.pyplot(fig)
        else:
            st.error("The column 'Sentiment de Don' is missing. Check your dataset.")

    # Geographic Sentiment Analysis - Graph 2
    with col2:
        st.subheader("Average Hemoglobin Level by Sentiment")
        if "Taux d’hémoglobine" in df.columns:
            fig, ax = plt.subplots(figsize=(6, 4))
            df.groupby('Sentiment de Don')["Taux d’hémoglobine"].mean().plot(kind='bar', ax=ax, color='skyblue', legend=False)
            ax.set_title("Average Hemoglobin by Sentiment")
            ax.set_ylabel("Hemoglobin Level")
            ax.set_xlabel("Sentiment")
            ax.tick_params(axis='x', rotation=45)
            st.pyplot(fig)
        else:
            st.error("The column 'Taux d’hémoglobine' is missing. Check your dataset.")

    # Health Factor Analysis - Graph 3
    # Sentiment Distribution Map
    if 'Arrondissement de résidence' in df.columns:
        st.subheader("Sentiment Distribution Across Different Regions")
        sentiment_map = df.groupby("Arrondissement de résidence")["Sentiment de Don"].value_counts().unstack().fillna(0)
        fig = px.bar(sentiment_map, x=sentiment_map.index, y=sentiment_map.columns, barmode='stack', title="Sentiment by Region")
        st.plotly_chart(fig, use_container_width=True)

# Run the function to generate the dashboard
if __name__ == "__main__":
    sentiment_analysis_dashboard()
