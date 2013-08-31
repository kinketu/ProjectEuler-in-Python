# Project Euler problem 23

from projecteuler import proper_divisors, time_func


def sum_of_two(n, abd):
    for i in abd:
        if i > n / 2:
            break
        if cache[n-i]:
            return True
    return False

cache = [False] * 28124 # is abundant number

def main():
    global cache
    for i in xrange(1, 28124):
        if sum(proper_divisors(i)) > i:
            cache[i] = True
    abundants = [i for i in xrange(28124) if cache[i]]
    print sum([i for i in xrange(1, 28124) if not sum_of_two(i, abundants)])

if __name__ == '__main__':
    time_func(main)

