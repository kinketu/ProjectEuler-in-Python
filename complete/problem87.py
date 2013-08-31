# Project Euler problem 87
# cf. http://blog.dreamshire.com/
# 2011/07/16/project-euler-problem-87-solution/

from pyprimes import primes_below
from math import sqrt
from projecteuler import time_func

def sub(lst):
    return lst[0] ** 2 + lst[1] ** 3 + lst[2] ** 4

def main():
    limit = 50000000
    p2_limit = sqrt(limit-2**3-2**4)
    p3_limit = 369
    p4_limit = 84
    p2_list = list(primes_below(p2_limit))
    p3_list = list(primes_below(p3_limit))
    p4_list = list(primes_below(p4_limit))
    numbers = set()

    for p2 in p2_list:
        for p3 in p3_list:
            for p4 in p4_list:
                num = sub([p2, p3, p4])
                if num < limit:
                    numbers.add(num)

    print len(numbers)

if __name__ == '__main__':
    time_func(main)
