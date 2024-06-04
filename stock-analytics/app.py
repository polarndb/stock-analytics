from flask import Flask, request, Response
#import csv
#import sqlite3
from database import *


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'csv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file and allowed_file(file.filename):
        print(f'File object:\n{file}')  # Debug print
        file.seek(0, 2)
        print(f'File size: {file.tell()} bytes')
        csv_to_database(file)
        return 'File uploaded and database updated', 200
    
@app.route('/download-csv', methods=['GET'])
def download_csv():
    
    data = read_database_content()

    # Convert data to CSV
    csv_data = '\n'.join([','.join(map(str, row)) for row in data])

    # Create a generator for the data
    def generate():
        yield csv_data

    # Return the data as a file
    return Response(generate(), mimetype='text/csv', headers={'Content-Disposition': 'attachment; filename=data.csv'})


if __name__ == '__main__':
    app.run(debug=True)