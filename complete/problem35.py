# Project Euler problem 35

from pyprimes import isprime
from projecteuler import time_func

def circular(num):
    tmp = str(num) * 2
    length = len(str(num))
    numbers = []
    for i in range(length):
        tmp2 = ""
        for j in range(i, length+i):
            tmp2 += tmp[j]
        numbers.append(tmp2)
    return [int(x) for x in numbers]

def main():
    primes = [] # circular primes
    for i in xrange(1, 1000000):
        if False not in [isprime(x) for x in circular(i)]:
            primes.append(i)

    #print primes
    print len(primes)

if __name__ == '__main__':
    time_func(main)
