import pandas as pd
import streamlit as st
from utils.constants import TEXT_COLOR
from utils.generate_pdf import construct_pdf
from utils.utils import load_header, add_columns_for_graphs
from utils.graph_functions import *


def dashboard():        
    master_df = st.session_state['master_df']
    
    if st.session_state['tweet_data'] is None:
        st.session_state['tweet_data'], st.session_state['master_df'] = add_columns_for_graphs(master_df)
    tweet_data = st.session_state['tweet_data']
    
    load_header("Sentiment Analysis Dashboard")
    metrics_bar(tweet_data, master_df)
    
    cols = st.columns([2, 2, 1.6])
    
    with cols[0]:
        if st.session_state['sentiment_over_date'] is None and st.session_state['display_target_count'] is None:
            st.session_state['sentiment_over_date'] = sentiment_over_date(master_df)
            st.session_state['display_target_count'] = display_target_count(master_df)
        
        for graph in [st.session_state['sentiment_over_date'], st.session_state['display_target_count']]:
            with st.container(border=True):
                st.plotly_chart(graph, use_container_width=True)
                
    with cols[1]:
        if st.session_state["most_common_trigrams"] is None and st.session_state["display_word_cloud"] is None:
            st.session_state["most_common_trigrams"] = most_common_trigrams(master_df)
            st.session_state["crear_grafico_dispersion"] = crear_grafico_dispersion(master_df)
        
        # for graph in [st.session_state["most_common_trigrams"], st.session_state["display_word_cloud"]]:
        for graph in [st.session_state["most_common_trigrams"], st.session_state["crear_grafico_dispersion"]]:
            with st.container(border=True):
                st.plotly_chart(graph, use_container_width=True)
    
    with cols[2]:
        with st.container(border=True):
            # st.write("###### Post Analysis Report")
            cols = st.columns(2)
            with cols[0]:
                st.metric(label="Views 👁️", value=tweet_data["viewCount"])
                st.metric(label="Likes ❤️", value=tweet_data["likeCount"])
                st.metric(label="Retweets 🔁", value=tweet_data["retweetCount"])
                st.download_button(label="Download PDF", data=construct_pdf(), file_name="sentiment_analysis_report.pdf", use_container_width=True)
            with cols[1]:
                st.metric(label="Followers 👥", value=tweet_data["author__followers"])
                st.metric(label="Replies 💬", value=tweet_data["replyCount"])
                st.metric(label="Is Verified 🔐", value=tweet_data["is_author_verified"])
                st.link_button("Go to Tweet", url=tweet_data["url"], use_container_width=True)
                
        with st.container(border=True):
            st.session_state["display_word_cloud"] = display_word_cloud(master_df)
            st.plotly_chart(st.session_state["display_word_cloud"], use_container_width=True)

            # st.write("###### Sentiment Breakdown")
            # pos, neu, neg = st.columns(3)
            # st.info(f"##### **Overall Sentiment**: :{TEXT_COLOR[tweet_data['overall_sentiment'].lower()]}[**{tweet_data['overall_sentiment']}**]")
            # pos.metric(label=":green[Positive]", value=tweet_data["positive"])
            # neu.metric(label=":gray[Neutral]", value=tweet_data["neutral"])
            # neg.metric(label=":red[Negative]", value=tweet_data["negative"])
            
    with st.container(border=True):
        st.plotly_chart(stacked_bar_fig(master_df), use_container_width=True)
        
    
if __name__ == "__main__":
    from utils.utils import init_session_state

    st.set_page_config(page_title="Sentiment Analysis Dashboard", page_icon="💬", layout="wide")
    init_session_state()

    df = pd.read_csv('assets/dataset/master.csv')
    st.session_state['master_df'] = pd.read_csv('assets/dataset/temp_output_combined.csv')

    df_author = pd.read_csv('assets/dataset/temp_output_author.csv')
    df_comments = pd.read_csv('assets/dataset/temp_output_comments.csv')
    
    # with st.spinner("Analyzing Tweets..."):
    #     master_df, tweet_data = construct_master_df(df_author, df_comments)
    
    # with st.spinner("Loading Dashboard..."):
        # dashboard(master_df, tweet_data)