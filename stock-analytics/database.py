import sqlite3
import csv
import pandas as pd


def write_to_database(records):
    ##print('records written to db')
    ##for record in records:
    ##    print(record)
    # Connect to the SQLite database
    conn = sqlite3.connect('trade_events.db')
    c = conn.cursor()

    # Write records to the database
    for record in records:
        columns = ', '.join(record.keys())
        placeholders = ', '.join('?' * len(record))
        sql = f"INSERT INTO trade_raw_data ({columns}) VALUES ({placeholders})"
        c.execute(sql, tuple(record.values()))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def csv_to_database(file):
    file.seek(0)  # Ensure file pointer is at the beginning
    df = pd.read_csv(file)  # Read the file into a DataFrame
    print('df read from csv')
    print(df)
    records = df.to_dict('records')  # Convert the DataFrame to a list of dictionaries
    print('records read from csv')
    for record in records:
        print(record)
    write_to_database(records)  # Write the records to the database

def print_database_content():
    # Connect to the SQLite database
    conn = sqlite3.connect('trade_events.db')
    c = conn.cursor()

    # Execute a query to get all records from the stocks table
    c.execute('SELECT * FROM trade_raw_data')

    # Fetch all the records
    records = c.fetchall()

    # Print each record
    for record in records:
        print(record)

    # Close the connection
    conn.close()

def read_database_content():
    # Connect to the SQLite database
    conn = sqlite3.connect('trade_events.db')
    c = conn.cursor()

    # Execute a query to get all records from the stocks table
    c.execute('SELECT * FROM trade_raw_data')

    # Fetch all the records
    records = c.fetchall()

    # Convert all items in each record to strings
    records = [tuple(map(str, record)) for record in records]

    # Close the connection
    conn.close()

    return records