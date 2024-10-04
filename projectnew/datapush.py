import psycopg2
import pandas as pd

# Function to connect to PostgreSQL
def connect_to_postgres():
    conn = psycopg2.connect(
        dbname="postgres",  # replace with your DB name
        user="postgres",  # replace with your DB user
        password="postgres",  # replace with your DB password
        host="localhost",
        port="5432"
    )
    return conn

# Load the dataset from the Excel file
df = pd.read_excel(r"C:\Users\patna\Downloads\Updated_Dataset_with_Converted_Date_Format.xlsx")  # Provide the correct file path

# Connect to PostgreSQL and insert data
def insert_data_to_postgres():
    conn = connect_to_postgres()
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lake_data (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            SD FLOAT,
            chlorophyll FLOAT,
            TP FLOAT,
            TNO2 FLOAT,
            eutrophication_index FLOAT,
            unix_time BIGINT,
            date DATE
        )
    ''')

    # Insert data into the table
    for _, row in df.iterrows():
        cursor.execute('''
            INSERT INTO lake_data (name, SD, chlorophyll, TP, TNO2, eutrophication_index, unix_time, date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (row['name'], row['SD'], row['chlorophyll'], row['TP'], row['TNO2'], row['eutrophication_index'], row['unix_time'], row['date']))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data inserted into PostgreSQL successfully!")

# Run the insertion function
insert_data_to_postgres()
