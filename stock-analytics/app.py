from flask import Flask, request
import csv
import sqlite3
from database.py import *

app = Flask(__name__)

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        conn = sqlite3.connect('my_database.db')
        c = conn.cursor()

        csv_reader = csv.reader(file.stream.read().decode('utf-8').splitlines())
        for row in csv_reader:
            # Assuming each row in the CSV file corresponds to a row in the table
            c.execute("INSERT INTO my_table VALUES (?, ?, ?)", row)

        conn.commit()
        conn.close()

        return 'File uploaded and database updated', 200

if __name__ == '__main__':
    app.run(debug=True)