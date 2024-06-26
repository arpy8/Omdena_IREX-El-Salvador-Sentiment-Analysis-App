import streamlit as st
from streamlit_lottie import st_lottie
from utils.constants import PAGE_BANNER, PAGE_FAVICON

def home_page():
    with st.columns([1,2,1])[1]:
        st.image(PAGE_BANNER, use_column_width="auto")

    st.write("""
    <center>
        <h1 class="top">Herramienta de Analisis de Sentimientos de Omdena para Actores Políticos en El Salvador</h1>
        <p class="caption">
            Este proyecto tiene como objetivo desarrollar una herramienta de analisis de sentimientos impulsada por IA que categorice las opiniones públicas sobre los actores políticos en El Salvador en sentimientos positivos, negativos y neutrales. Al automatizar el proceso de analisis de sentimientos, pretendemos ofrecer información mas rapida y precisa para los analistas políticos y los responsables de la formulación de políticas. 
            <hr>
        </p>
    </center>
    """, unsafe_allow_html=True)
    
    cols1 = st.columns([0.2, 1, 0.05, 1, 0.2])
    padding_row = "<br>"
    
    with cols1[1]: 
        st.write("""
            <h3>Impacto en el Analisis Político y la Toma de Decisiones</h3>
            <p>El ritmo lento y las posibles inexactitudes del analisis de sentimientos manual tienen implicaciones significativas para el analisis político y la toma de decisiones en El Salvador. La demora en obtener información impide a los analistas y responsables de políticas responder proactivamente al sentimiento público, lo que puede resultar en oportunidades perdidas para interactuar o intervenir. Ademas, las inexactitudes en el analisis manual pueden llevar a estrategias mal informadas, que no solo podrían fallar en alcanzar sus objetivos, sino también exacerbar el descontento o la desconfianza pública, afectando la estabilidad política y socavando el proceso democratico.</p>
        """, unsafe_allow_html=True)
        st.write(padding_row, unsafe_allow_html=True)
    
        st_lottie("https://lottie.host/4bbcd636-eece-482f-8613-0e3ed93dafec/4ezAdnro3W.json", height=325)
        st.write(padding_row, unsafe_allow_html=True)

        st.write("""
            <h3>Empoderando a Analistas y Formuladores de politícas</h3>
            <p>El objetivo de esta iniciativa es proporcionar a los analistas políticos y responsables de políticas en El Salvador información precisa y en tiempo real sobre el sentimiento público, mediante una interfaz web para el analisis y visualización instantanea, mejorando así la capacidad de respuesta y la efectividad de las estrategias y políticas políticas.</p>
        """, unsafe_allow_html=True)
    
    with cols1[3]:  
        st_lottie("https://lottie.host/a786afd8-9903-4bed-8952-12b21b8016bd/PBO8x4JBEQ.json", height=325)
        st.write(padding_row, unsafe_allow_html=True)
        
        st.write(f"""
            <br>
            <h3>La necesidad de una solucion automatizada</h3>
            <p>El desarrollo de una herramienta de analisis de sentimientos impulsada por IA es esencial para superar los desafíos del analisis manual, proporcionando un proceso mas preciso y rapido al aplicar técnicas avanzadas de Procesamiento del Lenguaje Natural (NLP) a diversas fuentes de datos.</p>
            {'<br>'*5}
        """, unsafe_allow_html=True)
        st.write(padding_row, unsafe_allow_html=True)

        st_lottie("https://lottie.host/9c945dc7-e5d7-4148-b7f6-dfd748e1eb38/q0oJidkFyf.json", height=325)
    
   
if __name__=="__main__":
    st.set_page_config(page_title='Sentiment Analysis Tool', page_icon=PAGE_FAVICON, layout='wide')
    st.markdown('<style>' + open('./assets/css/styles.css').read() + '</style>', unsafe_allow_html=True)
    home_page()