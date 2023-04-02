import streamlit as st
import os
import json 
import pandas as pd
from pandas.api.types import is_numeric_dtype
import plotly.graph_objects as go
from plots.pie_chart import generate_pie_chart
from plots.box_plot import generate_box_plot

with open('interface.json') as f:
    config = json.load(f)

st.set_page_config(page_title=config["upload_2"], page_icon="📈")

def page3_gui_positive():
    st.title(config['upload_2'])
    
    df = pd.read_parquet(os.path.join(config["download_folder"], config["output_filename"]))
    
    st.write(df.head(config["n_rows_table"]))
    st.write(df.describe())

    st.plotly_chart(generate_pie_chart(df, "type_operation"))

    option = st.selectbox(
        'Pick column with numerical values',
        [col for col in list(df.columns) if is_numeric_dtype(df[col])]
    )
    st.plotly_chart(generate_box_plot(df.sample(config["max_data_points"]), option))

def page3_gui_negative():
    st.title(config["missing_data_message"])

if os.path.exists(os.path.join(config["download_folder"], "output.parquet")):
    page3_gui_positive()
else:
    page3_gui_negative()
 