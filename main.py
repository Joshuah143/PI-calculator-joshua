import numpy
import math
import time
import twilio
pp = numpy.pi

def pi(limit=1000000):
    start = time.time()
    c = 4
    n = c
    a = 1
    d = -1

    while abs(n) != pp:
        n += a * (4/d)
        d += 2
        if d % 30000000 == 1:
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
    return n

pi()
