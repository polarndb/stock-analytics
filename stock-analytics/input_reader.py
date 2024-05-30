import csv
from database import write_to_database

def read_csv_file(file_path):
    records = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            records.append(row)
    write_to_database(records)