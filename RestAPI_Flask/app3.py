from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('register.html')  # your HTML file

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        return "Passwords do not match!"
    return f"Welcome {name}, your email is {email}."

if __name__ == "__main__":
    app.run(debug=True)
