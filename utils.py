import streamlit as st
import json, re, requests, os
from dotenv import dotenv_values

config = dotenv_values('.env')
blogger_api_key = config['BLOGGER_API_KEY']
blog_id = config['BLOG_ID']

@st.cache_data
def load_timeline_data():
    f = open('timeline3.json', 'r') if 'timeline.json' not in os.listdir() else open('timeline.json', 'r')
    data = f.read()
    f.close()
    
    return json.loads(data)

def get_timeline_data(censura=False):
    f = open('timeline3.json', 'r') if 'timeline.json' not in os.listdir() else open('timeline.json', 'r')
    data = f.read()
    f.close()
    
    return json.loads(data)

def get_blogger_posts():
    return requests.get(f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts?key={blogger_api_key}').json()

def urls_from_blog(censura=False):
    blog_post = get_blogger_posts()['items'][0]['content']
    pattern = r'src="([^"]+)"'
    return re.findall(pattern, blog_post)

def links_not_in_doc(events, links, tuples=False):
    events = {event['media']['url'] for event in events}
    if tuples:
        return [(name, link) for name, link in links if link not in events]
    else:
        return list(set(links).difference(events))