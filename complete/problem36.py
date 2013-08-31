# Project Euler problem 36

from projecteuler import time_func

def test():
    if str(585)[::-1] == str(585):
        print 585
    b585 = bin(585)[2:]
    if b585[::-1] == b585:
        print b585

def main():
    # the sum of all numbers, which are palindromic in base 10 and 2
    sum_pal = 0 
    for i in xrange(1000000):
        binary = bin(i)[2:]
        if str(i)[::-1] == str(i) and binary == binary[::-1]:
            sum_pal += i
    print sum_pal

if __name__ == '__main__':
    time_func(main)
