import re
import pandas as pd
import streamlit as st
from pysentimiento import create_analyzer
from sklearn.feature_extraction.text import CountVectorizer

def load_css():
    st.markdown('<style>' + open('./assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)
    
def load_header(title):
    cols = st.columns([4,1,0.7,1.5]) 
    with cols[0]:
        st.write("""<h2 class='custom' style='color:#00000099'>{}</h2>""".format(title), unsafe_allow_html=True)
    with cols[2]:
        st.image("assets/img/PCE.png", use_column_width=True)
    with cols[3]:
        st.image("assets/img/omdena_logo.png", use_column_width=True)
    # st.write("---")    
    
def tokenize(text):
    """ basic tokenize method with word character, non word character and digits """
    text = re.sub(r" +", " ", str(text))
    text = re.split(r"(\d+|[a-zA-ZğüşıöçĞÜŞİÖÇ]+|\W)", text)
    text = list(filter(lambda x: x != '' and x != ' ', text))
    sent_tokenized = ' '.join(text)
    return sent_tokenized

def get_top_ngram(corpus, n=None):
    vec = CountVectorizer(ngram_range=(n, n),
                          max_df=0.9,
                          ).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis=0)
    words_freq = [(word, sum_words[0, idx])
                  for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:15]
    
def is_valid_twitter_url(url):
    pattern = r"^https://(www\.)?(twitter|x)\.com/.+/status/\d+$"
    return re.match(pattern, url) is not None

def combine_author_and_comments_df(df_author, df_comments):
    if 'author__name' in df_comments:
        df_comments, df_author = df_author, df_comments     

    master_df = pd.concat([df_comments, df_author.drop(['author__name', 'author__id', 'author__description'], axis=1)], ignore_index=True)
    master_df = master_df.astype({'id': str, 'inReplyToId': str})
    master_df.sort_values(by='createdAt', inplace=True)
    
    return master_df

def tokenize(text):
    """ basic tokenize method with word character, non word character and digits """
    text = re.sub(r" +", " ", str(text))
    text = re.split(r"(\d+|[a-zA-ZğüşıöçĞÜŞİÖÇ]+|\W)", text)
    text = list(filter(lambda x: x != '' and x != ' ', text))
    sent_tokenized = ' '.join(text)
    return sent_tokenized

def add_sentiment_columns(master_df):
    data = {
        "viewCount": master_df.viewCount.iloc[0],
        "likeCount": master_df.likeCount.iloc[0],
        "retweetCount": master_df.retweetCount.iloc[0],
        "replyCount": master_df.replyCount.iloc[0],
        "author__followers": master_df.author__followers.iloc[0],
        "is_author_verified": master_df.author__verified.iloc[0],
        "text": master_df.text.iloc[0],
        "url": master_df.url.iloc[0],
    }

    analyzer = create_analyzer(task="sentiment", lang="es")
    master_df['sentiment'] = master_df['text'].apply(lambda x: analyzer.predict(x))
    master_df['sentiment_label'] = master_df['sentiment'].apply(lambda x: x.output)
    master_df['sentiment_numeric'] = master_df['sentiment'].apply(lambda x: max(x.probas))

    # master_df["tokenized_review"] = master_df.text.apply(lambda x: tokenize(x))
    master_df['createdAt'] = pd.to_datetime(master_df['createdAt'])
    master_df['date'] = master_df['createdAt'].dt.strftime('%Y-%m-%d')
    
    grouped = master_df.groupby(['date', 'sentiment_label']).size().unstack(fill_value=0)
    
    pos_sum = grouped.get('POS', 0).sum()
    neu_sum = grouped.get('NEU', 0).sum()
    neg_sum = grouped.get('NEG', 0).sum()

    sums = {"Positive": pos_sum, "Neutral": neu_sum, "Negative": neg_sum}
    overall_sentiment = max(sums, key=sums.get)

    data.update({
        "overall_sentiment": overall_sentiment,
        "positive": pos_sum,
        "neutral": neu_sum,
        "negative": neg_sum
    })

    return data

def init_session_state():
    if 'master_df' not in st.session_state:
        st.session_state['master_df'] = None
        
    if 'sentiment_over_date' not in st.session_state:
        st.session_state['sentiment_over_date'] = None
        
    if 'display_target_count' not in st.session_state:
        st.session_state['display_target_count'] = None
        
    if 'most_common_trigrams' not in st.session_state:
        st.session_state['most_common_trigrams'] = None
        
    if 'display_word_cloud' not in st.session_state:
        st.session_state['display_word_cloud'] = None
        
    if 'graphs_created' not in st.session_state:
        st.session_state['graphs_created'] = False

    if 'tweet_data' not in st.session_state:
        st.session_state['tweet_data'] = None
        
    # graphs
    if "sentiment_over_date" not in st.session_state:
        st.session_state["sentiment_over_date"] = None

    if "display_target_count" not in st.session_state:
        st.session_state["display_target_count"] = None

    if "most_common_trigrams" not in st.session_state:
        st.session_state["most_common_trigrams"] = None

    if "display_word_cloud" not in st.session_state:
        st.session_state["display_word_cloud"] = None