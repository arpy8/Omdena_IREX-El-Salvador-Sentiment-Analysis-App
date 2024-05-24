import streamlit as st
from graph_functions import *

import streamlit.components.v1 as components

def visualization_page():
    df = pd.read_csv('assets/dataset/output.csv')
    
    # fig1, fig2, fig3, fig4 = characters_count_in_the_data(df)
    col = st.columns((2.7, 4, 2.7), gap='medium')

    with col[0]:   
        plotly_graphs = [
            display_word_cloud(df, 'processed_text'),
            display_target_count(df),
            sentiment_vs_date(df)
                # token_counts_with_simple_tokenizer(df),
        ]   
        
        for title, graph in plotly_graphs:
            # st.write(f"<center><h4 style='color:#00000090;font-size: 100%;font-weight: 300;'><b>{title}</b></h4></center>", unsafe_allow_html=True)
            st.plotly_chart(graph, use_container_width=True)    

        # matplotlib_graphs = [
        #     fig1, 
        #     fig3
        # ]
        
        # for title, graph in matplotlib_graphs:
        #     # st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
        #     st.pyplot(graph, use_container_width=True) 

    with col[1]:
        # plotly_graphs = [   
            # token_counts_With_bert_tokenizer(df),
        # ]
        
        # for title, graph in plotly_graphs:
        #     st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
        #     st.plotly_chart(graph, use_container_width=True)
        with st.form("tweets_form"):
            slider_val = st.text_input("Paste the url of the tweet you want to analyze.", value="https://x.com/Google/status/1790555395041472948")

            components.html("""<center><blockquote class="twitter-tweet"><p lang="en" dir="ltr">Love this</p>&mdash; maa linga bhairvi (@anilsingh88888) <a href="https://twitter.com/anilsingh88888/status/1793029725276803441?ref_src=twsrc%5Etfw">May 21, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></center>""", 
                            scrolling=False, height=150)
            
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write("slider", slider_val)
                        
        title, graph = most_common_trigrams(df)
        st.write(f"<center><h4 style='color:#00000090;font-size: 100%;font-weight: 300;'><b>{title}</b></h4></center>", unsafe_allow_html=True)
        st.plotly_chart(graph, use_container_width=True)
        
    with col[2]:
        plotly_graphs = [
            # token_counts_With_bert_tokenizer(df),
        ]
        
        for title, graph in plotly_graphs:
            st.write(f"<center><h4 style='color:#00000090;font-size: 100%;font-weight: 300;'><b>{title}</b></h4></center>", unsafe_allow_html=True)
            st.plotly_chart(graph, use_container_width=True)
        
        with st.expander('Posts Analysis Report', expanded=True):
            cols = st.columns(3 )
            with cols[0]:
                st.success("⠀❤️12⠀")
            with cols[1]:   
                st.success("⠀♻️312")
            with cols[2]:
                st.success("⠀🖇️42⠀")
                
            st.write('''
                - Followers Count: 5348
                - Following Count: 1229
                - Subject: **Lorem ipsum dolor sit amet, consectetur adipiscing elit.**
                - Keywords and Phrases: `lorem ipsum`, `dolor sit amet`, `consectetur adipiscing elit`.
                - Overall Sentiment: :red[**Negative**]
                - Sentiment Breakdown:
                    - Positive: :green[**0.2**]
                    - Neutral: :orange[**0.1**]
                    - Negative: :red[**0.7**]
            ''')

        with st.expander('Current Stats', expanded=True):
            st.write('''
                - Most Influential politician: **N.B**
                - Trending Hashtags: `#loremipsum`, `#dolorsitamet`
            ''')
        
    #     matplotlib_graphs = [
    #         fig2,
    #         fig4
    #     ]
        
    #     for title, graph in matplotlib_graphs:
    #         # st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
    #         st.pyplot(graph, use_container_width=True)
                 
    # st.plotly_chart(most_common_words(df)[1], use_container_width=True) 
        
    # plotly_graphs = [
    #     most_common_ngrams(df),
    #     most_common_unigrams(df),
    #     most_common_bigrams(df),
    #     most_common_trigrams(df),
    # ]
    
    # left, right = st.columns(2)
    
    # with left:
    #     for title, graph in plotly_graphs[:2]:
    #         st.plotly_chart(graph, use_container_width=True)
    
    # with right:
    #     for title, graph in plotly_graphs[2:]:
    #         st.plotly_chart(graph, use_container_width=True)
    

if __name__=="__main__":
    st.set_page_config(layout="wide")
    visualization_page()