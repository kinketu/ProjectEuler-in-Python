# Project Euler problem 10

from pyprimes import primes_below
from projecteuler import time_func

def main():
    primes = list(primes_below(2*10**6))
    print sum(primes)


if __name__ == '__main__':
    time_func(main)
