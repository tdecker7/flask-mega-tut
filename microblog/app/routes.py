from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
def default():
    return "Default Page"
@app.route('/index')
def index():
    user = {'username': 'Trey'}
    posts = [
        {
            'author': { 'username': 'John Doe' },
            'body': 'This is my first blog post'
        },
        {
            'author': { 'username': 'Janie Doe' },
            'body': 'This is my second blog post'
        }
    ]
    return render_template(
        'index.html', 
        title='home', 
        user=user, 
        posts=posts
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')
    return render_template(
        'login.html',
        title="Login",
        form=form
    )