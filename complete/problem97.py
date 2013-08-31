# Project Euler problem 97
# cf. http://code.jasonbhill.com/c/project-euler-97/

from projecteuler import time_func

def main():
    n = 2
    for i in range(7830456):
        n = (2 * n) % 10000000000
    n *= 28433
    n += 1
    n = n % 10000000000
    print n


if __name__ == '__main__':
    time_func(main)
