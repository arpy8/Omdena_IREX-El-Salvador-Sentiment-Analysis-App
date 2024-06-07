import re
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
    
def tokenize(text):
    """ basic tokenize method with word character, non word character and digits """
    text = re.sub(r" +", " ", str(text))
    text = re.split(r"(\d+|[a-zA-ZğüşıöçĞÜŞİÖÇ]+|\W)", text)
    text = list(filter(lambda x: x != '' and x != ' ', text))
    sent_tokenized = ' '.join(text)
    return sent_tokenized

def _get_top_ngram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(n, n),
                          max_df=0.9,
                          ).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:15]

def load_header(title):
    cols = st.columns([4,1,1,2])
    with cols[0]:
        st.write("""<h2 class='custom' style='color:#00000099'>{}</h2>""".format(title), unsafe_allow_html=True)
    
    with cols[2]:
        st.image("assets/img/PCE.png", use_column_width=True)
    with cols[3]:
        st.image("assets/img/omdena_logo.png", use_column_width=True)
    
    # st.write("---")