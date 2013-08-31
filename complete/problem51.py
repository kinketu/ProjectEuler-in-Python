# Project Euler problem 51
# cf. http://sozorogusa.blogspot.jp/2012/08/project-euler-problem-51.html

from pyprimes import primes_below
from projecteuler import time_func
 
def replace(n, L):
    """Return the value that was substitueted with the value
    of the number of digits specified position."""
    for i in xrange(10):
        t = ""
        for j, k in enumerate(str(n)):
            if j in L: t += str(i)
            else: t += k
        yield int(t)
 
def g(m, n):
    """Return the replacement candidate number and the position list."""
    d = {}
    for i, t in enumerate(str(m)):
        d[t] = d.get(t, []) + [i]
    for k,v in sorted(d.items()):
        if len(v) == n: yield int(k),v

def main1():
    #answer = 0
    for rep_digits in xrange(3, 100, 3):
        # rep_digits is the number of digits of the replacement characters
        for n in xrange(rep_digits+1, 100):
            # list of prime numbers of n digits
            primes = [s for s in list(primes_below(10**n)) if s>10**(n-1)]
            for prime in primes:
                for k, L in g(prime, rep_digits):
                    if k > 2:
                        break
                    if L[-1] >= n-1:
                        break
                    cnt_non_prime = 0 # counter of non-prime
                    for replaced_num in replace(prime, L):
                        if replaced_num not in primes:
                            cnt_non_prime += 1
                        if cnt_non_prime > 2:
                            break
                    if cnt_non_prime == 2:
                        return prime

def main2():
    print main1()

if __name__ == '__main__':
    time_func(main2)
