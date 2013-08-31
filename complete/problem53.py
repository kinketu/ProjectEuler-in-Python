# Project Euler problem 53

from math import factorial
from projecteuler import time_func

def combination(n, r):
    ans = factorial(n) / (factorial(n-r) * factorial(r))
    return ans

def main():
    cnt = 0
    for n in range(1, 101):
        for r in range(n+1):
            if combination(n, r) > 1000000:
                cnt += 1
    print cnt


if __name__ == '__main__':
    time_func(main)
