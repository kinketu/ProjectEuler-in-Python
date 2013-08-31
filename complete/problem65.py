# Project Euler problem 65

from math import sqrt, floor
from fractions import Fraction
from math import e
from projecteuler import num_split, time_func

def cont_frac(num, index):
    """There are some bags in this function because of truncation error.

    example:
    >>>cont_frac(sqrt(2), 100)
    >[1, 2, 2, ..., 1, 1, ..., 1809, ...]
    """
    b = []
    b.append(int(num))
    for i in xrange(1, index):
        num = 1 / (num - b[i-1])
        #print num
        b.append(int(num))
    return b

def cntfrac2float(fractions):
    """Calculate continued fraction and return a float type number."""
    f = 0
    n = len(fractions)-1
    while n > 0:
        f = 1.0 / (fractions[n] + f)
        print f
        n -= 1
    return f + fractions[0]

def cntfrac2frac(fractions):
    """Calculate continued fraction and return a fraction."""
    fractions = [Fraction(i) for i in fractions]
    f = Fraction(0)
    n = len(fractions)-1
    while n > 0:
        f = Fraction(Fraction(1) / (fractions[n] + f))
        #print f
        #print type(f)
        n -= 1
    return Fraction(f + fractions[0])

def main():
    lst = []
    for i in range(100):
        if i % 3 == 2:
            lst.append((i/3+1)*2)
        else:
            lst.append(1)
    lst[0] = 2
    #print lst
    numerator = cntfrac2frac(lst).numerator
    numbers = num_split(numerator)

    print sum(numbers)

if __name__ == '__main__':
    time_func(main)
    
