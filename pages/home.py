import streamlit as st
from streamlit_timeline import timeline
from time import sleep
from utils import load_timeline_data
from youtube_auto import youtube_auto

st.set_page_config(page_title="Nossa linha do tempo💛", layout="wide")

if 'auth_status' not in st.session_state or not st.session_state.auth_status:
    st.info('Sai daqui mocreia.')
    sleep(2)
    st.switch_page('./app.py')

st.title('Nossa linha do tempo💛')


data = load_timeline_data()

# render timeline
timeline(data, height=750)

if st.button("Clear All"):
    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()
    st.rerun()

if st.button('YOUTUBE'):
    youtube_auto()