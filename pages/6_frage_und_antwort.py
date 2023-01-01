st.caption("https://www.kdnuggets.com/2021/10/simple-question-answering-web-app-hugging-face-pipelines.html")

import streamlit as st
# from transformers import pipeline

# App title and description
st.title("Frage und Antwort")

# Perform question answering
# question_answerer = pipeline('question-answering')

answer = ''
question = st.text_input('', 'Stell deine Frage')

# if question != '':
#     answer = question_answerer({
#         'question': question,
#         'context': "42 is the answer to everything"
#     })

st.write(answer)

st.caption("# https://gist.github.com/demarant/d9e617fb80057692f2f7cddf00013b9b")

import streamlit as st
import requests
from annotated_text import annotated_text

st.set_page_config(
     page_title="Haystack - Ask me something and get an answer!",
     page_icon=":crown:",
     layout="centered",
     initial_sidebar_state="auto",
)

st.title(':crown: Haystack QA demo app')
'*This application demonstrates how Modern NLP models can understand questions in natural language and find the answer among many documents in so called golden passages of text. It is not a >
st.subheader('Ask me something and get an answer')
question=st.text_input('')
params = {'questions':[],'top_k_retrievet': 5}
params['questions']= [question]
import json
data = json.dumps(params)

st.sidebar.subheader('Options')
nr_of_answers = st.sidebar.slider('How many relevant answers do you want?', min_value=1, max_value=5)


@st.cache(show_spinner=False)
def get_answers(data):
    response = requests.post(f"https://haystack-demo-api.deepset.ai/models/1/doc-qa", data=data,
       headers={
       "Content-Type": "application/json",
       "accept": "application/json"
       }
    )
    return response.json()

def annotate_context(answer, context):
    idx = context.find(answer)
    idx_end = idx + len(answer)
    annotated_text(context[:idx],(answer,"","#adff2f"),context[idx_end:],)

if question:
   with st.spinner(text=':crown: Looking for answers...'):
      results = get_answers(data)
      if results['results']:
         for i in range(nr_of_answers):
            answer = results['results'][0]['answers'][i]['answer']
            #answer_display.subheader(answer)
            if answer:
                context = '...' + results['results'][0]['answers'][i]['context'] + '...'
                document_name = results['results'][0]['answers'][i]['meta']['name']
                relevance_pct = round(results['results'][0]['answers'][i]['probability']*100,2)
                annotate_context(answer, context)
                '**Relevance:** ', relevance_pct , '**source:** ' , document_name

if question and st.sidebar.checkbox('Show debug info'):
    st.subheader('REST API JSON response')
    st.write(results)