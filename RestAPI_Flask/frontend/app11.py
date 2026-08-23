from flask import Flask, render_template
from datetime import datetime
import requests

BACKEND_URL = 'http://0.0.0.0:9000'


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
    requests.post(BACKEND_URL + '/submit', json=form_data)

    return 'Data submitted successfully'


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)

