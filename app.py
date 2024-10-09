import streamlit as st

st.set_page_config(page_title="Login")

st.session_state['auth_status'] = False

st.title("Login")

with st.form("login_form"):
    user = st.text_input("Nome de usuário:")
    psswd = st.text_input("Senha:", type='password')
    sub = st.form_submit_button("Enviar")

if sub:
    if (user == st.secrets['USERNAME'] and psswd == st.secrets['PSSWD']) or (user == st.secrets['ADMIN'] and psswd == st.secrets['ADMIN_PSSWD']):
        st.session_state['auth_status'] = True
        st.switch_page('pages/home.py')
    else:
        st.error(st.secrets['MSG'])