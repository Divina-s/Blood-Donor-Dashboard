# Blood Donation Campaign Dashboard

## Project Overview
The Blood Donation Campaign Dashboard is an interactive tool designed to aid blood donation campaigns by providing data-driven insights. This dashboard helps users analyze donor behavior, campaign success, and eligibility criteria using data visualization and machine learning. By leveraging these insights, organizations can optimize strategies and effectively target potential donors.

## Features
### Data Visualization
- **Donor Distribution Mapping**: Displays geographic locations of donors using interactive maps.
- **Health Condition Analysis**: Visualizes the impact of conditions like hypertension and diabetes on donor eligibility.
- **Donor Retention Analysis**: Identifies repeat donors and trends in retention.
- **Campaign Effectiveness Tracking**: Analyzes past campaign success through participation trends.
- **Sentiment Analysis**: Extracts donor feedback insights using natural language processing.

### Machine Learning
- **Eligibility Prediction Model**: A real-time machine learning model predicts donor eligibility based on health and demographic data.

## Tools & Libraries Used
### Data Analysis & Visualization
- **Pandas**: Data cleaning and manipulation
- **Matplotlib / Seaborn**: Static visualizations
- **Plotly**: Interactive charts and graphs
- **Geopandas**: Mapping donor locations
- **Folium**: Interactive geographical visualizations
- **Streamlit**: Dashboard development

### Machine Learning
- **Scikit-learn**: Eligibility prediction model
- **NLTK / TextBlob**: Sentiment analysis on donor feedback
- **FastAPI**: API for real-time predictions

## Project Workflow
1. **Data Cleaning**: Handle missing values, standardize formats, and prepare data for analysis.
2. **Dashboard Development**: Build an interactive dashboard using dirty data as a placeholder.
3. **Data Integration**: Replace dirty data with cleaned, finalized data.
4. **Machine Learning Model**: Train an eligibility prediction model and integrate it via FastAPI.
5. **Code Review & Refinements**: Collaborate via pull requests and merge reviewed code.
6. **Final Testing**: Ensure all components function as expected.

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Git
- Virtual Environment (recommended)

### Installation Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. **Create a Virtual Environment & Install Dependencies**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Run the Dashboard**
   ```sh
   streamlit run app.py
   ```
4. **Run the FastAPI Model Server**
   ```sh
   uvicorn model_api:app --reload
   ```

## Using the Dashboard
- Navigate to `http://localhost:8501` to explore the visualizations and insights.
- Input donor information to check real-time eligibility predictions.

## API Usage (Machine Learning Predictions)
The FastAPI server provides a REST API for real-time eligibility predictions.
### Endpoint
```sh
POST /predict
```
### Request Format
```json
{
   "age": 30,
   "blood_pressure": "normal",
   "diabetes": "no",
   "previous_donations": 3
}
```
### Response Format
```json
{
   "eligibility": "eligible",
   "confidence": 0.89
}
```

## Collaboration & Code Contribution
- **Branching Strategy**: Each contributor must work on a personal branch and submit changes via pull requests.
- **Code Reviews**: Changes will be reviewed before merging to the main branch.
- **Commenting**: Ensure all code is well-documented and follows best practices.

## Assumptions & Considerations
- **Data Privacy**: All personal identifiers have been anonymized.
- **Data Imbalance**: Certain eligibility groups might be underrepresented, which could affect the model's performance.
- **Performance**: The eligibility prediction model is optimized for efficiency but may require future improvements.

## Authors & Contributors
- **Divina Mbel** – Geospatial Mapping, Sentiment Analysis, README File
- **Lesly** – Data Cleaning, Donor Profiling, Presentation
- **Raoul** – Health Analysis, Campaign Effectiveness, Donor Retention
- **Tamanji** – Machine Learning Model & FastAPI Integration

## License
This project is open-source and available under the MIT License.

