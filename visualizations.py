import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

def display_key_metrics(data):
    st.title("Honor of Kings Review Analysis Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Reviews", len(data))
    with col2:
        st.metric("Avg. Sentiment Score", f"{data['sentiment_score'].mean():.2f}")
    with col3:
        response_rate = data['replyContent'].notnull().mean() * 100
        st.metric("Response Rate", f"{response_rate:.1f}%")
    with col4:
        median_response = data['response_hours'].median()
        st.metric("Median Response Time (hrs)", f"{median_response:.1f}")

def sentiment_time_analysis(data):
    tab1, tab2, tab3 = st.tabs(["Sentiment Overview", "Temporal Trends", "Advanced Analytics"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            fig_pie = px.pie(data, names='sentiment', title='Sentiment Distribution', template="plotly_white")
            st.plotly_chart(fig_pie, use_container_width=True)
        with col2:
            fig_box = px.box(data, x='score', y='sentiment_score', title='Sentiment Scores by Star Rating',
                             template="plotly_white", points="all", hover_data=['content'])
            st.plotly_chart(fig_box, use_container_width=True)
    
    with tab2:
        df_weekly = data.groupby([pd.Grouper(key='at', freq='W'), 'sentiment']).size().reset_index(name='count')
        fig_line = px.line(df_weekly, x='at', y='count', color='sentiment',
                           title='Weekly Review Volume by Sentiment', template="plotly_white")
        st.plotly_chart(fig_line, use_container_width=True)
    
    with tab3:
        st.subheader("Correlation Analysis")
        corr_features = ['score', 'sentiment_score', 'thumbsUpCount', 'response_hours']
        corr_df = data[corr_features].dropna()
        corr_matrix = corr_df.corr()
        fig_corr = px.imshow(corr_matrix, text_auto=True, title="Correlation Matrix", template="plotly_white")
        st.plotly_chart(fig_corr, use_container_width=True)
        
        # Outlier detection for thumbsUpCount
        threshold = data['thumbsUpCount'].quantile(0.95)
        outliers = data[data['thumbsUpCount'] > threshold]
        st.write(f"Outlier Reviews (Thumbs Up > {threshold:.0f}):")
        st.dataframe(outliers[['at', 'content', 'thumbsUpCount']])

def text_analysis(data):
    st.header("Complaint Analysis")
    col1, col2 = st.columns([2, 3])
    
    with col1:
        sentiment_choice = st.selectbox("Select Sentiment for Word Cloud", options=['negative', 'positive'])
        selected_text = ' '.join(data[data['sentiment'] == sentiment_choice]['processed_text'])
        st.subheader(f"Common Themes in {sentiment_choice.capitalize()} Reviews")
        if selected_text:
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(selected_text)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            st.pyplot(plt)
            plt.clf()
        else:
            st.write("No text available for the selected sentiment.")
    
    with col2:
        df_version = data.groupby(['appVersion', 'sentiment']).size().reset_index(name='count')
        df_version = df_version.sort_values(by='appVersion')
        fig_bar = px.bar(df_version, x='appVersion', y='count', color='sentiment',
                         title='Review Sentiment by App Version', template="plotly_white")
        st.plotly_chart(fig_bar, use_container_width=True)

def user_engagement(data):
    st.header("User Engagement & Responses")
    col1, col2 = st.columns(2)
    
    with col1:
        fig_scatter = px.scatter(data, x='sentiment_score', y='score', size='thumbsUpCount',
                                 title='Review Impact Analysis',
                                 labels={'score': 'Star Rating', 'sentiment_score': 'Sentiment Score'},
                                 template="plotly_white", hover_data=['at', 'content'])
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with col2:
        response_times = data.dropna(subset=['repliedAt'])
        fig_hist = px.histogram(response_times, x='response_hours', nbins=20,
                                title='Time to Respond (Hours)', template="plotly_white")
        st.plotly_chart(fig_hist, use_container_width=True)
        st.write("Mean Response Time (hrs):", f"{response_times['response_hours'].mean():.1f}")
        st.write("Median Response Time (hrs):", f"{response_times['response_hours'].median():.1f}")

def raw_data_explorer(data):
    st.header("Review Explorer")
    search_term = st.text_input("Search reviews:")
    if search_term:
        explorer_df = data[data['content'].str.contains(search_term, case=False, na=False)]
    else:
        explorer_df = data
    st.dataframe(explorer_df[['at', 'content', 'sentiment', 'thumbsUpCount']], 
                 use_container_width=True,
                 column_config={"content": "Review", "at": "Date", "thumbsUpCount": "Upvotes"})
