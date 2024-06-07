import pandas as pd
import streamlit as st

from utils import load_header
from generate_pdf import generate_pdf
from graph_functions import sentiment_vs_date, display_target_count, most_common_trigrams, display_word_cloud

df = pd.read_csv('assets/dataset/output.csv')

def construct_pdf():
    fig1 = sentiment_vs_date(df)
    fig2 = display_target_count(df)
    fig3 = most_common_trigrams(df)
    fig4 = display_word_cloud(df, 'Text_Clean')
    
    return generate_pdf(fig1, fig2, fig3, fig4)

def dashboard():
    load_header("Analizar Tweet")
    
    cols = st.columns([5,1])
    
    with cols[0]:
        twitter_url = st.text_input("Paste your link here:", placeholder="https://x.com/Google/status/1790555395041472948")
    
    with cols[1]:
        st.write("<br>", unsafe_allow_html=True)
        submitted = st.button("Submit", use_container_width=True)

    if submitted and len(twitter_url)>0:
        pass
    
    master_df = pd.read_excel('assets/dataset/master_dataframe.xlsx')
    master_df = master_df.astype({'id': str, 'inReplyToId': str, 'Conversation ID': str})
    st.dataframe(master_df, height=350, use_container_width=True)
    
    with st.columns([1,7])[0]:
        st.download_button(label="Download CSV", data="", file_name="output.csv", use_container_width=True)
        st.write("<br><br>", unsafe_allow_html=True)
    
    ################################################################################
    
    load_header("Sentiment Analysis Dashboard")

    col = st.columns([2,2,1.6])

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
                
    with col[2]:
        with st.expander('Posts Analysis Report', expanded=True):
            cols = st.columns(3 )
            with cols[0]:
                st.success("⠀❤️12⠀")
            with cols[1]:   
                st.success("⠀♻️312")
            with cols[2]:
                st.success("⠀🖇️42⠀")
                
            st.write('''
            - **Followers Count**: 5348
            - **Following Count**: 1229
            - **Subject**: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            - **Keywords and Phrases**: `lorem ipsum`, `dolor sit amet`, `consectetur adipiscing elit`.
            - **Overall Sentiment**: :red[**Negative**]
            - **Sentiment Breakdown**:
                - Positive: :green[**0.2**]
                - Neutral: :orange[**0.1**]
                - Negative: :red[**0.7**]
            
            <br>
            <br>
            <br>
            <br>
            <br>
            ''', unsafe_allow_html=True)
            
            
    st.session_state["dashboard_ready"] = True

    with st.columns([1,7])[0]:
        st.download_button(label="Download PDF", data=construct_pdf(), file_name="sentiment_analysis_report.pdf", use_container_width=True)


if __name__=="__main__":

    st.set_page_config(page_title="Sentiment Analysis Dashboard", page_icon="💬", layout="wide")
    with st.spinner("Loading Dashboard..."):
        dashboard()
    
    # pdf =  construct_pdf()
    # print(pdf)