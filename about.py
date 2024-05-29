import streamlit as st
from utils import load_header

def about_us_page():
    load_header("Meet our Contributors")
    
    with open("assets/txt/contributors.txt", "r") as f:
        data = f.read().splitlines()
        full_string = ""
        
        for i in range(0, len(data), 3):
            try:
                contributor1 = data[i].split(",")[0].strip().title()
                contributor2 = data[i + 1].split(",")[0].strip().title()
                contributor3 = data[i + 2].split(",")[0].strip().title()

                contributors = f"""<tr>
                    <td>{contributor1}</td>
                    <td>{contributor2}</td>
                    <td>{contributor3}</td>
                </tr>
                """
                full_string += contributors
            
            except IndexError:
                if len(data[i:])==2:
                    full_string += f"""<tr>
                            <td>
                                {data[i:][0].split(",")[0].strip().title()}
                            </td>
                            <td>
                                {data[i:][1].split(",")[0].strip().title()}
                            </td>
                        </tr>
                    """
                elif len(data[i:])==1:
                    full_string += f"""<tr>
                            <td>
                                {data[i:][0].split(",")[0].strip().title()}
                            </td>
                        </tr>
                    """
        with open('assets/html_components/team.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
            
        st.write(html_content.format(team=full_string), unsafe_allow_html=True)