# -*- coding: utf-8 -*-
__author__ = 'florije'
import re

a = "fuboqing"
b = "FUBOQING"
c = "fuBoqing"

print "fuboqing".upper().find('FUBOQING'), a
print b.upper().find('FUBOQING'), b
print "fuBoqing".upper().find('FUBOQING'), c

if re.search('fuBoqing', 'FUBOQING', re.IGNORECASE):
    print True
