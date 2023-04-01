import streamlit as st
import time
import numpy as np
import os
import json 

with open('interface.json') as f:
    config = json.load(f)

st.set_page_config(page_title=config["upload_2"], page_icon="📈")

def page2_gui_positive():
    st.markdown(f"# {config['upload_2']}")
    st.sidebar.header(config["upload_2"])
    st.write(
        """This demo illustrates a combination of plotting and animation with
    Streamlit. We're generating a bunch of random numbers in a loop for around
    5 seconds. Enjoy!"""
    )

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

def page2_gui_negative():
    st.title(config["missing_data_message"])

if os.path.exists(os.path.join(config["download_folder"], "input.parquet")):
    page2_gui_positive()
else:
    page2_gui_negative()
 