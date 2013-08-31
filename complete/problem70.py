# Project Euler problem 70

from projecteuler import totient, is_perm, time_func
from pyprimes import primes, primes_below

def main1():
    """This aproach is very slow."""
    end = 10 ** 7
    lowerbound = 2000
    upperbound = 5000
    numbers = list() # totient(n) is a permutation of n
    for i in xrange(2, end):
        if is_perm(i, totient(i)):
            numbers.append(i)
    print len(numbers)

def create_semiprimes():
    end = 10 ** 7
    lowerbound = 2000
    upperbound = 5000
    prime_nums = [x for x in primes_below(upperbound) if x > lowerbound]
    semiprimes = set()
    for prime1 in prime_nums:
        for prime2 in prime_nums:
            semiprime = prime1 * prime2
            if semiprime < end:
                semiprimes.add(semiprime)
    return semiprimes

def main2():
    semiprimes = create_semiprimes()
    numbers = set() # totient(n) is a permutation of n
    min_value = 100
    min_n = 0
    for semiprime in semiprimes:
        if is_perm(semiprime, totient(semiprime)):
            numbers.add(semiprime)
            
    for num in numbers:
        tmp = num / float(totient(num))
        if tmp < min_value:
            min_value = tmp
            min_n = num
    print min_n
            


if __name__ == '__main__':
    time_func(main2)
