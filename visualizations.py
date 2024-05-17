import streamlit as st
from graph_functions import *


def visualization_page():
    df = pd.read_csv('./assets/dataset/final.csv')
    
    st.write("""
            <div style='text-align:center;'>    
                <h1 style='text-align:center; font-size: 300%;'>Visualizations</h1>
                <p style='color: #ffffff95'>Explore insightful visual representations from our dataset.</p>
                <hr>
            </div>
        """, unsafe_allow_html=True)

    left, right = st.columns(2)
    fig1, fig2, fig3, fig4 = characters_count_in_the_data(df)
    
    with left:
        graphs = [
            display_word_cloud(df, 'Text_Clean'),
            token_counts_with_simple_tokenizer(df),
            fig1,
            fig2,
            # plot_word_number_histogram(df[df['label'] == 0]['Text_Clean'],
            #                         df[df['label'] == 1]['Text_Clean'],
            #                         df[df['label'] == 2]['Text_Clean'],
            #                     ),
            # review_lengths(df[df['label'] == 0], 'char_count',
            #         'Characters Count "positive Review'),
            # review_lengths(df[df['label'] == 1], 'char_count',
            #         'Characters Count "neutral Review'),
            # review_lengths(df[df['label'] == 2], 'char_count',
            #         'Characters Count "negative Review'),
        ]
            
        for title, graph in graphs:
            st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
            st.plotly_chart(graph, use_container_width=True) 


    with right:
        graphs = [
            display_target_count(df),
            token_counts_With_bert_tokenizer(df),
            fig3,
            fig4
        ]
        
        for title, graph in graphs:
            st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
            st.plotly_chart(graph, use_container_width=True)
            
    graphs = [
        most_common_words(df),
        most_common_bigrams(df),
        most_common_trigrams(df),
        most_common_ngrams(df),
    ]
    
    for title, graph in graphs:
        st.write(f"<center><h4>{title}</h4></center>", unsafe_allow_html=True)
        st.plotly_chart(graph, use_container_width=True) 
        

if __name__=="__main__":
    st.set_page_config(layout="wide")
    visualization_page()