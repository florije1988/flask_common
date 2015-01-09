# -*- coding: utf-8 -*-
__author__ = 'florije'
from fabric.api import run


def host_type():
    run('uname -s')