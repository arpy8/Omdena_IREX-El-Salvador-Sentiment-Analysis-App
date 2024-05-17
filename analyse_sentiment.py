import streamlit as st
from pysentimiento import create_analyzer
from constants import ANALYSIS_REPORT_TEMPLATE


def analyze_text(text: str):
    analyzer = create_analyzer(task="sentiment", lang="es")
    prediction = analyzer.predict(text)
    
    return prediction.output, prediction.probas[prediction.output]

def analyse_sentiment_page():
    st.write("""
        <div style='text-align:center;'>
            <h1 style='text-align:center; font-size: 300%;'>Analyse Sentiment</h1>
            <p style=' color: #ffffff95'>Paste the text to get the analysis report.</p>
            <hr>
            <br>
        </div>
    """
    , unsafe_allow_html=True)
    
    user_text_input = st.text_area('Paste your text here', key='text', height=200)
    
    with st.columns(4)[-1]:
        submit_button = st.button('Submit', key='submit_button', use_container_width=True)

    if user_text_input and submit_button:
        with st.spinner('Analyzing the text...'):
            sentiment_category_raw, sentiment_score = analyze_text(user_text_input)
            sentiments = {
                "POS": ["Positive", st.success],
                "NEG": ["Negative", st.error],
                "NEU": ["Neutral", st.info]
            }
            sentiment_score = round(sentiment_score, 5)
            sentiment_category = sentiments[sentiment_category_raw][0]

        sentiments[sentiment_category_raw][1](ANALYSIS_REPORT_TEMPLATE.format(sentiment_category=sentiment_category, sentiment_score=sentiment_score))

    elif len(user_text_input)==0 and submit_button:
        st.toast("Text area cannot be empty.", icon="⚠️")