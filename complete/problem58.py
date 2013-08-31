# Project Euler problem 58
# cf.http://blog.dreamshire.com/2009/04/11/project-euler-problem-58-solution/

from pyprimes import isprime
from projecteuler import time_func

def main():
    n_prime, d, prime_ratio, n = 0, 1, 1, 2

    while prime_ratio >= 0.10:
        n_prime += isprime(d + n) + isprime(d + n*2) + isprime(d + n*3)
        d += n * 4
        n += 2
        prime_ratio = float(n_prime) / (2 * n)

    print n-1


if __name__ == '__main__':
    time_func(main)
