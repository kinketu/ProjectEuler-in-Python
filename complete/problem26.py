# Project Euler problem 26

from projecteuler import time_func

def cycle(n):
    """"Count recurring cycle."""
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5
    if n == 1:
        return 0
    count = 1
    while 10 ** count % n != 1:
        count += 1
    return count

def main():
    max_cycle = 0 # longest recurring cycle
    max_index = 0
    for i in xrange(1, 1000):
        count_cycle = cycle(i)
        if count_cycle > max_cycle:
            max_cycle = count_cycle
            max_index = i
    #print max_cycle
    print max_index


if __name__ == '__main__':
    time_func(main)
