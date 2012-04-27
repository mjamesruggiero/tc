#!/usr/bin/python

# mruggiero
# Thu Apr  5 22:05:30 PDT 2012
# From Think Complexity chapter 2
# an infinite generator

import string

def inifinite_alpha():
    """docstring for inifinite_alpha"""
    i = 0
    while True:
        i +=1
        for c in string.lowercase:
            yield "%s%d" % (c, i)

if __name__ == '__main__':
    infinite_a = inifinite_alpha()
    for i in range(30):
        print infinite_a.next()

