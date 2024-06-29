import random
import warnings
import pandas as pd
from PIL import Image
import streamlit as st
from wordcloud import WordCloud
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from utils.utils import get_top_ngram

warnings.filterwarnings('ignore')
nltk.download('stopwords')
nltk.download('punkt')

def custom_color_func(word, font_size, position, orientation, font_path, random_state):
    color_palette = ['#ff2b2b', '#83c9ff', '#0068c9']
    return random.choice(color_palette)

def display_word_cloud(dataframe):
    all_text = ' '.join(dataframe['text'])
    wordcloud = WordCloud(background_color="#fff", colormap="autumn", color_func=custom_color_func).generate(all_text)
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
        height=170,
        width=500,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False)
    )
    
    return fig

def most_common_trigrams(df, pdf=False):
    stop_words = set(stopwords.words('english'))

    colors = ['#ff2b2b', '#83c9ff', '#0068c9']
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
    colors = ['#83c9ff', '#ff2b2b', '#0068c9']
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

    colors = ['#ff2b2b', '#83c9ff', '#0068c9'][::-1]
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

##############################################################################################################################

def crear_grafico_dispersion(df):
    fig = px.scatter(
        df,
        x='likeCount',
        y='sentiment_label',
        color='sentiment_label',
        labels={'likeCount': 'Número de Likes', 'sentiment_label': 'Etiqueta de Sentimiento'},
        title='Relación entre Número de Likes y Etiquetas de Sentimiento'
    )
    
    fig.update_layout(
        title_y=1,
        title_font=dict(color='#808495', size=15),
        autosize=True,
        height=250,
        margin=dict(l=0, r=0, t=20, b=0),
        # xaxis=dict(visible=False),
        # yaxis=dict(visible=False)
    )
    
    return fig

def bubble_fig(df):
    bubble_chart_data = df.groupby('account_creation_time').size().reset_index(name='user_count')
    bubble_fig = px.scatter(
        bubble_chart_data, x='account_creation_time', y='user_count', size='user_count',
        title='Tiempo de Creación de Cuenta<br>vs. Número de Usuarios',
        labels={'account_creation_time': 'Tiempo de Creación de Cuenta (meses)', 'user_count': 'Número de Usuarios'}
    )
    return bubble_fig

def hist_fig(df):
    hist_fig = px.histogram(
        df, x='account_creation_time',
        title='Distribución del Tiempo de Creación de Cuenta',
        labels={'account_creation_time': 'Tiempo de Creación de Cuenta (meses)', 'user_count': 'Número de Usuarios'},
        nbins=25
    )
    
    return hist_fig

def stacked_bar_fig(df):
    stacked_bar_fig = px.histogram(
        df, x='account_creation_time', color='sentiment_label',
        title='Distribución del Tiempo de <br>Creación de Cuenta por Sentimiento de Comentario',
        labels={'account_creation_time': 'Tiempo de Creación de Cuenta (meses)', 'count': 'Número de Usuarios', 'sentiment_beto': 'Sentimiento'},
        barmode='stack',
        nbins=25      
    )
    return stacked_bar_fig

def metrics_bar(tweet_data, df):
    st.write("""
    <style>
    div[data-testid="stMetric"]
    {
        background-color: #00000005;
        color: black;
        padding: 10px 0 0 10px;
        border-radius: 5px;
    }
    </style>
            
    """, unsafe_allow_html=True)

    avg_time = df['account_creation_time'].mean()
    min_time = df['account_creation_time'].min()
    max_time = df['account_creation_time'].max()

    left, right = st.columns([2,1])
    
    with left:
        with st.container(border=True):
            # st.write("###### Analysis of Time Metrics")
            col1, col2, col3 = st.columns(3)
            col1.metric("Tiempo Promedio", f"{round(avg_time/12)} años")
            col2.metric("### Tiempo Mínimo", f"{min_time} meses")
            col3.metric("Tiempo Máximo", f"{round(max_time/12)} años")
    
    with right:
        with st.container(border=True):
            # st.write("###### Sentiment Breakdown")
            pos, neu, neg = st.columns(3)
            # st.info(f"##### **Overall Sentiment**: :{TEXT_COLOR[tweet_data['overall_sentiment'].lower()]}[**{tweet_data['overall_sentiment']}**]")
            pos.metric(label=":green[Positive]", value=tweet_data["positive"])
            neu.metric(label=":gray[Neutral]", value=tweet_data["neutral"])
            neg.metric(label=":red[Negative]", value=tweet_data["negative"])


if __name__ == "__main__":
    pass