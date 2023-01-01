# https://www.kdnuggets.com/2021/10/simple-question-answering-web-app-hugging-face-pipelines.html

import streamlit as st
from transformers import pipeline

# App title and description
st.title("Fragen und Antworten")

# Perform question answering
question_answerer = pipeline('question-answering')

answer = ''
question = st.text_input('Ask a question')

if question != '':
    answer = question_answerer({
        'question': question,
        'context': "42 is the answer to everything"
    })

st.write(answer)