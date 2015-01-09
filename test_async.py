# -*- coding: utf-8 -*-
__author__ = 'florije'
import time
import requests

s = time.time()
print requests.get("http://127.0.0.1:5000").text
print time.time() - s