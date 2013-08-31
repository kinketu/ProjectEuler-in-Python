# Project Euler problem 120

from projecteuler import time_func

def main():
    sum_num = 0
    max_a = 1000
    for a in xrange(3, max_a+1):
        if a % 2 == 0:
            sum_num += a * (a - 2)
        else:
            sum_num += a * (a - 1)
    print sum_num


if __name__ == '__main__':
    time_func(main)
