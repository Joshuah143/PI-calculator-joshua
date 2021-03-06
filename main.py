import numpy
import math
import time
import twilio.rest as twil


pp = numpy.pi


def pi(limit=100000000000000):
    # very long, infinite
    start = time.time()
    c = 4
    n = c
    a = 1
    d = -1
    while abs(n) != pp and d < limit:
        n += a * (4/d)
        d += 2
        if d % 100000000 == 1:
            t = f'{abs(n):.15f}'
            print(f'working with: {t}\t{d}')
            print(f'What we need: {pp}')
        if a == 1:
            a = -1
        elif a == -1:
            a = 1
        else:
            print("ERROR")
            break
    n = n * -1
    finish = time.time() - start
    print(finish)
    print(f'{n}\n{numpy.pi}\n{math.pi}')
    return n, finish


def pi2(limit=10000000):
    # very long, infintit
    num = 2
    den = 1
    final = 2.
    flip = 0
    i = 0
    while (final != numpy.pi) and (i <= limit):
        i += 1
        if i % 10000000 == 0:
            print(f'working with: {str(final):.17}\t{i}')
            print(f'What we need: {pp}')
        final = final * (num/den)
        if flip % 2 == 0:
            den += 2
            flip = 1
        elif flip % 2 == 1:
            num += 2
            flip = 0
    return i


def pi3(n=65001314):
    # very short, finite
    n = int(n)
    d = 360/n
    rd = (180-d)/2
    r = 1
    diamiter = 2
    e = (r * float(numpy.sin(d * numpy.pi / 180.)))/(float(numpy.sin(rd * numpy.pi / 180.)))
    circum = e * n
    pivalue = circum / diamiter
    return pivalue


def pi4(increment=0.00005):
    # finite, inacurate, no pi, pure python
    ycalc = lambda a: ((1 - (a ** 2)) ** 0.5)
    pythag = lambda y, yn, x, xn: (abs((((abs(yn - y)) ** 2) + ((abs(xn - x)) ** 2)) ** 0.5))
    increment = float(increment)
    xvalue = increment
    lastxvalue = 0
    total_length = 0
    while xvalue <= 1:
        total_length += pythag(ycalc(lastxvalue), ycalc(xvalue), lastxvalue, xvalue)
        lastxvalue = xvalue
        xvalue += increment
    total_length = total_length * 4
    pi_value = total_length/2
    return pi_value

