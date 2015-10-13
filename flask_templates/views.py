""" Views redirecting to the appropriate HTML file content. (Flask Routes) """

from flask_templates import app
from flask import render_template
from flask import g, request

@app.before_request
def before_request():
    pass
    #g.current_users = ["robin", "bob"]

@app.route('/index')
@app.route('/')
def index():
    """Main page of the website."""
    username = request.cookies.get('username')
    return render_template('index.html')
