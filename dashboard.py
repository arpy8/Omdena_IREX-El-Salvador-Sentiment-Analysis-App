import pandas as pd
import streamlit as st
from graph_functions import sentiment_vs_date, display_target_count, most_common_trigrams, display_word_cloud
from utils import load_header


df = pd.read_csv('assets/dataset/output.csv')

def dashboard():
    load_header("Sentiment Analysis Dashboard")
    
    with st.form("tweets_form"):
        cols = st.columns([4,1])
        
        with cols[0]:
            twitter_url = st.text_input("Paste the url of the tweet you want to analyze.", placeholder="https://x.com/Google/status/1790555395041472948")
        with cols[1]:
            st.write("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Submit", use_container_width=True)

        if submitted and len(twitter_url)>0:
            pass

    col = st.columns(2)

    with col[0]:
        plotly_graphs = [
            sentiment_vs_date(df),
            display_target_count(df),
        ]   
        
        for _, graph in plotly_graphs:
            with st.container(border=True):
                st.plotly_chart(graph, use_container_width=True)    

    with col[1]:
        plotly_graphs = [
            most_common_trigrams(df),
            display_word_cloud(df, 'processed_text'),
        ]               

        for _, graph in plotly_graphs:
            with st.container(border=True):
            # st.write(f"<center><h4 style='color:#00000090;font-size: 100%;font-weight: 300;'><b>{title}</b></h4></center>", unsafe_allow_html=True)
                st.plotly_chart(graph, use_container_width=True)
        

if __name__=="__main__":
    st.set_page_config(layout="wide")
    dashboard()