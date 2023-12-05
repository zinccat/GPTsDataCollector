from flask import Flask, request
import csv
import os

app = Flask(__name__)

# add index page
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/save', methods=['POST'])
def save_request():
    data = request.json

    # Save to CSV
    file_exists = os.path.isfile('requests.csv')
    with open('requests.csv', 'a', newline='') as csvfile:
        fieldnames = data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Write header only once

        writer.writerow(data)

    return {"message": "Data saved successfully"}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80) #, ssl_context=('../cert.pem', '../key.pem'))
