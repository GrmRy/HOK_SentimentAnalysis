import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="HOK Review Dashboard", layout="wide")
# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('HOK-En-VADER-Analysis.csv')
    # Preprocess dates
    df['at'] = pd.to_datetime(df['at'])
    df['repliedAt'] = pd.to_datetime(df['repliedAt'])
    df['processed_text'] = df['processed_text'].fillna('')  # Replace NaN with empty strings
    df['processed_text'] = df['processed_text'].astype(str)  # Ensure all values are strings
    return df

df = load_data()

# Configure page

st.title("Honor of Kings Review Analysis Dashboard")

# --------------------------
# SECTION 1: KEY METRICS
# --------------------------
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Reviews", len(df))
with col2:
    st.metric("Avg. Sentiment Score", f"{df['sentiment_score'].mean():.2f}")
with col3:
    response_rate = df['replyContent'].notnull().mean() * 100
    st.metric("Response Rate", f"{response_rate:.1f}%")

# --------------------------
# SECTION 2: SENTIMENT & TIME ANALYSIS
# --------------------------
tab1, tab2 = st.tabs(["Sentiment Overview", "Temporal Trends"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        # Sentiment Distribution
        fig = px.pie(df, names='sentiment', title='Sentiment Distribution')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Sentiment vs Score
        fig = px.box(df, x='score', y='sentiment_score', 
                    title='Sentiment Scores by Star Rating')
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    # Time-series analysis
    df_weekly = df.groupby([pd.Grouper(key='at', freq='W'), 'sentiment']).size().reset_index(name='count')
    fig = px.line(df_weekly, x='at', y='count', color='sentiment', 
                 title='Weekly Review Volume by Sentiment')
    st.plotly_chart(fig, use_container_width=True)

# --------------------------
# SECTION 3: TEXT ANALYSIS
# --------------------------
st.header("Complaint Analysis")
col1, col2 = st.columns([2, 3])

with col1:
    # Word Cloud
    st.subheader("Common Themes in Negative Reviews")
    negative_text = ' '.join(df[df['sentiment'] == 'negative']['processed_text'])
    wordcloud = WordCloud(width=800, height=400).generate(negative_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(plt)

with col2:
    # Version Impact
    st.subheader("Version Performance")
    fig = px.bar(df.groupby(['appVersion', 'sentiment']).size().reset_index(name='count'),
                x='appVersion', y='count', color='sentiment',
                title='Review Sentiment by App Version')
    st.plotly_chart(fig, use_container_width=True)

# --------------------------
# SECTION 4: USER ENGAGEMENT
# --------------------------
st.header("User Engagement & Responses")
col1, col2 = st.columns(2)

with col1:
    # Thumbs Up Analysis
    fig = px.scatter(df, x='sentiment_score', y='score',
                    size='thumbsUpCount', title='Review Impact Analysis',
                    labels={'score': 'Star Rating', 'sentiment_score': 'Sentiment Score'})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Response Time Analysis
    st.subheader("Response Time Distribution")
    response_times = df.dropna(subset=['repliedAt'])
    response_times['response_hours'] = (response_times['repliedAt'] - response_times['at']).dt.total_seconds() / 3600
    fig = px.histogram(response_times, x='response_hours', 
                      title='Time to Respond (Hours)')
    st.plotly_chart(fig, use_container_width=True)

# --------------------------
# SECTION 5: RAW DATA EXPLORER
# --------------------------
st.header("Review Explorer")
search_term = st.text_input("Search reviews:")
filtered_df = df[df['content'].str.contains(search_term, case=False, na=False)]
st.dataframe(filtered_df[['at', 'content', 'sentiment', 'thumbsUpCount']], 
            use_container_width=True,
            column_config={
                "content": "Review",
                "at": "Date",
                "thumbsUpCount": "Upvotes"
            })