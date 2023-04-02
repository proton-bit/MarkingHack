import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from supply_chain import create_supply_chains
from utils import empty_page
import os
import json


with open("interface.json") as f:
    config = json.load(f)

def page1_gui():
    def update_map():
        geodata = create_supply_chains(st.session_state.threshold_slider)
        layers = [basic_layer(geodata)] 

        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": avg_latitude,
                "longitude": avg_longtitude,
                "zoom": 5,
                "pitch": 50,
            },
            layers=layers,
        )

    st.set_page_config(page_title=config["mappage_title"], page_icon="🌍")

    st.title(config["mappage_title"])
    st.sidebar.header(config["mappage_title"])

    # geodata_path =  os.path.join(config["download_folder"], config["geochain_filename"])

    threshold = st.sidebar.slider(
        config["threshold_sidebar_text"], 
        max_value=6, 
        min_value=2,
        value=5, 
        key="threshold_slider",
        on_change=update_map
        )

    geodata = create_supply_chains(threshold)

    avg_latitude = ((geodata.lat + geodata.lat2)/2).sum() / len(geodata)
    avg_longtitude = ((geodata.lon + geodata.lon2)/2).sum() / len(geodata)



    def basic_layer(data):
        return pdk.Layer(
                "ArcLayer",
                data=data,
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[255, 0, 0, 100],
                get_target_color=[0, 0, 255, 100],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            )


    try:
        layers = [basic_layer(geodata)]

        if layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={
                        "latitude": avg_latitude,
                        "longitude": avg_longtitude,
                        "zoom": 5,
                        "pitch": 50,
                    },
                    layers=layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
        
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )

if os.path.exists(os.path.join(config["download_folder"], config["geochain_filename"])):
    page1_gui()
else:
    empty_page()
 