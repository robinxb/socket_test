""" Views redirecting to the appropriate HTML file content. (Flask Routes) """

from flask_templates import app
from flask.ext.socketio import SocketIO, emit

socketio = SocketIO(app)

@socketio.on('chat_push')
def on_chat_recieve(message):
    emit('chat_recieve', {'content': message['data']}, broadcast=True)
