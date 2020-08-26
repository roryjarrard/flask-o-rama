from app import app
from flask import render_template, request, redirect, jsonify, make_response
from datetime import datetime

users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creatof of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guido Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "technology entrepreneur, investor, and engineer",
        "twitter_handle": "@elonmusk"
    }
}


@app.route('/')
def index():
    return render_template('public/index.html')


@app.route('/about')
def about():
    return render_template('public/about.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        req = request.form

        missing = list()

        for k, v in req.items():
            if v == "":
                missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template('public/sign_up.html', feedback=feedback)

        return redirect(request.url)

    return render_template('public/sign_up.html')


@app.route('/profile/<username>')
def profile(username):
    user = None

    if username in users:
        user = users[username]

    return render_template('public/profile.html', username=username, user=user)


@app.route('/json', methods=['POST'])
def json_example():
    # validate the request body contains JSON
    if request.is_json:
        # parse the JSON into a Python dict
        req = request.get_json()

        response_body = {
            "message": "JSON received!",
            "sender": req.get("name")
        }

        res = make_response(jsonify(response_body), 200)

        return res
    else:
        return make_response(jsonify({'message': 'Request body must be JSON'}), 400)


@app.route('/jinja')
def jinja():
    # strings
    my_name = 'Rory'

    # integers
    my_age = 51

    # lists
    langs = ['Python', 'JavaScript', 'Bash', 'Ruby', 'C', 'Rust']

    # dictionaries
    friends = {
        'Tony': 43,
        'Cody': 28,
        'Amy': 26,
        'Clarissa': 23,
        'Wendell': 39
    }

    # tuples
    colors = ('Red', 'Blue')

    # boolean
    cool = True

    # functions
    def repeat(x, qty=1):
        return x * qty

    # classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name='Learning Flask',
        description='Learn the Flask web framework for Python',
        domain='https://github.com/roryjarrard/flask-o-rama'
    )

    date = datetime.utcnow()

    my_html = "<h1>This is some HTML</h1>"

    suspicious = "<script>alert('NEVER TRUST USER INPUT')</script>"

    return render_template(
        'public/jinja.html', my_name=my_name, my_age=my_age, langs=langs,
        friends=friends, colors=colors, cool=cool, GitRemote=GitRemote,
        my_remote=my_remote, repeat=repeat, date=date, my_html=my_html,
        suspicious=suspicious
    )


@app.template_filter('clean_date')
def clean_date(dt):
    return dt.strftime("%d %b %Y")
