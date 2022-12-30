# https://discuss.streamlit.io/t/how-to-embed-javascript-into-streamlit/20152/3

import streamlit as st
import streamlit.components.v1 as components

st.title("meilisearch")

HtmlFile = open("./meilisearch.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=600, scrolling=True)
