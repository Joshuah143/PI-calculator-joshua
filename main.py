import numpy
import math
import time
import twilio.rest as twil
import sys

sid = "ACee46d15aee42ece35152b01a0cf0db61"
tokensid = 'a16dc9df73edf829357d5354e5802147'
pp = numpy.pi


def send_text(message):
    try:
        twil.Client(sid, tokensid).messages.create(body=message, from_='+15873285525', to='+15874340118').sid
    except Exception as e:
        print(f'FAILED TO SEND TEXT:\n{e}')


def pi(limit=100000000000000):
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
    print(i)


def pi3(n=10000000000000000000000000000000000000000000000000000):
    n = int(n)
    d = 360/n
    rd = (180-d)/2
    r = 1
    diamiter = 2
    e = (r * float(numpy.sin(d * numpy.pi / 180.)))/float(numpy.sin(rd* numpy.pi / 180.))
    circum = e * n
    pivalue = circum / diamiter
    return pivalue


def pi1time(timelimit=30):
    start = time.time()
    c = 4
    n = c
    a = 1
    d = -1
    while time.time() - start <= timelimit:
        n += a * (4 / d)
        d += 2
        if (d % 100000000 == 1) and False:
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
    print('p1:', finish)
    print(f'p1: {n}\nEx: {numpy.pi}')
    return n, finish


def pi2time(timelimit=30):
    start = time.time()
    num = 2
    den = 1
    final = 2.
    flip = 0
    i = 0
    while time.time() - start <= timelimit:
        i += 1
        if (i % 10000000 == 0) and False:
            print(f'working with: {str(final):.17}\t{i}')
            print(f'What we need: {pp}')
        final = final * (num / den)
        if flip % 2 == 0:
            den += 2
            flip = 1
        elif flip % 2 == 1:
            num += 2
            flip = 0
    finish = time.time() - start
    print('p2:', finish)
    print(f'p2: {final}\nEx: {numpy.pi}')


if __name__ == '__ma in__':
    test_time = 30
    pi1time(timelimit=test_time)
    pi2time(timelimit=test_time)

starttime = time.time()
calculated = float(pi3(n=10000000000000000000000000000000000000000000000000000))
fin = starttime - time.time()
print(f'{calculated:.30}')
print(f'{numpy.pi:.30}')
print(fin)
