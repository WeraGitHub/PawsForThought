from flask import render_template
from application import app
from application.posts_repo import posts


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    header = "Paws For Thought"
    sub_header = "reflective blog"
    return render_template('home.html', header=header, subheader=sub_header, posts=posts)


@app.route('/about')
def about():
    header = "About"
    return render_template('about.html', header=header, subheader='')


@app.route('/contact')
def contact():
    header = "Contact"
    return render_template('contact.html', header=header, subheader='')
