# Project Euler problem 16

from projecteuler import time_func

def main():
    num = 2 ** 1000

    print sum([int(x) for x in str(num)])


if __name__ == '__main__':
    time_func(main)
