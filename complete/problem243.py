# Project Euler problem 243
# cf. http://d.hatena.ne.jp/inamori/20090803/p1

from pyprimes import isprime, primes
from itertools import count
from fractions import Fraction
from projecteuler import time_func

def main():
    target = Fraction(15499, 94744)
    f = Fraction(1)
    d = 1
    for prime in primes():
        f *= Fraction(prime-1, prime)
        d *= prime
        if f < target:
            break
    n = int(f * d)
    for k in count(1):
        if Fraction(n * k, d * k -1) < target:
            break
    print k * d

if __name__ == '__main__':
    time_func(main)
