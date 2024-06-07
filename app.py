import streamlit as st
from st_on_hover_tabs import on_hover_tabs

from home import home_page
from analyse import analyse
from dashboard import dashboard
from about import about_us_page
from constants import PAGE_FAVICON


st.set_page_config(page_title='Sentiment Analysis Tool', page_icon=PAGE_FAVICON, layout='wide')
st.markdown('<style>' + open('./assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)

with st.sidebar:    
    st.write('<br><br><br>', unsafe_allow_html=True)
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
        default_choice=0)

if selected_task == 'Home Page':
    home_page()

elif selected_task == 'Analyse Sentiment':
    analyse()

elif selected_task == 'Dashboard':
    with st.spinner("Loading Dashboard..."):
        dashboard()
    
elif selected_task == 'About Us':
    about_us_page()