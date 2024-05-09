import base64
import time
import constants
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from googletrans import Translator
from streamlit_lottie import *
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from textblob import TextBlob
import toml
import html 
import requests 
from streamlit.runtime.media_file_storage import MediaFileStorageError
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
# from config import BASE_PROMPT, HF_EMAIL, HF_PASS

flag = 0


# Login Credentials
HF_EMAIL = "gamersid123456@gmail.com"
HF_PASS = "a+Xw5H(Rnu9,~#k"
BASE_PROMPT = "I want you to act as a virtual assistant for farmers and come up with conventional treatments for plant diseases. You should be able to recommend conventional  methods to resolve the plant disease and other natural alternatives.\n\n"

indian_languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Bengali': 'bn',
    'Telugu': 'te',
    'Marathi': 'mr',
    'Tamil': 'ta',
    'Urdu': 'ur',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Odia': 'or',
    'Malayalam': 'ml',
    'Punjabi': 'pa',
    'Assamese': 'as',
    'Maithili': 'mai',
    'Santali': 'sat',
    'Kashmiri': 'ks',
    'Nepali': 'ne',
    'Sindhi': 'sd',
    'Konkani': 'kok',
    'Manipuri': 'mni',
    'Dogri': 'doi',
    'Bodo': 'brx',
    'Sanskrit': 'sa'
}

# Function to clear the page
def clear_page():
    st.empty()


def chat_bot():
    # Store LLM generated responses
    clear_page()
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How may I help you?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Function for generating LLM response
    def generate_response(prompt_input, email, passwd):

        # Hugging Face Login
        sign = Login(email, passwd)
        cookies = sign.login()
        # Create ChatBot                            
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        global flag
        if flag < 1:
            flag += 1
            prompt_input = BASE_PROMPT + prompt_input
        return str(chatbot.chat(prompt_input)).strip('`')

    # User-provided prompt
    if prompt := st.chat_input(disabled=not (HF_EMAIL and HF_PASS)):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt, HF_EMAIL, HF_PASS) 
                st.write(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)

# Function to display the home page content
def home_page():
    def get_image_download_link(img_path):
        with open(img_path, "rb") as img_file:
            img_bytes = img_file.read()
        img_base64 = base64.b64encode(img_bytes).decode()
        return f"data:image/png;base64,{img_base64}"

# Path to your local image file
    image_path = "/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/assets/floralogo.png"
    st.write(
    """
    <div style="display: flex; justify-content: center;">
        <img src="{}" alt="Local Image" width=500>
    </div>
    """.format(get_image_download_link(image_path)),
    unsafe_allow_html=True
)
    # Lottie animations
    lottie = """
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://lottie.host/5ca098aa-290c-4091-9548-f8f46c51b8ce/gzqvydc0py.json"  background="transparent"  speed="2"  style="width: 2000px; height: 2000px;"  loop  autoplay></lottie-player>
    """
    st.markdown("""
        <style>
            iframe {
                position: fixed;
                top: 2rem;
                bottom: 0;
                left: 0;
                right: 0;
                margin: auto;
                z-index=-1;
            }
            .nav-pills {
                position: relative;
                z-index: 10;
                background-color: #fff;
                padding: 10px;
                border-radius: 10px;
            }
        </style>
        """, unsafe_allow_html=True)
    # st.components.v1.html(lottie, width=2010, height=2010)

    lottie3 = """
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://lottie.host/b60fff1d-cbeb-4d41-aba1-b624200c0513/OoZwK6n4cr.json"  background="transparent"  speed="2.75"  style="width: 2000px; height: 2000px;"  loop  autoplay></lottie-player>
    """
    st.markdown("""
    <style>
        iframe {
            position: fixed;
            top: 2rem;
            bottom: ;
            left: 0;
            right: 0;
            margin: auto;
            z-index=-1;
        }
        .nav-pills {
            position: relative;
            z-index: 10;
        }
    </style>
    """, unsafe_allow_html=True)
    # st.components.v1.html(lottie3, width=2010, height=2010)

    lottie2 = """
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://lottie.host/20837e04-4218-4d4c-8889-08e2a1ddbf96/BjmCosJ0eF.json"  background="transparent"  speed="1"  style="width: 1000px; height: 1000px;"  loop  autoplay></lottie-player>
    """
    st.markdown("""
    <style>
        iframe {
            position: fixed;
            top: 2rem;
            bottom: ;
            left: 0;
            right: 0;
            margin: auto;
            z-index=-1;
        }
        .nav-pills {
            position: relative;
            z-index: 10;
        }
    </style>
    """, unsafe_allow_html=True)
    # st.components.v1.html(lottie2, width=1010, height=1300)

    # Home page content
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write('<div style="text-align: center;">This tool is designed to assist you in identifying the health status of your plants with the help of a Convolutional Neural Network (CNN). Whether you are a home gardener or a farmer, early detection of plant diseases can make a significant difference in preserving the well-being of your plants and optimizing crop yields.</div>', unsafe_allow_html=True)

    # with st.sidebar:
    #     st.image("/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/assets/floralogo.png")

    #     # selected_language = st.sidebar.selectbox("Choose a language", list(indian_languages.keys()), index=0)
    #     # dest_language = indian_languages[selected_language]

    #     st.info("""
    #             # About
    #             This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).

    #             # Contact
    #             For inquiries, you can mail us [here](mailto:mohrilsiddharth@gmail.com).
    #             """)
    #     st.image("/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/assets/vitlogo3.png")

def forum_page():
    # Load credentials from secrets.toml
    credentials = toml.load("/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/.streamlit/secrets.toml")
    lottie2 = """
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://lottie.host/20837e04-4218-4d4c-8889-08e2a1ddbf96/BjmCosJ0eF.json"  background="transparent"  speed="1"  style="width: 1000px; height: 1000px;"  loop  autoplay></lottie-player>
    """
    st.markdown("""
    <style>
        iframe {
            position: fixed;
            top: 2rem;
            bottom: ;
            left: 0;
            right: 0;
            margin: auto;
            z-index=-1;
        }
        .nav-pills {
            position: relative;
            z-index: 10;
        }
    </style>
    """, unsafe_allow_html=True)
    st.components.v1.html(lottie2, width=1010, height=1300)

    # Get the GSheets connection details
    gsheets_connection = credentials.get("connections", {}).get("gsheets", {})

    # Establish connection with Google Sheets using credentials
    conn = GSheetsConnection(
        connection_name="gsheets",  # Add the missing connection_name argument
        spreadsheet=gsheets_connection.get("spreadsheet"),
        worksheet=gsheets_connection.get("worksheet"),
        type=gsheets_connection.get("type"),
        project_id=gsheets_connection.get("project_id"),
        private_key_id=gsheets_connection.get("private_key_id"),
        private_key=gsheets_connection.get("private_key"),
        client_email=gsheets_connection.get("client_email"),
        client_id=gsheets_connection.get("client_id"),
        auth_uri=gsheets_connection.get("auth_uri"),
        token_uri=gsheets_connection.get("token_uri"),
        auth_provider_x509_cert_url=gsheets_connection.get("auth_provider_x509_cert_url"),
        client_x509_cert_url=gsheets_connection.get("client_x509_cert_url")
    )

    st.write("<h1>Feedback forum</h1>", unsafe_allow_html=True)

    with st.sidebar:
        st.image("assets/logo.png")
        st.info("""
                # About
                This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).

                # Contact
                For inquiries, you can mail us [here](mailto:mohrilsiddharth@gmail.com).
                """)

    home_page = st.empty()
    display_image = st.empty()
    classifying_text = st.empty()
    button = st.empty()

    card_width = 800

    st.markdown(
        f"""
        <style>
            .banner-card {{
                width: {card_width}px;
                display: flex;
                flex-direction: column;
                align-items: center;
                background-color: #f0f0f0;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
            }}
            .banner-card img {{
                width: 100%;
                border-radius: 12px;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the banner card
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        st.markdown(
            f'<div class="banner-card"><img src="data:image/jpeg;base64,{uploaded_image.read().encode("base64").decode()}"></div>',
            unsafe_allow_html=True
        )

    # Read data from the specified worksheet
    data = conn.read(worksheet="Forum")

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Check if the columns are named correctly

    with st.expander("Community Reviews"):
        for index, row in df.iterrows():
            sentiment = str(row["Sentiment"])  # Convert sentiment to string
            feedback = row["Feedback"]
            if sentiment.lower() == "positive":
                st.success(f"👍 Positive Feedback: {feedback}")
            elif sentiment.lower() == "negative":
                st.error(f"👎 Negative Feedback: {feedback}")
            else:
                st.warning(f"Unrecognized sentiment: {sentiment}")


    # Create an input field for feedback
    feedback_input = st.text_area("Enter Feedback")

    # Perform sentiment analysis using TextBlob
    blob = TextBlob(feedback_input)
    sentiment = blob.sentiment.polarity
    sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"

    # Add a button to submit the feedback and sentiment
    if st.button("Submit"):
        # Append the new feedback and sentiment to the DataFrame
        new_entry = {"0": sentiment_label, "1": feedback_input}
        df = df.append(new_entry, ignore_index=True)

        # Write the updated DataFrame back to the Google Sheets document
        conn.update(worksheet="Forum", data=df.values.tolist())

        st.success("Feedback submitted successfully!")

# Function to display the news page content
def news_page():
    clear_page()  # Clear the page
    lottie3 = """
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://lottie.host/b60fff1d-cbeb-4d41-aba1-b624200c0513/OoZwK6n4cr.json"  background="transparent"  speed="2.75"  style="width: 1000px; height: 1000px;"  loop  autoplay></lottie-player>
    """
    st.markdown("""
    <style>
        iframe {
            position: fixed;
            top: 2rem;
            bottom: ;
            left: 0;
            right: 0;
            margin: auto;
            z-index=-1;
        }
        .nav-pills {
            position: relative;
            z-index: 10;
        }
    </style>
    """, unsafe_allow_html=True)
    # st.components.v1.html(lottie3, width=1010, height=1010)
    API_KEY = "8efc9c32c15e48a995ee95ea892226ee"
    news_data = requests.get(f'https://newsapi.org/v2/everything?q=plant%20disease&apiKey={API_KEY}&language=en&searchIn=title').json()['articles']

    for random_news in news_data:
        st.write(f"""<h2>{html.unescape(random_news['title'])}</h2><br>""", unsafe_allow_html=True)
        try:
            if random_news["urlToImage"]:
                st.image(f'{random_news["urlToImage"]}')
        except MediaFileStorageError:
            st.image("https://unsplash.com/photos/red-and-green-leaf-in-close-up-photography-E3g2UP9WoLU")
        st.write(f"""
            <h5>{random_news['description']}</h5>
            Link : <a href="{random_news['url']}">{random_news['url'][:80]}...</a><br>
            Author : {random_news['author']}, &nbsp; <i>{random_news['publishedAt'][:10]}</i>
            <hr>
            """, unsafe_allow_html=True)



# Main function
def main():
    st.set_page_config(
        page_title='FloraMD',
        page_icon='🌱',
        layout='wide',
        initial_sidebar_state='collapsed'
    )

    home_page_content = home_page  # Save the home page content function
    with st.sidebar:
        st.image("/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/assets/floralogo.png")

        selected_language = st.sidebar.selectbox("Choose a language", list(indian_languages.keys()), index=0)
        dest_language = indian_languages[selected_language]

        st.info("""
                # About
                This is a web app to predict the disease in a plant using Convolutional Neural Network (CNN).

                # Contact
                For inquiries, you can mail us [here](mailto:mohrilsiddharth@gmail.com).
                """)
        st.image("/Users/Sid/Downloads/Project Exib 2/Plant_Disease_Detection-main/assets/vitlogo3.png")


    with st.container():
    # Lottie animations
        lottie = """
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src="https://lottie.host/5ca098aa-290c-4091-9548-f8f46c51b8ce/gzqvydc0py.json"  background="transparent"  speed="2"  style="width: 2000px; height: 2000px;"  loop  autoplay></lottie-player>
        """
        st.markdown("""
            <style>
                iframe {
                    position: fixed;
                    top: 2rem;
                    bottom: 0;
                    left: 0;
                    right: 0;
                    margin: auto;
                    z-index=-1;
                }
                .nav-pills {
                    position: relative;
                    z-index: 10;
                    background-color: #fff;
                    padding: 10px;
                    border-radius: 10px;
                }
            </style>
            """, unsafe_allow_html=True)
        st.components.v1.html(lottie, width=2010, height=2010)

        lottie3 = """
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src="https://lottie.host/b60fff1d-cbeb-4d41-aba1-b624200c0513/OoZwK6n4cr.json"  background="transparent"  speed="2.75"  style="width: 2000px; height: 2000px;"  loop  autoplay></lottie-player>
        """
        st.markdown("""
        <style>
            iframe {
                position: fixed;
                top: 2rem;
                bottom: ;
                left: 0;
                right: 0;
                margin: auto;
                z-index=-1;
            }
            .nav-pills {
                position: relative;
                z-index: 10;
            }
        </style>
        """, unsafe_allow_html=True)
        st.components.v1.html(lottie3, width=2010, height=2010)

        lottie2 = """
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src="https://lottie.host/20837e04-4218-4d4c-8889-08e2a1ddbf96/BjmCosJ0eF.json"  background="transparent"  speed="1"  style="width: 1000px; height: 1000px;"  loop  autoplay></lottie-player>
        """
        st.markdown("""
        <style>
            iframe {
                position: fixed;
                top: 2rem;
                bottom: ;
                left: 0;
                right: 0;
                margin: auto;
                z-index=-1;
            }
            .nav-pills {
                position: relative;
                z-index: 10;
            }
        </style>
        """, unsafe_allow_html=True)
        st.components.v1.html(lottie2, width=1010, height=1300)

    with st.container():
        # Option menu is placed here
        app_mode = option_menu(
        options=["Home", "Predict", "ChatBot", "News", "Forum", "Team"],
        orientation="horizontal",
        menu_title="",
        styles={"nav-link-selected": {"background-color": "#A47CF3"}}
    )
        pass  # Replace with your option menu code

    st.markdown("""
    <style>
        iframe {
            position: fixed;
            top: 2rem;
            bottom: ;
            left: 0;
            right: 0;
            margin: auto;
            z-index=-3000000;
        }
        .nav-pills {
            position: relative;
            z-index: 10000;
        }
    </style>
    """, unsafe_allow_html=True)

    # Determine which page to display based on the selected mode
    if app_mode == "Home":
        home_page_content()  # Display home page content
    elif app_mode == "Predict":
        st.write("Welcome to the Prediction Page!")
    elif app_mode == "ChatBot":
        st.empty()
        chat_bot()
    elif app_mode == "News":
        news_page()  # Display news page content
    elif app_mode == "Forum":
        forum_page()
    elif app_mode == "Team":
        st.write("Welcome to the Team Page!")


if __name__ == "__main__":
    main()