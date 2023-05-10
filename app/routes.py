from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, PatrykFicek!"

@app.route('/name/', defaults = {'name': "Anon"})
@app.route('/name/<name>')
def name(name):
    return f"Hello, {name}"