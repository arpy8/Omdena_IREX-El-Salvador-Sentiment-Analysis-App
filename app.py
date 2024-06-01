import streamlit as st
from st_on_hover_tabs import on_hover_tabs

from dashboard import dashboard
from analyse import analyse_sentiment_page
from about import about_us_page
from constants import PAGE_BANNER, PAGE_FAVICON
from home import home_page


st.set_page_config(page_title='Sentiment Analysis Tool', page_icon=PAGE_FAVICON, layout='wide')
st.markdown('<style>' + open('./assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)

if 'disable_button' not in st.session_state:
    st.session_state['disable_button'] = False

with st.sidebar:    
    st.write('<br><br><br><br>', unsafe_allow_html=True)
    selected_task = on_hover_tabs(
        tabName=['Home Page', 'Analyse Sentiment', 'Dashboard', 'About Us'],
        iconName=['home', 'engineering', 'insert_chart', 'contact_support'],
        styles = {
            'navtab': {'background-color':'#fff',
                        'color': '#00000080',
                        'padding': '40px 0px 10px 0px',
                        'border-radius': '0px',
                        'font-size': '18px',    
                        'transition': '.5s',
                        'white-space': 'nowrap',
                        'text-transform': 'uppercase',
            },
            'tabOptionsStyle': {':hover :hover': {'color': '#170034',
                                            'cursor': 'pointer'},
                            },
            'iconStyle':{'position':'fixed',    
                        'left':'11.5px'},
            'tabStyle' : {'background-color':'rgba(0, 0, 0, 0)',
                        'list-style-type': 'none',
                        'margin-bottom': '30px',
                        },
        },
        key="1",
        default_choice=0)

if selected_task == 'Home Page':
    # with st.columns([3,4,3])[1]:
    #     st.image(PAGE_BANNER, use_column_width="auto")
    
    # st.write(open('assets/html_components/home.html', 'r').read(), unsafe_allow_html=True)
    home_page()

elif selected_task == 'Analyse Sentiment':
    analyse_sentiment_page()

elif selected_task == 'Dashboard':
    with st.spinner("Loading Dashboard..."):
        dashboard()
    
elif selected_task == 'About Us':
    about_us_page()