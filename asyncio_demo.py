# -*- coding: utf-8 -*-
__author__ = 'florije'

from asyncio import coroutine, sleep
from flask import Flask, request

app = Flask(__name__)

@app.route("/hello/<string:name>")
@coroutine
def say_hi(name):
    pass
    # yield from sleep(2)
    # return "it worked %s" % request.args.get("name", name)

app.run()