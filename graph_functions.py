import pandas as pd
from wordcloud import WordCloud
import seaborn as sns
from collections import Counter
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
import warnings
import nltk
from nltk.corpus import stopwords

warnings.filterwarnings("ignore")

# @st.cache_data()
def download_stopwords():
    nltk.download('stopwords')
    return True

download_stopwords()

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go

from utils import _get_top_ngram

warnings.filterwarnings('ignore')
nltk.download('stopwords')

stopWords_nltk = set(stopwords.words('english'))
colors = ['gold', 'mediumturquoise', 'lightgreen'] # darkorange



df = pd.read_csv('https://raw.githubusercontent.com/arpy8/Omdena_IREX-El-Salvador-Sentiment-Analysis-App/main/assets/dataset/final.csv')

def histogram_of_review_rating(df):
    fig = px.histogram(df,
             x = 'AP',
             title = 'Histogram of Review Rating',
             template = 'ggplot2',
             color = 'AP',
             color_discrete_sequence= px.colors.sequential.Blues_r,
             opacity = 0.8,
             height = 525,
             width = 835,
            )

    fig.update_yaxes(title='Count')
    return "Histogram of Review Rating", fig

# ## Word Cloud
def display_word_cloud(df, column_name, background_color='black', max_words=200, max_font_size=40, scale=1, random_state=1):
    text = " ".join(df[column_name].values)

    wordcloud = WordCloud(
        background_color=background_color,
        max_words=max_words,
        max_font_size=max_font_size,
        scale=scale,
        random_state=random_state
    ).generate(text)

    word_positions = wordcloud.layout_
    x = []
    y = []
    words = []
    font_sizes = []

    for (word, freq), font_size, position, orientation, color in word_positions:
        x.append(position[0])
        y.append(position[1])
        words.append(word)
        font_sizes.append(font_size)

    trace = Scatter(
        x=x,
        y=y,
        text=words,
        mode='text',
        textfont=dict(size=font_sizes, color='white'),
    )

    layout = Layout(
        title='WordCloud',
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        plot_bgcolor=background_color
    )

    fig = go.Figure(data=[trace], layout=layout)
    fig.update_layout(yaxis=dict(autorange='reversed'))
    
    return "WordCloud", fig

# ## Target Count
def display_target_count(df):
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "bar"}]])
    colors = ['gold', 'mediumturquoise', 'lightgreen']
    fig.add_trace(go.Pie(labels=df.AP.value_counts().index,
                                values=df.label.value_counts().values), 1, 1)
    fig.update_traces(hoverinfo='label+percent', textfont_size=20,
                    marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.add_trace(go.Bar(x=df.AP.value_counts().index, y=df.label.value_counts().values, marker_color = colors), 1,2)
    fig.update_layout(title_text="")

    return "Class Distribution", fig

# # Token Counts with simple tokenizer
def token_counts_with_simple_tokenizer(df):
    # df["tokenized_review"] = df.Text.apply(lambda x: tokenize(x))
    # df["sent_token_length"] = df["tokenized_review"].apply(lambda x: len(x.split()))

    fig = px.histogram(df, x="sent_token_length", nbins=20, color_discrete_sequence=px.colors.cmocean.algae, barmode='group', histnorm="percent")
    return "Token counts with Simple Tokenizer", fig

# # Token Counts with BERT tokenizer
def token_counts_With_bert_tokenizer(df):
    # tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',
    #                                       do_lower_case=True)
    # df["sent_bert_token_length"] = df["Text"].apply(lambda x: len(tokenizer(x, add_special_tokens=False)["input_ids"]))
    fig = px.histogram(df, x="sent_bert_token_length", nbins=20, color_discrete_sequence=px.colors.cmocean.algae, barmode='group', histnorm="percent")
    return "Token counts with Bert Tokenizer", fig

# # Characters Count in the Data¶
def characters_count_in_the_data(df):
    df['char_count'] = df['Text_Clean'].apply(lambda x: len(str(x)))

    def plot_dist(df, feature, title):
        fig = plt.figure(constrained_layout=True, figsize=(18, 8))
        grid = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)
        ax1 = fig.add_subplot(grid[0, :2])
        ax1.set_title(title)
        sns.histplot(df.loc[:, feature], kde=True, ax=ax1)
        ax1.set(ylabel='Frequency')
        ax1.xaxis.set_major_locator(MaxNLocator(nbins=20))

        return title, fig

    title1, fig1 = plot_dist(df, 'char_count', 'Characters Count in Data')
    title2, fig2 = plot_dist(df[df['label'] == 0], 'char_count', 'Characters Count "positive Review')
    title3, fig3 = plot_dist(df[df['label'] == 1], 'char_count', 'Characters Count "neutral Review')
    title4, fig4 = plot_dist(df[df['label'] == 2], 'char_count', 'Characters Count "negative Review')

    def mpl_to_plotly_fig(title, fig):
        plotly_fig = go.Figure()
        plotly_fig.add_trace(go.Histogram(x=df['char_count']))
        plotly_fig.update_layout(bargap=0)
        return title, plotly_fig

    return (
            mpl_to_plotly_fig(title1, fig1),
            mpl_to_plotly_fig(title2, fig2),
            mpl_to_plotly_fig(title3, fig3),
            mpl_to_plotly_fig(title4, fig4)
        )

    
    
# # Reviews Lengths
def plot_review_lengths(df):
    def review_lengths(df, feature, title):
        fig = plt.figure(constrained_layout=True, figsize=(24, 12))
        grid = gridspec.GridSpec(ncols=3, nrows=3, figure=fig)

        ax1 = fig.add_subplot(grid[0, :2])
        ax1.set_title('Histogram')
        sns.histplot(df.loc[:, feature],
                    kde=True,
                    ax=ax1,
                    color='#e74c3c')
        ax1.set(ylabel='Frequency')
        ax1.xaxis.set_major_locator(MaxNLocator(nbins=20))

        ax2 = fig.add_subplot(grid[1, :2])
        ax2.set_title('Empirical CDF')
        sns.histplot(df.loc[:, feature],
                    ax=ax2,
                    kde_kws={'cumulative': True},
                    color='#e74c3c')
        ax2.xaxis.set_major_locator(MaxNLocator(nbins=20))
        ax2.set(ylabel='Cumulative Probability')

        return title, fig
    
    return (
            review_lengths(df[df['label'] == 0], 'char_count',
                    'Characters Count "positive Review'),
            review_lengths(df[df['label'] == 1], 'char_count',
                    'Characters Count "neutral Review'),
            review_lengths(df[df['label'] == 2], 'char_count',
                    'Characters Count "negative Review'),
        )

# ## Word Counts
def plot_word_number_histogram(textno, textye, textz):
    fig, axes = plt.subplots(ncols=1, nrows=3, figsize=(18, 12), sharey=True)
    sns.displot(textno.str.split().map(lambda x: len(x)), ax=axes[0], color='#e74c3c')
    sns.displot(textye.str.split().map(lambda x: len(x)), ax=axes[1], color='#e74c3c')
    sns.displot(textz.str.split().map(lambda x: len(x)), ax=axes[2], color='#e74c3c')


    axes[0].set_xlabel('Word Count')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('positive')
    axes[1].set_xlabel('Word Count')
    axes[1].set_title('netrual')
    axes[2].set_xlabel('Word Count')
    axes[2].set_title('negative')

    fig.suptitle('Words Per Review', fontsize=24, va='baseline')
    fig.tight_layout()
    
    return "Words Per Review", fig

# # Most Common Words
def most_common_words(df):
    texts = df['tokenized_review']
    new = texts.str.split()
    new = new.values.tolist()
    corpus = [word for i in new for word in i]
    counter = Counter(corpus)
    most = counter.most_common()
    x, y = [], []

    for word, count in most[:30]:
        if word not in stopWords_nltk:
            x.append(word)
            y.append(count)

    fig = go.Figure(go.Bar(
                x=y,
                y=x,
                orientation='h',  marker=dict(
            color='rgba(50, 171, 96, 0.6)',
            line=dict(
                color='rgba(50, 171, 96, 1.0)',
                width=1),
        ),
        name='Most common Word',))

    fig.update_layout( title={
            'text': "",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}, font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        ))

    return "Most Common Words", fig

# # Most Common ngrams
def most_common_ngrams(df):
    fig = make_subplots(rows=1, cols=3)
    title_ = ["positive", "neutral", "negative"]

    for i in range(3):
        texts = df[df["label"] == i]['tokenized_review']

        new = texts.str.split()
        new = new.values.tolist()
        corpus = [word for i in new for word in i]
        counter = Counter(corpus)
        most = counter.most_common()
        x, y = [], []

        for word, count in most[:30]:
            if word not in stopWords_nltk:
                x.append(word)
                y.append(count)

        fig.add_trace(go.Bar(
                    x=y,
                    y=x,
                    orientation='h', type="bar",
            name=title_[i], marker=dict(color=colors[i])), 1, i+1)

    fig.update_layout(
        autosize=False,
        width=2000,
        height=600,title=dict(
            text='',
            x=0.5,
            y=0.95,
            font=dict(
            family="Courier New, monospace",
            size=24,
            color="RebeccaPurple"
            )
        ),)

    return "Most Common ngrams per Classes", fig

# ## Top Bigrams
def most_common_bigrams(df):
    fig = make_subplots(rows=1, cols=3)
    title_ = ["positive", "neutral", "negative"]

    for i in range(3):
        texts = df[df["label"] == i]['tokenized_review']

        new = texts.str.split()
        new = new.values.tolist()
        corpus = [word for i in new for word in i]
        top_n_bigrams = _get_top_ngram(texts, 2)[:15]
        x, y = map(list, zip(*top_n_bigrams))


        fig.add_trace(go.Bar(
                    x=y,
                    y=x,
                    orientation='h', type="bar",
            name=title_[i], marker=dict(color=colors[i])), 1, i+1)


    fig.update_layout(
        autosize=False,
        width=2000,
        height=600,title=dict(
            text='',
            x=0.5,
            y=0.95,
            font=dict(
            family="Courier New, monospace",
            size=24,
            color="RebeccaPurple"
            )
        ))

    return "Most Common Bigrams per Classes", fig  

# ## Trigram
def most_common_trigrams(df):
    fig = make_subplots(rows=1, cols=3)
    title_ = ["negative", "neutral", "positive"]

    for i in range(3):
        texts = df[df["label"] == i]['tokenized_review']

        new = texts.str.split()
        new = new.values.tolist()
        # corpus = [word for i in new for word in i]

        top_n_bigrams = _get_top_ngram(texts, 3)[:15]
        x, y = map(list, zip(*top_n_bigrams))

        fig.add_trace(go.Bar(
                    x=y,
                    y=x,
                    orientation='h', type="bar",
            name=title_[i], marker=dict(color=colors[i])), 1, i+1),

    fig.update_layout(
        autosize=False,
        width=2000,
        height=600,title=dict(
            text='',
            x=0.5,
            y=0.95,
            font=dict(
            family="Courier New, monospace",
            size=24,
            color="RebeccaPurple"
            )
        ))

    return "Most Common Trigrams per Classes", fig

if __name__=="__main__":
    display_word_cloud(df, 'Text_Clean')
    display_target_count(df).show()
    token_counts_with_simple_tokenizer(df).show()
    token_counts_With_bert_tokenizer(df).show()
    characters_count_in_the_data(df)

    # review_lengths(df[df['label'] == 0], 'char_count',
    #         'Characters Count Positive Review')
    # review_lengths(df[df['label'] == 1], 'char_count',
    #         'Characters Count Neutral Review')
    # review_lengths(df[df['label'] == 2], 'char_count',
    #         'Characters Count Negative Review')

    plot_word_number_histogram(df[df['label'] == 0]['Text_Clean'],
                            df[df['label'] == 1]['Text_Clean'],
                            df[df['label'] == 2]['Text_Clean'],
                            )

    most_common_words(df).show()
    most_common_ngrams(df).show()
    most_common_bigrams(df).show()
    most_common_trigrams(df).show()