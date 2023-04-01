from utils import upload_form 
import plotly.express as px
import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import json 

config = json.load(open('interface.json'))

st.set_page_config(
    page_title=f"{config['title']}" ,
    page_icon=config["emojies"]["pushpin"],
)

st.title(f"{config['title']} {config['emojies']['uptrend']}")

input_circulation_data = upload_form(
    config["upload_1"], 
    config["required_columns"][config["upload_1"]],
    file_format='.parquet'
    )
output_circulation_data = upload_form(
    config["upload_2"], 
    config["required_columns"][config["upload_2"]],
    file_format='.parquet'
    )
transition_circulation_data = upload_form(
    config["upload_3"], 
    config["required_columns"][config["upload_3"]],
    file_format='.parquet'
    )
product_handbook_data = upload_form(
    config["upload_4"],
    config["required_columns"][config["upload_4"]],
    file_format='.csv'
    )
outlet_handbook_data = upload_form(
    config["upload_5"],
    config["required_columns"][config["upload_5"]],
    file_format='.csv'
    )
participants_handbook_data = upload_form(
    config["upload_6"],
    config["required_columns"][config["upload_6"]],
    file_format='.csv'
    )
