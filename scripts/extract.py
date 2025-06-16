import pandas as pd
import requests
import os
import datetime
from write_to_log import log
import json

api_key = os.getenv('API_KEY')

# Extract data from The World Bank using API call
# - APIKEY is your secret api key from your openWeatherMap account
# - This will return a data in a json format
def extract_data(url: str):
    try:
        response = requests.get(url)
        return response.json()
    except:
        error_message = f'Error: Something went wrong while extracting data with your api key @{datetime.datetime.now()}\n'
        log(error_message)


# You can change the url parameters to get different data or change the url all together.
raw_data = extract_data('https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2024&format=json&per_page=100')


if raw_data is None:
    print('An Error has occured, check the program.log file for more details')

elif isinstance(raw_data, list) or isinstance(raw_data, dict): # Public AIP call 
    log_message = f'Message: Data has been extracted successfuly from a public API on an API call @{datetime.datetime.now()}\n'
    log(log_message)
    with open('data/raw/raw_data.json', 'w', encoding='utf-8') as f:
        json.dump(raw_data, f, ensure_ascii=False, indent=4)
    log_message = f'Message: Data has been successfuly saved on the raw directory of the project @{datetime.datetime.now()}\n'
    log(log_message)




