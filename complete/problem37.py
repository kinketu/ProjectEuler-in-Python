# Project Euler problem 37

from pyprimes import isprime
from projecteuler import time_func
import time


def left_truncatable(n):
    """There are some bags in this function.
    ex) If n = 307, return a list = [307, 7, 7]"""
    numbers = []
    cnt = 1
    while True:
        if n % (10**cnt) != n:
            numbers.append(n%(10**cnt))
            cnt += 1
        else:
            numbers.append(n)
            break
    numbers.reverse()
    return numbers

def right_truncatable(n):
    """There are some bags in this function.
    ex) If n = 307, return a list = [307, 3, 3]"""
    list = left_truncatable(int(str(n)[::-1]))
    numbers = [int(str(x)[::-1]) for x in list]
    return numbers

def not_zero(n):
    if "0" not in str(n):
        return True
    else:
        return False

def main():
    primes = [] # Truncatable primes
    cnt = 1
    while True:
        if cnt < 800000:
            left = left_truncatable(cnt)
            right = right_truncatable(cnt)
            #zero = not_zero(cnt)
            if False not in [isprime(x) for x in left] \
                and False not in [isprime(x) for x in right] \
                and len(str(cnt)) > 0:
                primes.append(cnt)
            cnt += 1
        else:
            break
    primes = primes[4:]
    primes = [x for x in primes if not_zero(x) == True]
    #print primes
    #print len(primes)
    print sum(primes)


if __name__ == '__main__':
    time_func(main)