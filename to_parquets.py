import pandas as pd
import numpy as np
from config import *

input_data = pd.read_csv(INPUT_CIRCULATION_FILENAME)
transition_data = pd.read_csv(TRANSITION_CICULATION_FILENAME)
output_data = pd.read_csv(
    OUTPUT_CIRCULATION_FILENAME,
    dtype={'price': np.uint32, 'cnt': np.uint32},
    parse_dates=['dt']
)

input_data.to_parquet(INPUT_CIRCULATION_PARQUET_FILENAME)
transition_data.to_parquet(TRANSITION_CIRCULATION_PARQUET_FILENAME)
output_data.to_parquet(OUTPUT_CIRCULATION_PARQUET_FILENAME)