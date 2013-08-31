# Project Euler problem 31

from math import floor
from projecteuler import time_func


def main1(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [1] + [0]*target

    for coin in coins:
        for i in range(coin, target+1):
            ways[i] += ways[i-coin]

    print ways[target]

def main2():
    main1(200)

def change_pence1(n, k):
    """Calculate how many patterns to change pond and pence.
    There are sume bags in this function."""
    s = 0

    if n < 0:
        return 0
    s = 1 + n / 2 + change_pence1(n - 5, 5)
    if k >= 10:
        s += change_pence1(n - 10, 10)
    elif k >= 20:
        s += change_pence1(n - 20, 20)
    elif k >= 50:
        s += change_pence1(n - 50, 50)
    elif k >= 100:
        s += change_pence1(n - 100, 100)
    elif k >= 200:
        s += change_pence1(n - 200, 200)
    return s

def change_pence2(n):
    k = n
    s = change_pence1(n, k)
    return s  

def change_yen1(n, k):
    """Calculate now many patterns to change yen."""
    s = 0

    if n < 0:
        return 0
    s = 1 + n / 5 + change_yen1(n - 10, 10)
    if k >= 50:
        s += change_yen1(n - 50, 50)
    elif k >= 100:
        s += change_yen1(n - 100, 100)
    return s

def change_yen2(n):
    k = n
    s = change_yen1(n, k)
    return s

if __name__ == '__main__':
    time_func(main2)
