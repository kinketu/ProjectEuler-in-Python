# Project Euler problem 69
# cf. http://d.hatena.ne.jp/tanakaBox/20080516/1210893388

from pyprimes import primes_below
from projecteuler import time_func, totient

def main1():
    primes = list(primes_below(18))
    products = 1
    for prime in primes:
        if products < 1000000:
            products *= prime
        else:
            break
    print products

def main2():
    max_value = 0
    max_n = 0
    for n in xrange(1, 1000001):
        value = n / float(totient(n))
        if max_value < value:
            max_value = value
            max_n = n
    print max_n
        
        

if __name__ == '__main__':
    time_func(main1)
