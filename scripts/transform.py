import pandas as pd
import extract
import os
import datetime
from write_to_log import log

raw_data = extract.extract_kaggle_data('ishajangir/bollywood-movies', 'Data for repository.csv')

if raw_data is None:
    print('An Error has occured, check the program.log file for more details')
elif isinstance(raw_data, pd.DataFrame):
    log_message = f'Message: Data has been extracted successfuly from kaggle @{datetime.datetime.now()}\n'
    log(log_message)

    


