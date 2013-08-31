# Project Euler problem 24

from itertools import permutations as pers
from projecteuler import time_func

def main():
    ans = list(pers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[1000000-1]
    print reduce(lambda x, y: str(x) + str(y), ans)

if __name__ == '__main__':
    time_func(main)
