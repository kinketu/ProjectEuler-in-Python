# Project Euler problem 46
# cf. http://alphacentauri32.wordpress.com/
# 2011/05/06/project-euler-problem-46-solved-with-python/

from pyprimes import primes_below, isprime
from projecteuler import time_func


def is_odd_composite(odd):
    if isprime(odd) == False:
        return True
    else:
        return False

def compute_conject(x, c):
    """Try the conjecture formula"""
    for n in range(1, 100):
        for ii in x:
            conject = ii + (2 * (n ** 2))
            if conject == c:
                return True
            else:
                continue
    return False

def main():
    limit = 10000
    primes = list(primes_below(10000))
    composites = [] # odd composites
    for odd in xrange(1, limit, 2):
        # make composites up to limit
        if is_odd_composite(odd):
            composites.append(odd)
        else:
            continue
    for c in composites:
        if c > 33:
        # We already know up through 33
            x2 = compute_conject(primes, c)
            if x2 == False:
                """print the first odd composite that cannot
                be written as the sum of a prime and twice the square"""
                print c
                break
            else:
                continue
        else:
            continue

def test():
    for odd in xrange(1, 100, 2):
        if is_odd_composite(odd):
            print odd, "is composite number"
        else:
            print odd, "is prime"

if __name__ == '__main__':
    time_func(main)
