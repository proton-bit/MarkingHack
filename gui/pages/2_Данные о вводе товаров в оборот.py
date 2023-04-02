import streamlit as st
import time
import numpy as np
import os
import json 
import pandas as pd

from plots.pie_chart import generate_pie_chart
from plots.box_plot import generate_box_plot

with open('interface.json') as f:
    config = json.load(f)

st.set_page_config(page_title=config["upload_1"], page_icon="📈")

def page2_gui_positive():
    st.title(config['upload_1'])
    
    df = pd.read_parquet(os.path.join(config["download_folder"], config["input_filename"]))
    
    st.write(df.head(config["n_rows_table"]))
    st.plotly_chart(generate_pie_chart(df, "operation_type"))
    st.plotly_chart(generate_box_plot(df.sample(300), "cnt"))

def page2_gui_negative():
    st.title(config["missing_data_message"])

if os.path.exists(os.path.join(config["download_folder"], "input.parquet")):
    page2_gui_positive()
else:
    page2_gui_negative()
 