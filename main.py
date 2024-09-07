from flask import Flask, render_template, redirect, url_for, session, request
from waitress import serve

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a more secure key

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signin', methods=['POST'])
def signin():
    # Simulate user login logic
    session['logged_in'] = True
    return redirect(url_for('home'))

@app.route('/signout')
def signout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('home'))
    return render_template('dashboard.html')

@app.route('/history')
def history():
    if not session.get('logged_in'):
        return redirect(url_for('home'))
    return render_template('history.html')

@app.route('/send_money', methods=['GET', 'POST'])
def send_money():
    if not session.get('logged_in'):
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Handle money sending logic here
        recipient = request.form.get('recipient')
        amount = request.form.get('amount')
        # Add money sending logic here

        return redirect(url_for('dashboard'))

    return render_template('send_money.html')

@app.route('/receive_money', methods=['GET', 'POST'])
def receive_money():
    if not session.get('logged_in'):
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Handle money receiving logic here
        sender = request.form.get('sender')
        amount = request.form.get('amount')
        # Add money receiving logic here

        return redirect(url_for('dashboard'))

    return render_template('receive_money.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
