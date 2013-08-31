# Project Euler problem 12
# factors has some bugs. ex) >>>factors(90)
# factors2 has also some bugs. ex) >>>factors(90) return [2, 3, 3, 3, 5]
# cf. http://glowingpython.blogspot.jp/2011/07/
# prime-factor-decomposition-of-number.html
# problem 12 is not to calculate prime factors, but factors.

from math import floor, sqrt
from itertools import chain
from projecteuler import time_func, count_proper_divisors

def tri_number(index):
    sum = 0
    for i in range(1, index+1):
        sum += i
    return sum

def main():
    count_divisors = count_proper_divisors
    cnt = 0
    while True:
        tri = tri_number(cnt)
        if count_divisors(tri)+1 > 500:
            break
        cnt += 1

    print tri


if __name__ == '__main__':
    time_func(main)