#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：pfl time:2019/2/21

'''
Singleton
'''


class Singleton(object):
    ''''' A python style singleton '''

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls)
        return cls._instance


if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    s1 = SingleSpam('spam')
    print(id(s1), s1)
    s2 = SingleSpam('spa')
    print(id(s2), s2)
    print(id(s1), s1)
