from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')



from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mukesh:<mukesh>@cluster0.a1xlerz.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(MONGO_URI)

db = client.test
collection = db['RestAPI_Flask']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)




app = Flask(__name__)

@app.route('/')
def home():
    # Get current day of the week
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%m:%S')
    # Pass it into the template
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)
    collection.insert_one(form_data)
    return 'Data submitted successfully'

@app.route('/view')
def view():

    data = collection.find()
    print(data)
   
    return 'Data retrieved successfully'


if __name__ == "__main__":
    app.run(debug=True)

