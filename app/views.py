from app import app


@app.route('/')
def index():
    return "Hello Flask"


@app.route('/about')
def about():
    return 'All about Flask'
