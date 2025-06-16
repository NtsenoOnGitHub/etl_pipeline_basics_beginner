import requests
import kagglehub
import os
import datetime

api_key = os.getenv('API_KEY')

# Extract Data from Kaggle using kagglehun package 
# - file_path is the path that points to the data on kaggle (eg. )
# - file_name is the name of the csv file you intrested in. (eg. )
# - This will return a pandas dataframe 
def extract_kaggle_data(file_path: str, file_name: str):
    try:
        return kagglehub.load_dataset(kagglehub.KaggleDatasetAdapter.PANDAS, file_path ,file_name,)
    except:
        error_message = f'Something went wrong while extracting data from Kaggle. Double check the filepath and filename for typos {datetime.datetime.now()}\n'
        errorslogfilepath = 'logs/program_errors.log'

        if os.path.exists(errorslogfilepath):
            with open('logs/program_errors.log', "a") as file:
                file.write(error_message)
        else:
            file = open("logs/program_errors.log", "x")
            file.write(error_message)


# Extract data from openWeatherMap using API kEY
# - APIKEY is your secret api key from your openWeatherMap account
# - This will return a data in a json format
def extract_openWeatherMap_data(APIKEY: str):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=30.55&lon=22.93&appid={APIKEY}")
    return response.json()



