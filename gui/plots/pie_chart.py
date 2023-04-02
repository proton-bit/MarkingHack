import plotly.express as px
import pandas as pd
import json

with open('interface.json') as f:
    config = json.load(f)

def generate_pie_chart(df:pd.DataFrame, column:str):
    return px.pie(
        df,
        names = 'operation_type',
        title=f"{config['plot_messages']['piechart_title_prefix']} <<{column}>>"
    )