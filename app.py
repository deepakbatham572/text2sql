import streamlit as st
from utils import *


if 'API_KEY' not in st.session_state:
    st.session_state['API_KEY'] = ''

st.set_page_config("Text to SQL" , page_icon=":moon:")
st.title("Welcome to the Text To SQL with LLM")

st.sidebar.title('😎🔑')
st.session_state['API_KEY'] = st.sidebar.text_input('Enter your HuggingFace Key here :' , type='password')

text = st.text_area("Enter your description here:" , height=120)
creativity = st.slider("Select your creativity here:" , 0.0 ,1.0 , step=0.1)
submit = st.button("Generate")

if submit:
       response = get_sql(text , creativity , st.session_state['API_KEY'])
       st.write(response)