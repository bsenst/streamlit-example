from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

# https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/

from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.set_page_config(layout="wide")

st.title("Angebote der Obdachlosenhilfe")

import streamlit.components.v1 as components

HtmlFile = open("./map-obdachlosenhilfe.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code), height=1200)

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # modify = st.checkbox("Filter hinzufügen")
    modify = True

    if not modify:
        return df
    
    df = df.copy()

    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter anwenden", df.columns[:2])
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Werte für {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Werte für {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Werte für {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.multiselect(
                    f"Werte für {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                if user_text_input:
                    df = df[df[column].isin(user_text_input)]
    return df

df = pd.read_json("obdachlosenhilfe-7v.json")

st.dataframe(filter_dataframe(df))
