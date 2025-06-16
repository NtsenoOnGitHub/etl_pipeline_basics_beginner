## Project requiements
Goal: Collect data from a source, clean and transform it, then store it in a database.
Steps:
1.	Data Extraction
o	Pick a public dataset (e.g., weather data, stock market data, or even CSV files from Kaggle).
o	Use Python (with libraries like requests or pandas) to pull the data from an API or read a local file.
2.	Data Transformation
o	Clean the data: Handle missing values, remove duplicates, format timestamps.
o	Perform simple transformations: Aggregate values, create new columns based on existing data.
3.	Data Storage
o	Choose a storage option: SQLite (local), PostgreSQL (for practice with relational databases), or even a cloud storage option (like AWS S3).
o	Load the transformed data into the database with SQL or Python (sqlalchemy).
4.	Automation
o	Use Apache Airflow or cron jobs to automate the process.
o	Schedule the pipeline to run daily or hourly.
5.	Visualization (Optional)
•	Use matplotlib or Power BI to display key insights from your data.

## Project Learnings 
- Using the virtual enviroment to test and run my projects
- generating requirements.txt file
- learning how the .gitignore file work
- using git and git hub for version control
- implementing log file and tracking program erros
- learning about .env file for my api keys
- documenting my functions