# -*- coding: utf-8 -*-
__author__ = 'florije'

from distutils.core import setup

setup(
    name='flask_common',
    version='0.0.1',
    packages=['my_app'],
    url='http://www.florije.com',
    license='florile.lic',
    author='florije',
    author_email='florije@gmail.com',
    description='this is the demo project',
    install_requires=[
        'Fabric==1.10.1',
        'Flask==0.10.1',
        'Flask-Mail==0.9.1',
        'Jinja2==2.7.3',
        'MarkupSafe==0.23',
        'Werkzeug==0.9.6',
        'amqp==1.4.6',
        'anyjson==0.3.3',
        'argparse==1.2.1',
        'billiard==3.3.0.19',
        'blinker==1.3',
        'celery==3.1.17',
        'ecdsa==0.11',
        'itsdangerous==0.24',
        'kombu==3.0.24',
        'paramiko==1.15.2',
        'pycrypto==2.6.1',
        'pytz==2014.10',
        'redis==2.10.3',
        'wsgiref==0.1.2',
    ],
)
