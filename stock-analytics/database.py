import sqlite3


def write_to_database(records):
    # Connect to the SQLite database
    conn = sqlite3.connect('trade_events.db')
    c = conn.cursor()

    # Write records to the database
    for record in records:
        c.execute("INSERT INTO trade_raw_data VALUES (?,?,?,?,?,?)", record)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

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