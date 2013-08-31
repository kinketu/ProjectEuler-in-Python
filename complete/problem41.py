# Project Euler problem 41

from pyprimes import isprime
from projecteuler import time_func
from itertools import permutations

def pandigital(digit):
    """Return a list of pandigital numbers."""
    num = 0
    for i in range(digit):
        num += 10**i * (i+1)
    num = str(num)
    numbers = [int(x) for x in num]
    pers = list(permutations(numbers))
    lst = []
    for i in pers:
        tmp = ""
        for j in range(len(num)):
            tmp += str(i[j])
        lst.append(int(tmp))
    return lst

def main():
    pans = pandigital(7)
    #print pans
    max_prime = 0
    for pan in pans:
        #print pan
        if isprime(pan) and max_prime < pan:
            max_prime = pan
    print max_prime

if __name__ == '__main__':
    time_func(main)
