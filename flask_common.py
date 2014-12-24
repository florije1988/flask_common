# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import Flask, jsonify
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


# @celery.task()
# def send_mail(message):
#     with app.app_context():
#         msg = Message(message,
#                       sender="945744127@qq.com",
#                       recipients=["945744127@qq.com"])
#         mail.send(msg)


# @celery.task(name="tasks.add")
# def add(x, y):
#     return x + y


@celery.task()
def add_together(a, b):
    return a + b


@celery.task
def add(x, y):
    return x + y


@app.route("/test")
def test():
    x = 16
    y = 16
    res = add.apply_async((x, y))
    context = {"id": res.task_id, "x": x, "y": y}
    result = "add((x){}, (y){})".format(context['x'], context['y'])
    goto = "{}".format(context['id'])
    return jsonify(result=add.AsyncResult(res.task_id).get(timeout=1.0), goto=goto)


@app.route('/')
def hello_world():
    # send_mail.apply_async(('Hello World!',))

    # msg = Message('Hello World!',
    # sender="945744127@qq.com",
    #               recipients=["945744127@qq.com"])
    # mail.send(msg)
    return 'Hello World!'


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    result = add.apply_async((4, 4),)
    print result.get()
