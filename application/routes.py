from flask import render_template
from application import app
from application.posts_repo import posts


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    header = "Paws For Thought"
    return render_template('home.html', header=header, posts=posts)
