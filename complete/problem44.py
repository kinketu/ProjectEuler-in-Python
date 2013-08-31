# Project Euler problem 44

from math import fabs
from projecteuler import time_func

def main():
    p = set(n * ((3 * n) -1) / 2 for n in range(2, 4000))
    for i in p:
        for j in p:
            if i + j in p and j - i in p:
                x = i - j
            else:
                continue
    print int(fabs(x))


if __name__ == '__main__':
    time_func(main)
