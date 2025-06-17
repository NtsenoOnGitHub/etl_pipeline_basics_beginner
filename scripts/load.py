from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
import pandas as pd


connector = Connector()
INSTANCE_CONNECTION_NAME = "bold-bastion-462618-b7:us-central1:etl-pipeline-project"
DB_USER = "postgres"
DB_PASS = "@N.N100%sql"
DB_NAME = "etlpipelineDB"

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

for index, row in csv_data[0:2].iterrows():
    if index != len(csv_data[0:2]) - 1:
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