import pandas as pd
import requests
import os
import datetime
from write_to_log import log
from dotenv import load_dotenv
import os
import json

# load_dotenv('config/.env')
api_key = os.getenv('API_KEY')

# Extract data from The World Bank using API call
# - APIKEY is your secret api key from your openWeatherMap account
# - This will return a data in a json format
def extract_data(API_KEY: str):
    try:
        url = f'https://api.aviationstack.com/v1/flights?access_key={API_KEY}' #replace with actual API_KEY AFTER TESTING
        response = requests.get(url)
        return response.json()
    except:
        error_message = f'Error {datetime.datetime.now()}: Something went wrong while extracting data with your api key\n'
        log(error_message)


# You can change the url parameters to get different data or change the url all together.
raw_data = extract_data(api_key)

if raw_data is None:
    print('An Error has occured, check the program.log file for more details')

elif isinstance(raw_data, list) or isinstance(raw_data, dict): # Public AIP call 
    log_message = f'Message {datetime.datetime.now()}: Data has been extracted successfuly from a public API on an API call\n'
    log(log_message)
    with open('data/raw/raw_data.json', 'w', encoding='utf-8') as f:
        json.dump(raw_data, f, ensure_ascii=False, indent=4)
    log_message = f'Message {datetime.datetime.now()}: Data has been successfuly saved on the raw directory of the project\n'
    log(log_message)
