# Project Euler problem 47

from projecteuler import time_func
from projecteuler import prime_factorization as factors


def sub1():
    a, b = set(), set()
    for i in range(3, 20):
        a = set(factors(i-1))
        b = set(factors(i))
        if len(a & b) == 0 and len(a) == 2 and len(b) == 2:
            print "answer", i-1, i

def sub2():
    a, b, c = set(), set(), set()
    for i in range(4, 700):
        a = set(factors(i-2))
        b = set(factors(i-1))
        c = set(factors(i))
        if len(a & b & c) == 0 and len(a) == 3 and len(b) == 3 and len(c) == 3:
            print "answer", i-2, i-1, i

def main():
    a, b, c, d = set(), set(), set(), set()
    for i in range(134000, 140000): # answer is 134043
        a = set(factors(i-3))
        b = set(factors(i-2))
        c = set(factors(i-1))
        d = set(factors(i))
        if len(a & b & c & d) == 0 and len(a) == 4 and len(b) == 4 \
           and len(c) == 4 and len(d) == 4:
            print i-3
            break

if __name__ == '__main__':
    time_func(main)
