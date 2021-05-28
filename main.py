import numpy
import math


def pi(limit=1000000):
    c = 4
    n = c
    a = 1
    d = -1

    while abs(n) != numpy.pi and d < limit:
        n += a * (4/d)
        d += 2
        if a == 1:
            a = -1
        elif a == -1:
            a = 1
        else:
            print("ERROR")
            break
    n = n * -1
    print(f'{n}\n{numpy.pi}\n{math.pi}')
    return n

pi()
