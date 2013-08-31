# Project Euler problem 50

from pyprimes import primes_below
from projecteuler import time_func


def method1(prime):
    primes = list(primes_below(prime))
    sum = 0
    max_cnt = 0
    for start_index in range(len(primes)):
        index = start_index
        cnt = 0
        while True:
            sum += primes[index]
            cnt += 1
            if sum == prime and max_cnt < cnt:
                max_cnt = cnt
                break
            elif sum >= prime:
                break
            index += 1
        sum = 0
    #print "prime", prime, "max_cnt", max_cnt
    return max_cnt

def main1():
    """Original solution"""
    primes = list(primes_below(1000))
    tmp = [0, 0] # tmp = [cnt, prime]
    for prime in primes:
        #print "-" * 50
        cnt = method1(prime)
        if tmp[0] < cnt:
            tmp = [cnt, prime]
    print tmp

def f(n):
    """Returns a list of prime numbers to be the longest
    when it is represented by the sum of the prime
    consecutive prime numbers less than or equal to n."""
    p = list(primes_below(n))
    i, s, t = 0, 0, 0
    while s < n:
        i, s = i+1, s+p[i]
    for j in xrange(i):
        if i-j < t:
            break
        for k in xrange(i-1, j, -1):
            if k-j < t:
                break
            l = p[j:k+1]
            if sum(l) in p:
                m, t = l, len(l)
    return m

def main2():
    l = f(1000000)
    print sum(l)
    """
    print "sum of " + str(len(l)) + " consecutive primes, " \
          + "from " + str(l[0]) + " to " + str(l[-1]) + "."
    """

if __name__ == '__main__':
    time_func(main2)
