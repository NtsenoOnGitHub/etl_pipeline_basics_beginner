import pandas as pd
import extract
import os
import datetime
import requests
from write_to_log import log
import json

# Load the data from a JSON file
with open('data/raw/raw_data.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

entries = raw_data[1]  # data[0] is metadata, data[1] contains the records
dataFrame = pd.DataFrame(entries) # Create DataFrame
dataFrame = dataFrame[['country', 'date', 'value']] # Take colums you intrested in
dataFrame["country"] = dataFrame["country"].apply(lambda x: x["value"]) # Clean up the messy columns
dataFrame.to_csv('data/processed/processed_data.csv')