import pandas as pd
import extract
import os
import datetime

raw_data = extract.extract_kaggle_data('ishajangir/bollywood-movies', 'Data for repository.csv')

if type(raw_data) == None:
    print('An Error has occured, check the program.log file for more details')
elif isinstance(raw_data, pd.DataFrame):
    log_message = f'Message: Data has been extracted successfuly from kaggle @{datetime.datetime.now()}'

    if os.path.exists('logs/program.log'):
        with open('logs/program.log', "a") as file:
            file.write(log_message)
    else:
        file = open("logs/program.log", "x")
        file.write(log_message)

