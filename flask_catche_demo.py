# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask, jsonify, request
from flask.ext.cache import Cache
from flask.ext.sqlalchemy import SQLAlchemy
from celery import Celery
import logging
from logging.handlers import TimedRotatingFileHandler

cache = Cache(config={
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'fcache',
    'CACHE_REDIS_HOST': 'localhost',
    'CACHE_REDIS_PORT': '6379',
    'CACHE_REDIS_URL': 'redis://localhost:6379'
})

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

cache.init_app(app)
db = SQLAlchemy(app)

handler = TimedRotatingFileHandler(filename='{0}'.format('logs.log'),
                                   when='D', interval=1, backupCount=5)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


def make_celery(app):
    celery = Celery('flask_celery_demo', broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(app)


@celery.task()
def add_log(msg):
    app.logger.warning(msg=msg)
    return msg


@app.route('/')
def hello_world():
    add_log.apply_async((request.host, ))
    users = User.query.all()
    return jsonify(result='success'), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')