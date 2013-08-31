# Project Euler problem 77
# cf. http://blog.dreamshire.com/2009/06/08/project-euler-problem-77-solution/

from pyprimes import primes_below
from projecteuler import time_func


def main():
    primes = list(primes_below(80))
    target = 11 # how many ?
    while True:
        ways = [1] + [0] * target
        for i in primes:
            for j in range(i, target+1):
                ways[j] += ways[j-i]
        if ways[target] > 5000:
            break
        target += 1
    print target
    

if __name__ == '__main__':
    time_func(main)
