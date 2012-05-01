#!/usr/bin/env python

# time the map classes and compare performance
# characteristics
# Sun Apr 29 15:23:23 PDT 2012
import os
import matplotlib.pyplot as pyplot

def etime():
    """See how much user and system time
    this process has used so far
    and return the sum"""
    user, sys, chuser, chsys, real = os.times()
    return user + sys


def dumb_func(size):
    some_list = []
    for i in range(0, size):
        some_list.append(i ** i)

    return some_list.sort(reverse=True)


def test_etime(func, number):
    start = etime()
    func(number)
    end = etime()
    elapsed = end - start
    return elapsed


def test_several_times(func, factor=10000):
    """Run the function several times 
    and count the elapsed time"""
    func = eval(func)
    times = []
    results = []
    for i in range(2, 25):
        number = factor * i
        results.append(number)
        elapsed = test_etime(func, number)
        times.append(elapsed)
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
        t = ratio**exp * tref
        tfit.append(t)

    return tfit

def graphit():
    funcs = ['dumb_func']
    exp = 1.0
    scale = 'log'
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('n')
    pyplot.ylabel('run time (n)')

    colors = ['darkslateblue']
    for functest, color in zip(funcs, colors):
        data = test_several_times(functest, 100)
        plot(*data, label=functest, color=color, exp=exp)

    pyplot.legend(loc=4)
    pyplot.show()

if __name__ == '__main__':
    #factor = 1000
    #results, times = test_several_times(dumb_func, factor)
    #for result, time in zip(results, times):
    #    print "%i: %i" % (result, time)
    graphit()
