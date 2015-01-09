# -*- coding: utf-8 -*-
__author__ = 'florije'
from flask import Flask, jsonify
import time
import gevent
from shelljob import proc
from gevent import monkey
monkey.patch_all()

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     time.sleep(20)
#     return 'Hello World!'

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/block')
def block():
    gevent.sleep(60)
    return 'Hello World!'


if __name__ == '__main__':
    # gunicorn -c async.conf async:app
    app.run(debug=True)
