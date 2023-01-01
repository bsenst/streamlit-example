import json
import streamlit as st

with open("fulltext_subset.json") as infile:
    docs = json.load(infile)

from haystack.document_stores import InMemoryDocumentStore
document_store = InMemoryDocumentStore()
document_store.write_documents(docs)

from haystack.nodes import TfidfRetriever
retriever = TfidfRetriever(document_store=document_store)

from haystack.nodes import TransformersReader
reader = TransformersReader(model_name_or_path="deepset/gelectra-base-germanquad-distilled", tokenizer="deepset/gelectra-base-germanquad-distilled", use_gpu=-1)

from haystack.pipelines import ExtractiveQAPipeline
pipe = ExtractiveQAPipeline(reader, retriever)

question = st.text_input('', 'Welche Dienste bietet das Deutsche Rote Kreuz?')

if question != "":
    prediction = pipe.run(
        query=question, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
    )

    for answer in prediction["answers"]:
        st.write(answer)