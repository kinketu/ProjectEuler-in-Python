# Project Euler problem 1

from projecteuler import time_func


def main():
    print sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])

if __name__ == '__main__':
    time_func(main)
