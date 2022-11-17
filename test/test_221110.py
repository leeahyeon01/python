from random import *
pi = 3.14


def cone_volume(r, h):
    print(r, h)
    result = (pi*(r*r)*h)/3
    volume = int(result)
    print(volume)


x = randint(1, 100)
y = randint(1, 100)
cone_volume(x, y)
