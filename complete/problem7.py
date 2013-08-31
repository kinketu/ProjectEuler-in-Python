# Project Euler problem 7

from pyprimes import nprimes
from projecteuler import time_func

def main():
    primes = list(nprimes(10001))
    print primes[10000]


if __name__ == '__main__':
    time_func(main)
