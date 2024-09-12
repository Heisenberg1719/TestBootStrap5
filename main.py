from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/login')
def loginPage():
   return render_template('login.html')

@app.route('/admin/dashboard')
def adminDash():
   return render_template('adminDash.html')

@app.route('/user/dashboard')
def userDash():
   return render_template('userDash.html')

if __name__ == '__main__':
    # Serve the app using Waitress on port 8080
    serve(app, host='0.0.0.0', port=8080)
