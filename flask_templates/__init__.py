from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask_templates import views
from flask_templates import modules

socketApp = modules.socketio
