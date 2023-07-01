
from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data to simulate registered users
registered_users = ["Alice", "Bob", "Charlie"]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in registered_users:
            message = f"Welcome back, {username}! You are already registered."
        else:
            message = f"Welcome, {username}! You are a first-time user."

        return render_template('result.html', message=message)

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

