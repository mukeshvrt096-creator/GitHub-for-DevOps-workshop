from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api', methods=['POST'])
def api():
    data=request.json
    return{"received":data}

if __name__ == "__main__":
    app.run(debug=True)
