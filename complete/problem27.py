# Project Euler problem 27

from pyprimes import isprime, primes_below
from projecteuler import time_func

def main():
    listb = list(primes_below(1000))
    listb = listb[1:]

    max_cnt = 0
    max_a = 0
    max_b = 0
    for b in listb:
        #print b
        for a in [x for x in xrange(-b/40-40, 1000) if x % 2 != 0]:
            cnt = 0
            #print "(a, b)", (a, b)
            while isprime(cnt**2+a*cnt+b):
                cnt += 1
                #print cnt
            if max_cnt < cnt:
                max_cnt = cnt
                max_a = a
                max_b = b
    #print listb
    #print "max_cnt", max_cnt, "max_a", max_a, "max_b", max_b
    print max_a * max_b


if __name__ == '__main__':
    time_func(main)
