#!/usr/bin/env python

# time the map classes and compare performance
# characteristics
# Sun Apr 29 15:23:23 PDT 2012
import os
import sys
import matplotlib.pyplot as pyplot
from bettermap import LinearMap, BetterMap, HashMap
import random
import string
import logging
from time import localtime


def etime():
    """See how much user and system time
    this process has used so far
    and return the sum"""
    user, sys, chuser, chsys, real = os.times()
    return user + sys


def test_map_class(map_class_name, size):
    """Using a random string, but I might
    get bitten by this. Maybe better to use an int?
    I just want to create more varied
    sorting concerns for the hash maps"""
    module = __import__('bettermap')
    class_ = getattr(module, map_class_name)
    object_ = class_()
    for i in range(0, size):
        key = random_string(8)
        object_.add(key, 1)
        ret = object_.get(key)


def test_etime(map_class_name, number):
    start = etime()
    test_map_class(map_class_name, number)
    end = etime()
    elapsed = end - start
    return elapsed


def random_string(n=4):
    choice = string.ascii_uppercase + string.digits
    return ''.join(random.choice(choice) for x in range(n))


def test_several_times(map_class_name, factor=10000):
    """Run the map_class_nametion several times
    and count the elapsed time"""
    times = []
    results = []
    string_size = 8
    for i in range(2, 25):
        number = factor * i
        elapsed = test_etime(map_class_name, number)
        times.append(elapsed)
        results.append(number)
    return results, times


def plot(ns, ts, label, color='blue', exp=1.0):
    tfit = fit(ns, ts, exp)
    pyplot.plot(ns, tfit, color='0.7', linewidth=2, linestyle='dashed')
    pyplot.plot(ns, ts, label=label, color=color, linewidth=3)


def fit(ns, ts, exp=1.0, index=-1):
    """Fits a curve with the given exponent.
    Use the given index as a reference point, and scale all other
    points accordingly.
    """
    nref = ns[index]
    tref = ts[index]

    tfit = []
    for n in ns:
        ratio = float(n) / nref
        t = ratio ** exp * tref
        tfit.append(t)

    return tfit


def save(root, exts=['pdf']):
    for ext in exts:
        filename = '%s.%s' % (root, ext)
        print 'Writing', filename
        pyplot.savefig(filename)


def graphit():
    exp = 1.0
    scale = 'log'

    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('n')
    pyplot.ylabel('run time (n)')

    classes = (('LinearMap', 1000,  'darkslateblue'),
               ('BetterMap', 10000, 'darkgreen'),
               ('HashMap',   10000, 'orangered'))

    for class_name, factor, color  in classes:
        data = test_several_times(class_name, factor)
        plot(*data, label=class_name, color=color, exp=exp)

    pyplot.legend(loc=4)
    stamp = '%4d-%02d-%02d-%02d-%02d-%02d' % localtime()[:6]
    filename = "timemaps-%s" % stamp
    save(filename)

if __name__ == '__main__':
    logging.basicConfig(
        #filename ="/tmp/python.log",
        format="%(levelname)-10s %(filename)s %(lineno)d %(message)s",
        level=logging.DEBUG
    )
    log = logging.getLogger(sys.argv[0])

    graphit()
