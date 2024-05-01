import numpy as np
import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px

def visualization_page():
    st.write("""
        <div style='text-align:center;'>
            <h1 style='text-align:center; font-size: 300%;'>Visualizations</h1>
            <p style=' color: #9c9d9f'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi, asperiores./p>
            <hr>
        </div>
            """
    , unsafe_allow_html=True)
    
    left, right = st.columns(2)
    
    with left:
        st.write("<center><h3>Distplot</h3></center>", unsafe_allow_html=True)
        
        x1 = np.random.randn(200) - 2
        x2 = np.random.randn(200)
        x3 = np.random.randn(200) + 2

        hist_data = [x1, x2, x3]
        group_labels = ['Group 1', 'Group 2', 'Group 3']

        fig = ff.create_distplot(
                hist_data, group_labels, bin_size=[.1, .25, .5])

        st.plotly_chart(fig, use_container_width=True)
    
    with right:
        st.write("<center><h3>Scatter Plot</h3></center>", unsafe_allow_html=True)
        
        df = px.data.gapminder()
        fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
                    size="pop", color="continent",
                        hover_name="country", log_x=True, size_max=60)
        
        st.plotly_chart(fig, use_container_width=True)