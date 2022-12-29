# https://discuss.streamlit.io/t/how-to-embed-javascript-into-streamlit/20152/3

import streamlit as st
import streamlit.components.v1 as components

st.title("meilisearch")

# HtmlFile = open("./meilisearch.html", 'r', encoding='utf-8')
# source_code = HtmlFile.read() 
# components.html(source_code, height=600, scrolling=True)

js = """
    const streamlit_example_search_key = process.env.streamlit_example_search_key

    const search = instantsearch({
      indexName: "web_preprocessed",
      searchClient: instantMeiliSearch(
        "https://ms-6b9ae8855fa6-1312.fra.meilisearch.io",
        """ + st.secrets["streamlit_example_search_key"] + """, // api key for searching
      )
    });
      
    search.addWidgets([
      instantsearch.widgets.searchBox({
        container: "#searchbox"
      }),
      // instantsearch.widgets.configure({ hitsPerPage: 8 }),
      instantsearch.widgets.hits({
        container: "#hits",
        templates: {
          item: `
            <div>
              <div class="hit-name" align="center">
                <b>{{#helpers.highlight}}{ "attribute": "title" }{{/helpers.highlight}}</b><br><br>
                {{#helpers.highlight}}{ "attribute": "text" }{{/helpers.highlight}}<br><br>
                <i>{{#helpers.highlight}}{ "attribute": "url" }{{/helpers.highlight}}</i>
              </div>
            </div>
          `
        }
      })
    ]);
    
    search.start();

"""

html = f"""
<!DOCTYPE html>
<html lang="en">
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
  <script>
    {js}
  </script>
</html>
"""

components.html(html)