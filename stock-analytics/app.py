from flask import Flask, request
#import csv
#import sqlite3
from database import *

app = Flask(__name__)

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        
        csv_to_database(file)
        return 'File uploaded and database updated', 200
    

if __name__ == '__main__':
    app.run(debug=True)