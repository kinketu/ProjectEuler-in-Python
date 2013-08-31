# Project Euler problem 78
# cf. http://zacharydenton.com/project-euler-solutions/78/

from projecteuler import pentagonal, time_func
from itertools import count, cycle, takewhile, izip

def main1():
    """This approach is very slow."""
    divisor = 1000000
    index = 1
    while True:
        if partition(index) % divisor == 0:
            break
        else:
            index += 1
            print index
    print index

partitions = {}
generalized_pentagonals = sorted(map(pentagonal, range(-250, 250)))[1:]
def partition(n):
    if n <= 1: return 1
    if n not in partitions:
        signs = cycle([1, 1, -1, -1])
        pentagonals = takewhile(lambda p: p <= n, generalized_pentagonals)
        partitions[n] = sum(sign * partition(n - p) \
                            for sign, p in izip(signs, pentagonals))

    return partitions[n]

def main2():
    print (n for n in count(0) if partition(n) % 1000000 == 0).next()

if __name__ == '__main__':
    time_func(main2)
