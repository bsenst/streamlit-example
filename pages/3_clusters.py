# https://github.com/max-lutz/national-assembly

import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.backends.backend_agg import RendererAgg
from PIL import Image

#Loading the data
@st.cache
def get_data_clusters():
     return pd.read_csv(os.path.join(os.getcwd(),'df_clusters.csv'), index_col=0)

#configuration of the page
st.set_page_config(layout="wide")

#load dataframes
df_clusters = get_data_clusters()
st.title('Cluster analysis')
st.markdown("""The notebook performing the clustering can be found here: https://www.kaggle.com/bnzn261029/work-with-clustered-texts

This page of the streamlit multipage app has been created using code from: https://github.com/max-lutz/national-assembly""")

image = Image.open('8_clusters.png')
st.image(image, caption='8 clusters')

st.sidebar.header('Select what to display')
clusters = df_clusters['cluster'].unique().tolist()
clusters_selected = st.sidebar.multiselect('Cluster group', 
clusters, clusters)

nb_docs = df_clusters['cluster'].value_counts()
nb_docs_slide = st.sidebar.slider("Cluster per number of documents", 
int(nb_docs.min()), int(nb_docs.max()), 
(int(nb_docs.min()), int(nb_docs.max())), 1)

#creates masks from the sidebar selection widgets
mask_cluster = df_clusters['cluster'].isin(clusters_selected)

#get the clusters with a number in the defined range
mask_docs = df_clusters['cluster'].value_counts().between(nb_docs_slide[0], 
nb_docs_slide[1]).to_frame()
mask_docs= mask_docs[mask_docs['cluster'] == 1].index.to_list()
mask_docs= df_clusters['cluster'].isin(mask_docs)

df_cluster_filtered = df_clusters[mask_cluster  & mask_docs]
st.write(df_cluster_filtered)

matplotlib.use("agg")
_lock = RendererAgg.lock

cluster_counts = df_cluster_filtered['cluster'].value_counts()

#merge the two dataframe to get a column with the color
df = pd.merge(pd.DataFrame(cluster_counts), df_clusters, left_index=True, 
right_on='cluster')
cluster = df['cluster'].tolist()

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((0.2, 1, .2, 1, .2))
with row0_1, _lock:
    st.header("Clusters")
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(cluster_counts, labels=(cluster_counts.index))
    #display a white circle in the middle of the pie chart
    p = plt.gcf()
    p.gca().add_artist(plt.Circle( (0,0), 0.7, color='white'))
    st.pyplot(fig)

st.header("Topic modeling")
st.write("Themen der Cluster (topic modelling - manuell)")
st.markdown("""
* 0 - Meldungen
* 1 - Meldungen
* 2 - Warenkorb, Weiterempfehlen
* 3 - Stellen
* 4 - Kurse
* 5 - Kurse
* 6 - Kurse
* 7 - Verbandsverzeichnis""")