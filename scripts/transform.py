import pandas as pd
import numpy as np
from write_to_log import log
import datetime
import json

# Load the data from a JSON file
with open('data/raw/raw_data.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

raw_data = pd.DataFrame(json_data['data'])
raw_data['departure'] = raw_data['departure'].apply(lambda x: x['airport'])
raw_data['arrival'] = raw_data['arrival'].apply(lambda x: x['airport'])
raw_data['airline'] = raw_data['airline'].apply(lambda x: x['name'])
raw_data['flight'] = raw_data['flight'].apply(lambda x: x['number'])
raw_data = raw_data[['flight_date', 'flight_status', 'departure', 'arrival', 'airline', 'flight']]
raw_data.replace('', np.nan, inplace=True)
raw_data.drop_duplicates(keep='first', inplace=True)

# Save the transfromed data into a csv file
raw_data.to_csv('data/processed/processed_data.csv', index=False)
log_message = f'Message {datetime.datetime.now()}: Transfromed Data has been successfuly saved on the processed directory of the project\n'
log(log_message)
