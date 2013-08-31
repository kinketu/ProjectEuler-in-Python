# Project Euler problem 49

from projecteuler import is_perm, time_func
from pyprimes import isprime

def main():
    n = 1489
    while True:
        b, c = n + 3330, n + 3330 * 2
        if isprime(n) and isprime(b) and isprime(c) \
            and is_perm(n, b) and is_perm(b, c):
            break
        n += 2
    print str(n) + str(b) + str(c)

if __name__ == '__main__':
    time_func(main)
