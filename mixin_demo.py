# -*- coding: utf-8 -*-
__author__ = 'florije'

import types


def MixIn(pyClass, mixInClass, makeAncestor=0):
    if makeAncestor:
        pyClass.__bases__ = (mixInClass,) + pyClass.__bases__
    elif mixInClass not in pyClass.__bases__:
        pyClass.__bases__ = pyClass.__bases__ + (mixInClass,)
    else:
        pass


class C1(object):
    def test(self):
        print 'test in C1'


class C0MixIn(object):
    def test(self):
        print 'test in C0MixIn'


class C2(C1, C0MixIn):
    def test(self):
        print 'test in C2'


class C0(C1):
    pass


if __name__ == "__main__":
    print C0.__mro__
    c1 = C0()
    c1.test()
    MixIn(C0, C0MixIn, 1)
    c0 = C0()
    c0.test()
    print C0.__mro__

    print C2.__mro__
    MixIn(C2, C0MixIn)
    print C2.__mro__