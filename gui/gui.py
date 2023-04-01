from io import StringIO
import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import json 

config = json.load(open('interface.json'))


st.title(config["title"])


uploaded_file = st.file_uploader(config["upload_1"])
if uploaded_file is not None:

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

    