import streamlit as st

from algoliasearch.search_client import SearchClient

client = SearchClient.create('S1ZBLN0UEH', '5c9ca20b4f60ea3d32b4c1986009e460') # search only api key, for frontend use
index = client.init_index('obdachlosenhilfe-index')

st.header("algoliasearch")
st.caption("search a subset of the dataset, limited search only as offered by free tier https://www.algolia.com/")

query = st.text_input("", "Kältebus")
button_clicked = st.button("Suchen")

if button_clicked:
    # Search for "query string" in the index "contacts"
    res = index.search(query)

    st.write("Anzahl der Suchergebnisse:", res["nbHits"])

    for i, hit in enumerate(res["hits"]):
        st.write(i+1, hit["url"])
        with st.expander(hit["title"]):
            st.caption(hit["text"])