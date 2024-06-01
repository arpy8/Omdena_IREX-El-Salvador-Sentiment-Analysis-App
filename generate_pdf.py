import plotly.express as px
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO

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
    
        # with open(filename, "wb") as f:
        #     f.write(buffer.getbuffer())
        
        return buffer
    
    except Exception as e:
        return f"Error: {e}"
    

if __name__=="__main__":
    df = px.data.iris()
    fig1 = "test message", px.scatter(df, x='sepal_length', y='petal_length', color='species')
    fig2 = "test message", px.scatter(df, x='sepal_length', y='petal_length', color='species')
    fig3 = "test message", px.scatter(df, x='sepal_length', y='petal_length', color='species')
    fig4 = "test message", px.scatter(df, x='sepal_length', y='petal_length', color='species')
    
    print(generate_pdf(fig1, fig2, fig3, fig4))