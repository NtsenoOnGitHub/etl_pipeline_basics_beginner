import pandas as pd
import requests
import kagglehub
import os
import datetime
from write_to_log import log

api_key = os.getenv('API_KEY')

# Extract Data from Kaggle using kagglehun package 
# - file_path is the path that points to the data on kaggle (eg. )
# - file_name is the name of the csv file you intrested in. (eg. )
# - This will return a pandas dataframe 
def extract_kaggle_data(file_path: str, file_name: str):
    try:
        return kagglehub.load_dataset(kagglehub.KaggleDatasetAdapter.PANDAS, file_path ,file_name,)
    except:
        error_message = f'Error: Something went wrong while extracting data from Kaggle. Double check the filepath and filename for typos @{datetime.datetime.now()}\n'
        log(error_message)

# Extract data from openWeatherMap using API kEY
# - APIKEY is your secret api key from your openWeatherMap account
# - This will return a data in a json format
def extract_openWeatherMap_data(APIKEY: str):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=30.55&lon=22.93&appid={APIKEY}")
    return response.json()


# Extract data from The World Bank using API call
# - APIKEY is your secret api key from your openWeatherMap account
# - This will return a data in a json format
def extract_worldBank_data(url: str):
    response = requests.get(url)
    return response.json()

# You can change the url parameters to get different data or change the url all together.
raw_data = extract_worldBank_data('https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2024&format=json&per_page=100')

if raw_data is None:
    print('An Error has occured, check the program.log file for more details')

elif isinstance(raw_data, pd.DataFrame): # Kaggle data
    log_message = f'Message: Data has been extracted successfuly from kaggle @{datetime.datetime.now()}\n'
    log(log_message)

    # Implement the rest of the logic to save the file into the raw data folder

elif isinstance(raw_data, list): # Public AIP call 
    log_message = f'Message: Data has been extracted successfuly from a public API on an API call @{datetime.datetime.now()}\n'
    log(log_message)
    entries = raw_data[1]  # data[0] is metadata, data[1] contains the records
    dataFrame = pd.DataFrame(entries) # Create DataFrame
    dataFrame = dataFrame[['country', 'date', 'value']] # Take colums you intrested in
    dataFrame["country"] = dataFrame["country"].apply(lambda x: x["value"]) # Clean up the messy columns
    dataFrame.to_csv('data/raw/raw_data.csv')




