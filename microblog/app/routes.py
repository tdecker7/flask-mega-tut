from app import app

@app.route('/')
def default():
    return "Default Page"
@app.route('/index')
def index():
    return "Hello, World!"