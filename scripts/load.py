from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
import pandas as pd
from dotenv import load_dotenv
import datetime
from write_to_log import log
import os


connector = Connector()
load_dotenv('config/.env')

INSTANCE_CONNECTION_NAME = os.getenv('INSTANCE_CONNECTION_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')

def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pg8000",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME,
        ip_type=IPTypes.PUBLIC
    )
    return conn

engine = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=getconn,
)

# Write Queries here
csv_data = pd.read_csv('data/processed/processed_data.csv')

query = "INSERT INTO Population (country, country_code, date, population) VALUES "
buildString = ''

for index, row in csv_data.iterrows():
    if index != len(csv_data) - 1:
        buildString = ''
        buildString += f'(\'{row["Country"]}\', \'{row["Country_code"]}\', \'{row["Date"]}\', {int(row["Population_Value"])}),'
        query += buildString
    else:
        buildString += f'(\'{row["Country"]}\', \'{row["Country_code"]}\', \'{row["Date"]}\', {int(row["Population_Value"])})'
        query += buildString

with engine.connect() as conn:
    insert_query = sqlalchemy.text(query)
    conn.execute(insert_query)
    conn.commit()

connector.close()

log_message = f'Message {datetime.datetime.now()}: Transfromed Data has been successfuly saved on the on a remote database on google cloud\n'
log(log_message)