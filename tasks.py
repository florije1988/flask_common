# -*- coding: utf-8 -*-
__author__ = 'florije'
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    result = add.apply_async((4, 4),)
    print result.ready()
    print result.get()