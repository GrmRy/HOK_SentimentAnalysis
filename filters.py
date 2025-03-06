import streamlit as st

def sidebar_filters(data):
    st.sidebar.header("Filters")
    
    # Date range filter
    min_date = data['at'].min().date()
    max_date = data['at'].max().date()
    date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])
    if isinstance(date_range, list) and len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = min_date, max_date
    
    # Sentiment filter
    sentiment_options = list(data['sentiment'].unique())
    selected_sentiments = st.sidebar.multiselect("Select Sentiment", sentiment_options, default=sentiment_options)
    
    # Score filter
    min_score = int(data['score'].min())
    max_score = int(data['score'].max())
    score_range = st.sidebar.slider("Select Score Range", min_score, max_score, (min_score, max_score))
    
    # App Version filter
    app_versions = data['appVersion'].dropna().unique().tolist()
    selected_versions = st.sidebar.multiselect("Select App Versions", app_versions, default=app_versions)
    
    return start_date, end_date, selected_sentiments, score_range, selected_versions

def filter_data(data, start_date, end_date, sentiments, score_range, versions):
    filtered = data[
        (data['at'].dt.date >= start_date) & 
        (data['at'].dt.date <= end_date) &
        (data['sentiment'].isin(sentiments)) &
        (data['score'] >= score_range[0]) &
        (data['score'] <= score_range[1]) &
        (data['appVersion'].isin(versions))
    ]
    return filtered
