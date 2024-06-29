import pandas as pd
import streamlit as st
from st_on_hover_tabs import on_hover_tabs

from st_pages.home import home_page
from st_pages.analyse import analyse_page
from st_pages.dashboard import dashboard
from st_pages.about import about_us_page
from utils.constants import PAGE_FAVICON, CONTRIBUTORS
from utils.utils import load_css, init_session_state, load_header

st.set_page_config(page_title='Sentiment Analysis Tool', page_icon=PAGE_FAVICON, layout='wide')

load_css()
init_session_state()

with st.sidebar:
    st.write('<br>'*4, unsafe_allow_html=True)
    selected_task = on_hover_tabs(
        tabName=['Home Page', 'Analyse Sentiment', 'Dashboard', 'About Us'],
        iconName=['home', 'engineering', 'insert_chart', 'contact_support'],
        styles = {
            'navtab': {'background-color':'#fff'},
            'tabOptionsStyle': {':hover :hover': {'color': '#170034', 'cursor': 'pointer'}},
        },
        default_choice=2)

if selected_task == 'Home Page':
    home_page()

elif selected_task == 'Analyse Sentiment':
    analyse_page()

elif selected_task == 'Dashboard':
    if 'master_df' in st.session_state and st.session_state['master_df'] is None:
        # load_header("Sentiment Analysis Dashboard")
        # st.info("Please analyze a tweet first.")
        st.session_state['master_df'] = pd.read_csv('assets/dataset/temp_output_combined.csv')
    # else:
    with st.spinner("Loading Dashboard..."):
        dashboard() 

elif selected_task == 'About Us':
    about_us_page(CONTRIBUTORS)