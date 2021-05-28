import numpy
import math
import time
import twilio.rest as twil

sid = "ACee46d15aee42ece35152b01a0cf0db61"
tokensid = 'a16dc9df73edf829357d5354e5802147'
pp = numpy.pi


def send_text(message):
    twil.Client(sid, tokensid).messages.create(body=message, from_='+15873285525', to='+15874340118').sid


def pi(limit=100000000000000):
    start = time.time()
    c = 4
    n = c
    a = 1
    d = -1

    while abs(n) != pp and d < limit:
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
    return n, finish


print('sending message after completion with time')
send_text(str(pi()))
