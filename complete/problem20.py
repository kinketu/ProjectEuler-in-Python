# Project Euler problem 20

from math import factorial
from projecteuler import time_func

def main():
    num = 100
    fact = factorial(num)

    print sum([int(x) for x in str(fact)])


if __name__ == '__main__':
    time_func(main)
