import streamlit as st
from graph_functions import *


def visualization_page():
    df = pd.read_csv('https://raw.githubusercontent.com/arpy8/Omdena_IREX-El-Salvador-Sentiment-Analysis-App/main/assets/dataset/final.csv')
    
    st.write("""
            <div style='text-align:center;'>    
                <h1 style='text-align:center; font-size: 300%;'>Visualizations</h1>
                <p style='color: #ffffff95'>Explore insightful visual representations from our dataset.</p>
                <hr>
            </div>
        """, unsafe_allow_html=True)

    fig1, fig2, fig3, fig4 = characters_count_in_the_data(df)
    left, right = st.columns(2)

    with left:   
        plotly_graphs = [
            display_word_cloud(df, 'Text_Clean'),
            # token_counts_with_simple_tokenizer(df),
        ]
        
        for title, graph in plotly_graphs:
            # st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
            st.plotly_chart(graph, use_container_width=True) 

        matplotlib_graphs = [
            fig1,
            fig3
        ]
        
        for title, graph in matplotlib_graphs:
            # st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
            st.pyplot(graph, use_container_width=True) 

    with right:
        plotly_graphs = [
            display_target_count(df),
            # token_counts_With_bert_tokenizer(df),
        ]
        
        for title, graph in plotly_graphs:
            # st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
            st.plotly_chart(graph, use_container_width=True)
            
        matplotlib_graphs = [
            fig2,
            fig4
        ]
        
        for title, graph in matplotlib_graphs:
            # st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
            st.pyplot(graph, use_container_width=True)
                 
    st.plotly_chart(most_common_words(df)[1], use_container_width=True) 
        
    plotly_graphs = [
        most_common_ngrams(df),
        most_common_unigrams(df),
        most_common_bigrams(df),
        most_common_trigrams(df),
    ]
    
    left, right = st.columns(2)
    
    with left:
        for title, graph in plotly_graphs[:2]:
            st.plotly_chart(graph, use_container_width=True)
    
    with right:
        for title, graph in plotly_graphs[2:]:
            st.plotly_chart(graph, use_container_width=True)
    

if __name__=="__main__":
    st.set_page_config(layout="wide")
    visualization_page()