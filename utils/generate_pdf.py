from io import BytesIO
import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

def generate_pdf(fig1=None, fig2=None, fig3=None, fig4=None, filename="output.pdf"):
    try:
        buffer = BytesIO()

        c = canvas.Canvas(buffer, pagesize=letter)
        c.setFont("Helvetica", 20)
        c.drawString(100, 750, "Sentiment Analysis Report")

        #### page 1
        buffer1 = BytesIO()
        fig1[1].write_image(buffer1, format='png')
        buffer1.seek(0)
        c.setFont("Helvetica", 12)
        c.drawString(100, 680, fig1[0])
        image1 = ImageReader(buffer1)
        c.drawImage(image1, 100, 480, width=400, height=150)

        buffer2 = BytesIO()
        fig2[1].write_image(buffer2, format='png')
        buffer2.seek(0)
        c.drawString(100, 370, fig2[0])
        image2 = ImageReader(buffer2)
        c.drawImage(image2, 100, 165, width=400, height=150)

        c.showPage()

        #### page 2
        buffer3 = BytesIO()
        fig3[1].write_image(buffer3, format='png')
        buffer3.seek(0)
        c.setFont("Helvetica", 12)
        c.drawString(100, 680, fig3[0])
        image3 = ImageReader(buffer3)
        c.drawImage(image3, 100, 480, width=400, height=150)

        buffer4 = BytesIO()
        fig4[1].write_image(buffer4, format='png')
        buffer4.seek(0)
        c.drawString(100, 350, fig4[0])
        image4 = ImageReader(buffer4)
        c.drawImage(image4, 100, 60, width=400, height=250)

        c.showPage()
        c.save()
        
        buffer.seek(0)
    
        with open(filename, "wb") as f:
            f.write(buffer.getbuffer())
        
        return "Successfully generated PDF"
    
    except Exception as e:
        return f"Error: {e}"
    
def construct_pdf():
    fig1 = st.session_state["sentiment_over_date"]
    fig2 = st.session_state["display_target_count"]
    fig3 = st.session_state["most_common_trigrams"]
    fig4 = st.session_state["display_word_cloud"]
    
    return generate_pdf(fig1, fig2, fig3, fig4)

if __name__=="__main__":
    import pandas as pd
    from utils.graph_functions import sentiment_over_date, \
                                        display_target_count, \
                                            most_common_trigrams, \
                                                display_word_cloud, \
                                                    display_word_cloud
    
    master_df = pd.read_csv('assets/dataset/temp_output_combined.csv')
    df = pd.read_csv('assets/dataset/master.csv')
    
    fig1 = "Sentiment Over Date", sentiment_over_date(master_df)
    fig2 = "Display Target Count", display_target_count(master_df)
    fig3 = "Most Common Trigrams", most_common_trigrams(master_df, pdf=True)
    fig4 = "Display Word Cloud", display_word_cloud(master_df)
    
    print(generate_pdf(fig1, fig2, fig3, fig4))