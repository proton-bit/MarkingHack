import plotly.express as px
from typing import List
import streamlit as st
import pydeck as pdk
import pandas as pd
import json
import os 

config = json.load(open('interface.json'))

def upload_form(name:str, columns:List[str], file_format:str='.csv') -> pd.DataFrame:
    user_query = st.text_input(label=f"Enter link to {name}", key=f"{name}_form")
    if st.button('Search', key=f"{name}_button"):
        if user_query:
            if file_format == ".csv":
                data = pd.read_csv(user_query)
            elif file_format == ".parquet":
                data = pd.read_parquet(user_query)
            else:
                AssertionError(f"{file_format} is not expected")
            if set(data.columns) == set(columns):
                st.sidebar.success(f"{name} {config['emojies']['done']}")
            else:
                st.sidebar.warning(f"{name} {config['warning']['wrong_columns_warning_p1']} {config['required_columns'][name]} {'wrong_columns_warning_p1'} {list(data.columns)} ")
        