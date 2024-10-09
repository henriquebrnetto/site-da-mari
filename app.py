import streamlit as st
import webbrowser
from creds import *
from dotenv import dotenv_values

config = dotenv_values('.env')

st.set_page_config(page_title="Login")

st.session_state['auth_status'] = False

st.title("Login")

with st.form("login_form"):
    user = st.text_input("Nome de usuário:")
    psswd = st.text_input("Senha:", type='password')
    sub = st.form_submit_button("Enviar")

if sub:
    if (user == config['USERNAME'] and psswd == config['PSSWD']) or (user == config['ADMIN'] and psswd == config['ADMIN_PSSWD']):
        st.session_state['auth_status'] = True
        st.switch_page('pages/home.py')
    else:
        st.error(message)