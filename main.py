from flask import Flask,  render_template

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
    app.run(debug=True)