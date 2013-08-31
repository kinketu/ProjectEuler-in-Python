# Project Euler problem 21

from projecteuler import time_func, sum_proper_divisors


def main():
    numbers = list() # amicable numbers
    for i in xrange(1, 10001):
        sum_prodiv = sum_proper_divisors(i) # sum of proper divisors
        if sum_proper_divisors(sum_prodiv) == i and sum_prodiv != i:
            numbers.append(i)

    print sum(numbers)

if __name__ == '__main__':
    time_func(main)
