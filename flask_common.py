# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask
from celery import Celery
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = '945744127'
app.config['MAIL_PASSWORD'] = 'td45957060'
app.config['MAIL_USE_TLS'] = True

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
mail = Mail(app)


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
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
def send_mail(message):
    with app.app_context():
        msg = Message(message,
                      sender="945744127@qq.com",
                      recipients=["945744127@qq.com"])
        mail.send(msg)


@app.route('/')
def hello_world():
    send_mail.apply_async(('Hello World!',))
    # msg = Message('Hello World!',
    #               sender="945744127@qq.com",
    #               recipients=["945744127@qq.com"])
    # mail.send(msg)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
