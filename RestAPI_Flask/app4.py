from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['RestAPI_Flask']

app = Flask(__name__)

@app.route('/')
def home():
    # Get current day of the week
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%m:%S')
    # Pass it into the template
    return render_template('register.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)
    collection.insert_one(form_data)
    return 'Data submitted successfully'

@app.route('/view')
def view():

    data = collection.find()
    for item in data:
        print(data)
    return 'data'

if __name__ == "__main__":
    app.run(debug=True)

