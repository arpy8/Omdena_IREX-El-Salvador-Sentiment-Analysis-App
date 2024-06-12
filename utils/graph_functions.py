import warnings
import pandas as pd
from PIL import Image
from wordcloud import WordCloud
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from utils.utils import get_top_ngram

warnings.filterwarnings('ignore')
nltk.download('stopwords')
nltk.download('punkt')

def display_word_cloud(dataframe):
    all_text = ' '.join(dataframe['text'])
    wordcloud = WordCloud(background_color="#fff", colormap="autumn").generate(all_text)
    wordcloud_image = wordcloud.to_array()

    fig = go.Figure()
    fig.add_layout_image(
        dict(
            source=Image.fromarray(wordcloud_image),
            x=0, y=1,
            sizex=1,
            sizey=1.3,
            opacity=1,
        )
    )
    fig.update_layout(
        autosize=False,
        height=250,
        width=500,
        margin=dict(l=0, r=0, t=30, b=0),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False)
    )
    
    return fig

def most_common_trigrams(df, pdf=False):
    stop_words = set(stopwords.words('english'))

    colors = ['#FFBE98', '#F7DED0', '#E2BFB3']
    fig = make_subplots(rows=1, cols=3)

    sentiment_list = ["positive", "neutral", "negative"]
    sentiment_list2 = ["POS", "NEU", "NEG"]

    for i in range(3):
        texts = df[df["sentiment_label"] == sentiment_list2[i]]['text']
        
        tokenized_texts = texts.apply(word_tokenize)
        tokenized_texts = tokenized_texts.apply(lambda x: [word.lower() for word in x if word.lower() not in stop_words])
        
        texts_cleaned = tokenized_texts.apply(lambda x: ' '.join(x))
        
        top_n_bigrams = get_top_ngram(texts_cleaned, 2)[:15]
        x, y = map(list, zip(*top_n_bigrams))

        fig.add_trace(go.Bar(
            x=y,
            orientation='h',
            type="bar",
            name=sentiment_list[i].title(),
            marker=dict(color=colors[i]),
            text=x,
            textposition='inside',
            hovertemplate="%{text}: %{y}"
        ), 1, i+1)

    fig.update_layout(
        autosize=False,
        margin=dict(t=0, b=0, l=0, r=0),
        height=250,
    )
    
    return fig

def display_target_count(df):
    colors = ['#F7DED0', '#FFBE98', '#E2BFB3']
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "bar"}]])
    fig.add_trace(go.Pie(labels=df.sentiment_label.value_counts().index,
                                values=df.sentiment_label.value_counts().values), 1, 1)
    fig.update_traces(hoverinfo='label+percent',
                        textfont_size=18,
                        marker=dict(
                            colors=colors,
                            line=dict(
                                color='#fff', 
                                width=1
                            )
                        )
                    )
    fig.add_trace(go.Bar(
                        x=df.sentiment_label.value_counts().index, 
                        y=df.sentiment_label.value_counts().values, 
                        marker_color = colors
                    ), 1,2)
    fig.update_layout(
        title_text="Sentiment Distribution",
        title_y=1,
        title_font=dict(color='#808495', size=15),
        autosize=True,
        height=250,
        margin=dict(l=0, r=0, t=25, b=10),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False)
    )

    return fig

def sentiment_over_date(df):
    df['createdAt'] = pd.to_datetime(df['createdAt'])
    df['date'] = df['createdAt'].dt.strftime('%Y-%m-%d')

    grouped = df.groupby(['date', 'sentiment_label']).size().unstack(fill_value=0)

    fig = go.Figure()

    colors = ['#FFBE98', '#F7DED0', '#E2BFB3'][::-1]
    for idx, sentiment_label in enumerate(grouped.columns):
        fig.add_trace(go.Scatter(
            x=grouped.index, y=grouped[sentiment_label],
            mode='lines',
            name=sentiment_label.capitalize(),
            stackgroup='one',
            line=dict(width=2, color=colors[idx]),
            fillcolor=colors[idx],
            hoverinfo='y+name'
        ))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_layout(
        title={
            'text': 'Sentiment Over Time',
            'x': 0.2,
            'y': 1,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 15, 'color': '#808495', 'family': 'Arial'}
        },
        xaxis_title='Date',
        yaxis_title='Sentiment Count',
        hovermode='x',
        showlegend=True,
        autosize=False,
        height=250,
        width=500,
        margin=dict(l=0, r=0, t=40, b=0),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )

    return fig