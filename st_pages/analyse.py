import pandas as pd
import streamlit as st
from utils.scraper import main_tweet_dataframe, comments_dataframe
from utils.utils import load_header, is_valid_twitter_url, combine_author_and_comments_df

def analyse_page():
    load_header("Analizar Tweet")
    
    cols = st.columns([5,1,1])
    
    with cols[0]:
        twitter_url = st.text_input("Paste your link here:", placeholder="https://x.com/Google/status/1790555395041472948")
    
    with cols[1]:
        st.write("<br>", unsafe_allow_html=True)
        submitted = st.button("Submit", use_container_width=True)

    if submitted and not is_valid_twitter_url(twitter_url):
        st.toast("⚠️ Invalid URL")

    if submitted and is_valid_twitter_url(twitter_url):
        if 'master_df' not in st.session_state:
            st.session_state['master_df'] = None

        with st.spinner("Scraping data..."):
            df_author = main_tweet_dataframe(twitter_url)
            df_comments = comments_dataframe(twitter_url)
            
            # df_author = pd.read_csv('assets/dataset/temp_output_author.csv')
            # df_comments = pd.read_csv('assets/dataset/temp_output_comments.csv')
            
            master_df = combine_author_and_comments_df(df_author, df_comments)
            st.session_state['master_df'] = master_df
            
            # master_df = pd.read_csv('assets/dataset/temp_output_combined2.csv')
            # master_df = master_df.astype({'id': str, 'inReplyToId': str})
            # st.session_state['master_df'] = master_df
            
    if 'master_df' in st.session_state and st.session_state['master_df'] is not None:
        st.dataframe(st.session_state['master_df'], height=450, use_container_width=True)
        
        with cols[2]:
            st.write("<br>", unsafe_allow_html=True)
            st.download_button(label="Download CSV",
                               data=st.session_state['master_df'].to_csv(index=False).encode('utf-8'), 
                               file_name="output.csv",
                               use_container_width=True)
            
if __name__=="__main__":
    st.set_page_config(page_title="Sentiment Analysis Dashboard", page_icon="💬", layout="wide")
    with st.spinner("Loading Dashboard..."):
        analyse_page()