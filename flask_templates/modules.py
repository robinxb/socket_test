# -*- coding: utf-8 -*-

from flask_templates import app
from flask.ext.socketio import SocketIO, emit
from flask import request
import requests
import copy

socketio = SocketIO(app)

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
           'Cache-Control': 'no-cache',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0',
           'Host': 'meican.com',
           'Origin': 'https://meican.com',
           'Upgrade-Insecure-Requests': 1
           }


@socketio.on('chat_push')
def on_chat_recieve(message):
    emit('chat_recieve', {'content': message['data']}, broadcast=True)

@app.route('/login_meican', methods=["POST"])
def login_meican():
    if request.method == 'POST':
        data = request.get_json()
        if not data["acc"] or not data["pwd"]:
            return ""
        payload = {'username': data["acc"], 'password': data['pwd'], 'remember':"true", 'loginType': 'username', "redirectUrl": ""}
        with requests.Session() as s:
            s.headers.update(headers)
            s.get('https://meican.com/login')
            r = s.post('https://meican.com/account/directlogin',data=payload)

            r2 = s.post("https://meican.com/preorder/api/v2.1/calendarItems/list",  cookies = s.cookies, data={
                "beginDate": "2015-9-30",
                "endDate": "2015-10-7"
            })
            print r2.text
        return ""
    else:
        return ""

