# Project Euler problem 71
# cf. http://ypsilonbox.blogspot.jp/2011/12/euler-problem-71.html

from fractions import Fraction, gcd
from projecteuler import time_func

def main1():
    """This approach is very slow."""
    max_d = 1000 # test is 8, problem is 10 ** 6
    fracs = list() # fractions
    for d in xrange(1, max_d+1):
        for n in xrange(1, d):
            if gcd(n, d) == 1:
                fracs.append(Fraction(n, d))
    fracs.sort()
    #print fracs
    index = fracs.index(Fraction(3, 7))
    print fracs[index-1]

def main2():
    # cf. http://www.mathblog.dk/
    # project-euler-71-proper-fractions-ascending-order/
    a = 3
    b = 7
    r = 0
    s = 1
    start = 10 ** 6
    for q in xrange(start, 2, -1):
        p = (a * q - 1 ) / b
        if p * s > r * q:
            s = q
            r = p
    print Fraction(r, s)

def main3():
    """Original"""
    target = 10 ** 6
    a, b = 2, 5
    c, d = 3, 7
    while True:
        if b < target:
            #print a, b
            a, b = a + c, b + d
        else:
            a, b = a - c, b - d
            break
    #print Fraction(a, b)
    print a

if __name__ == '__main__':
    time_func(main3)
