# https://discuss.streamlit.io/t/how-to-embed-javascript-into-streamlit/20152/3

import streamlit as st
from streamlit.components.v1 import html

# Define your javascript
my_js = """
    const search = instantsearch({
      indexName: "movies",
      searchClient: instantMeiliSearch(
        "http://localhost:7700"
      )
      });
      search.addWidgets([
        instantsearch.widgets.searchBox({
          container: "#searchbox"
        }),
        instantsearch.widgets.configure({ hitsPerPage: 8 }),
        instantsearch.widgets.hits({
          container: "#hits",
          templates: {
          item: `
            <div>
            <div class="hit-name">
                  {{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}
            </div>
            </div>
          `
          }
        })
      ]);
      search.start();
"""

# Wrapt the javascript as html code
my_html = f"""
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@meilisearch/instant-meilisearch/templates/basic_search.css" />
    </head>
    <body>
        <div class="wrapper">
        <div id="searchbox" focus></div>
        <div id="hits"></div>
        </div>
    </body>
    <script src="https://cdn.jsdelivr.net/npm/@meilisearch/instant-meilisearch/dist/instant-meilisearch.umd.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4"></script>
    <script>{my_js}</script>"""

# Execute your app
st.title("meilisearch example")
html(my_html)