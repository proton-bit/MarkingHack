import pandas as pd
import numpy as np
from config import *

input_data = pd.read_parquet(INPUT_CIRCULATION_FILENAME).iloc[::5]
transition_data = pd.read_parquet(TRANSITION_CICULATION_FILENAME).iloc[::100]
output_data = pd.read_parquet(
    OUTPUT_CIRCULATION_FILENAME,
    dtype={'price': np.uint32, 'cnt': np.uint32},
    parse_dates=['dt']
).iloc[::200]

input_data.to_parquet(INPUT_CIRCULATION_PARQUET_FILENAME)
transition_data.to_parquet(TRANSITION_CIRCULATION_PARQUET_FILENAME)
output_data.to_parquet(OUTPUT_CIRCULATION_PARQUET_FILENAME)