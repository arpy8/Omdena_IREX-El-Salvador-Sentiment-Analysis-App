import pandas as pd
import streamlit as st

from utils import load_header
from generate_pdf import generate_pdf
from graph_functions import sentiment_vs_date, display_target_count, most_common_trigrams, display_word_cloud
# import hydralit_components as hc
# import time


df = pd.read_csv('assets/dataset/output.csv')

def construct_pdf():
    fig1 = sentiment_vs_date(df)
    fig2 = display_target_count(df)
    fig3 = most_common_trigrams(df)
    fig4 = display_word_cloud(df, 'Text_Clean')
    
    return generate_pdf(fig1, fig2, fig3, fig4)

def dashboard():
    load_header("Sentiment Analysis Dashboard")
    
    with st.container(border=True):
        cols = st.columns([5,2,1,1])
        
        with cols[0]:
            twitter_url = st.text_input("Paste the url of the tweet you want to analyze.", placeholder="https://x.com/Google/status/1790555395041472948")
       
        with cols[1]:
            st.write("<br>", unsafe_allow_html=True)
            submitted = st.button("Submit", use_container_width=True)

        with cols[2]:
            st.write("<br>", unsafe_allow_html=True)
            st.download_button(label="Download PDF", data=construct_pdf(), file_name="sentiment_analysis_report.pdf", use_container_width=True)
        
        with cols[3]:
            st.write("<br>", unsafe_allow_html=True)
            st.download_button(label="Download CSV", data="", file_name="output.csv", use_container_width=True)
        
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
                st.plotly_chart(graph, use_container_width=True)

    st.session_state["dashboard_ready"] = True

if __name__=="__main__":
    # st.set_page_config(layout="wide")

    # with st.spinner("Loading Dashboard..."):
    # # with hc.HyLoader('Loading Dashboard',hc.Loaders.standard_loaders,index=5):
    #     dashboard()
    
    pdf =  construct_pdf()
    print(pdf)