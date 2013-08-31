# Project Euler problem 64
# cf. http://blog.dreamshire.com/2011/01/23/project-euler-problem-64-solution/

from math import sqrt
from projecteuler import time_func

def period_cntfrac_sqrt(num):
    """Return the period of the continued fraction of square root.
    >>>cntfrac_sqrt(2)
    >>>1
    >>>cntfrac_sqrt(23)
    >>>4
    >>>cntfrac_sqrt(4)
    >>>0"""
    r = limit = int(sqrt(num))
    if limit * limit == num:
        return 0
    k, period = 1, 0
    while k != 1 or period == 0:
        k = (num - r * r) / k
        r = ((limit + r) / k) * k - r
        period += 1
    return period

def main():
    cnt_odd_period = 0 # count odd period
    max_N = 10000 # 10000

    for N in range(2, max_N+1):
        if period_cntfrac_sqrt(N) % 2 == 1:
            cnt_odd_period += 1
    print cnt_odd_period

if __name__ == '__main__':
    time_func(main)
