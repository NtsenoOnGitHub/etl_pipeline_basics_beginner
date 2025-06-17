import pandas as pd
import numpy as np
from write_to_log import log
import json

# Load the data from a JSON file
with open('data/raw/raw_data.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

csv_data = pd.DataFrame(json_data[1])
csv_data = csv_data[['country', 'countryiso3code', 'date', 'value']]
csv_data['country'] = csv_data['country'].apply(lambda x: x['value'])
columns = ['Country', 'Country_code', 'Date', 'Population_Value']
csv_data.columns = columns
csv_data.replace('', np.nan, inplace=True)
csv_data.dropna(inplace=True)
csv_data.drop_duplicates(keep='first', inplace=True)

# Save the transfromed data into a csv file
csv_data.to_csv('data/processed/processed_data.csv', index=False)

csv_data = pd.read_csv('data/processed/processed_data.csv')