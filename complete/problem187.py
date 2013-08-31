# Project Euler problem 187
# cf. https://code.google.com/p/tzaman/source/browse/euler/
# python/euler187.py?r=c15f7b9eb99e916c31e82527c0b29e1b1b29a43a

from pyprimes import primes_below
from projecteuler import time_func
from math import sqrt


def main1():
    end = 10 ** 5 # 10 ** 8
    primes = list(primes_below(end/2))
    semiprimes = set()
    cnt = 0
    for prime1 in primes:
        for prime2 in primes:
            product = prime1 * prime2
            if product < end and product not in semiprimes:
                semiprimes.add(product)
                cnt += 1
    print cnt

def countprimes(primes, limit):
    """unknown function"""
    pi, k, count = [0]*limit, 0, 0
    for i in xrange(2, limit):
        if k < len(primes) and primes[k] <= i:
            count += 1
            k += 1
        pi[i] = count
    return pi

def main2():
    lim = 10 ** 8 # 10 ** 8
    sqlim = int(sqrt(lim))
    primes = list(primes_below(lim/2 + 1))
    #print primes
    #print len(primes)
    pi = countprimes(primes, lim/2 + 1)
    #print pi
    #print len(pi)
    total = 0
    for k in xrange(1, pi[sqlim]+1):
        total += pi[int(lim/primes[k-1])] - k + 1
    print total

if __name__ == '__main__':
    time_func(main2)
