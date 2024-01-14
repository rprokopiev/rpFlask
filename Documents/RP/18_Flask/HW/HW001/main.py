from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('basis.html')

@app.route('/main/')
def main():
    return render_template('basis.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/accessories/')
def accessories():
    return render_template('accessories.html')

@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')

if __name__ == '__main__':
    app.run(debug=True)