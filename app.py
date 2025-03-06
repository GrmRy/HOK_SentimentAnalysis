import streamlit as st
from data import load_data
from filters import sidebar_filters, filter_data
from visualizations import (
    display_key_metrics,
    sentiment_time_analysis,
    text_analysis,
    user_engagement,
    raw_data_explorer
)

# Set page configuration
st.set_page_config(page_title="HOK Review Dashboard", layout="wide")

# Load and cache data
@st.cache_data
def get_data():
    return load_data()

df = get_data()

# Apply sidebar filters
start_date, end_date, selected_sentiments, score_range, selected_versions = sidebar_filters(df)
filtered_df = filter_data(df, start_date, end_date, selected_sentiments, score_range, selected_versions)

# Display dashboard sections
display_key_metrics(filtered_df)
sentiment_time_analysis(filtered_df)
text_analysis(filtered_df)
user_engagement(filtered_df)
raw_data_explorer(filtered_df)
