import streamlit as st
import webbrowser
from creds import *

st.set_page_config(page_title="Login")

st.session_state['auth_status'] = False

st.title("Login")

with st.form("login_form"):
    user = st.text_input("Nome de usuário:")
    psswd = st.text_input("Senha:", type='password')
    sub = st.form_submit_button("Enviar")

if sub:
    if (user == username and psswd == pass_) or (user == adm and psswd == adm):
        st.session_state['auth_status'] = True
        st.switch_page('pages/home.py')
    else:
        st.error(message)