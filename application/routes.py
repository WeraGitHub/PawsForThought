from flask import render_template
from application import app


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    title_name = "Paws For Thought"
    return render_template('home.html', title=title_name)
