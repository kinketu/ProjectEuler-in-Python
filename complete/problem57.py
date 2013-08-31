# Project Euler problem 57

from projecteuler import cntfrac2frac, cont_frac, num_digits, time_func
from math import sqrt


def method1(term):
    """Return the fraction of the term(sqrt(2))."""
    #limit = 8
    fracs = [1] + [2] * term
    #print fracs
    frac = cntfrac2frac(fracs)
    return frac

def main():
    cnt = 0
    for term in xrange(1, 1001):
        num = method1(term)
        #print num
        if num_digits(num.numerator) > num_digits(num.denominator):
            cnt += 1
    print cnt


if __name__ == '__main__':
    time_func(main)
