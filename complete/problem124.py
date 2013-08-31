# Project Euler problem 124

from pyprimes import factorise
from projecteuler import time_func

def rad(n):
    facts = list(factorise(n))
    facts = [x[0] for x in facts]
    product = 1
    for num in facts:
        product *= num
    return product

def main():
    rads = {}
    for i in xrange(1, 100001):
        rads[i] = rad(i)
    #print rads
    cnt = 0
    for k, v in sorted(rads.items(), key=lambda x: x[1]):
        cnt += 1
        if cnt == 10000:
            print k
        #print k, v

if __name__ == '__main__':
    time_func(main)
