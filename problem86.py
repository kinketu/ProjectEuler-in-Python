# Project Euler problem 86

from math import log, sqrt, exp
from decimal import Decimal


def is_int(num):
    if num == int(num):
        return True
    else:
        False

def sub1(perimeters):
    (a, b, c) = perimeters
    tmp1 = sqrt(a**2 + (b+c)**2)
    tmp2 = sqrt(b**2 + (c+a)**2)
    tmp3 = sqrt(c**2 + (a+b)**2)
    return min(tmp1, tmp2, tmp3)

def sub2(a, b, c):
    """Decimal type"""
    #perimeters = [a, b, c]
    #perimeters.sort()
    tmp1 = Decimal(a**2 + (b+c)**2).sqrt()
    tmp2 = Decimal(b**2 + (c+a)**2).sqrt()
    tmp3 = Decimal(c**2 + (a+b)**2).sqrt()
    return min(tmp1, tmp2, tmp3)

def main1():
    """Original
    There are some bags in the following."""
    cuboids = set()
    cnt = 0
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                tmp = sub1((i, j, k))
                if is_int(tmp) == True:
                    cnt += 1
    print cnt

def main2():
    """Original
    There are some bags in the following."""
    cuboids = set()
    cnt = 0
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                cuboids.add((i, j, k))
    #print cuboids
    for cuboid in cuboids:
        tmp = sub1(cuboid)
        if is_int(tmp) == True:
            cnt += 1
    print cnt

def main3():
    target = 1000000
    c = 0
    a = 2

    while c < target:
        a += 1
        for bc in range(3, 2*a):
            if bc * a % 12:
                continue
            s = sqrt(bc * bc + a * a)
            if s == int(s): # whether s is integer or not
                c += min(bc, a+1) - int((bc+1)/2)
    print a

if __name__ == '__main__':
    main3()
