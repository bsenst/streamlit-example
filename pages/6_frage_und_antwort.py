import json

with open("fulltext_subset.json") as infile:
    docs = json.load(infile)

from haystack.document_stores import InMemoryDocumentStore
document_store = InMemoryDocumentStore()
document_store.write_documents(docs)

from haystack.nodes import TfidfRetriever
retriever = TfidfRetriever(document_store=document_store)

from haystack.nodes import TransformersReader
reader = TransformersReader(model_name_or_path="deepset/xlm-roberta-base-squad2", tokenizer="deepset/xlm-roberta-base-squad2", use_gpu=-1)

from haystack.pipelines import ExtractiveQAPipeline
pipe = ExtractiveQAPipeline(reader, retriever)

prediction = pipe.run(
    query="Welche Dienste bietet das Deutsche Rote Kreuz?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
)

print(prediction["answers"])