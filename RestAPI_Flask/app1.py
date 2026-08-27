
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!....made 1st flask application"

@app.route('/second')
def second():
    return "Welcome to the homepage"

if __name__ == "__main__":
    app.run(debug=True)