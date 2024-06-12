import streamlit as st
from utils.utils import load_header
from utils.constants import CONTRIBUTORS

def about_us_page(contributors):
    load_header("Meet our CONTRIBUTORS")
    
    data = contributors
    full_string = ""
    
    for i in range(0, len(data), 3):
        try:
            contributor1_name, contributor1_link = data[i]
            contributor2_name, contributor2_link = data[i+1]
            contributor3_name, contributor3_link = data[i+2]

            CONTRIBUTORS = f"""<tr>
                <td><a href='{contributor1_link}'>{contributor1_name}</a></td>
                <td><a href='{contributor2_link}'>{contributor2_name}</a></td>
                <td><a href='{contributor3_link}'>{contributor3_name}</a></td> 
            </tr>
            """
            full_string += CONTRIBUTORS
        
        except IndexError:
            if len(data[i:])==2:
                full_string += f"""<tr>
                        <td>
                            <a href='{data[i:][0][1]}'>{data[i:][0][0]}</a>
                        </td>
                        <td>
                            <a href='{data[i:][1][1]}'>{data[i:][1][0]}</a>
                        </td>
                    </tr>
                """
            elif len(data[i:])==1:
                full_string += f"""<tr>
                        <td>
                            <a href='{data[i:][0][1]}'>{data[i:][0][0]}</a> <a 
                        </td>
                    </tr>
                """
    with open('assets/html/about.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
        
    st.write(html_content.format(team=full_string), unsafe_allow_html=True)
    
        
if __name__ == "__main__":
    about_us_page(CONTRIBUTORS)