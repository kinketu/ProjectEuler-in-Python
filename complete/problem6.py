# Project Euler problem 6

from projecteuler import time_func

def main1():
    sum1 = 0
    sum2 = 0
    for i in range(1, 101):
        sum1 += i*i
        sum2 += i

    sum2 = sum2**2

    #print sum1
    #print sum2
    print sum2 - sum1

def main2():
    sum1 = sum([i*i for i in range(1, 101)])
    sum2 = sum([i for i in range(1, 101)])
    sum2 = sum2 ** 2
    #print sum1
    #print sum2
    print sum2 - sum1


if __name__ == '__main__':
    time_func(main1)
