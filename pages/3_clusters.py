# https://github.com/max-lutz/national-assembly

import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.backends.backend_agg import RendererAgg

#Loading the data
@st.cache
def get_data_clusters():
     return pd.read_csv(os.path.join(os.getcwd(),'df_clusters.csv'))

#configuration of the page
st.set_page_config(layout="wide")

#load dataframes
df_clusters = get_data_clusters()
# st.title('title')
# st.markdown("""...""")
st.write(df_clusters)
