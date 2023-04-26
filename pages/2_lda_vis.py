# https://discuss.streamlit.io/t/how-to-embed-javascript-into-streamlit/20152/3

import streamlit as st
import streamlit.components.v1 as components

st.title("LDA Topic Modeling")

HtmlFile = open("./lda.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=900, scrolling=True)

HtmlFile = open("./pyLDAvis.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height=900, scrolling=True)
