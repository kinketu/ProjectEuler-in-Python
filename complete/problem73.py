# Project Euler problem 73
# cf. http://blog.dreamshire.com/2011/01/20/project-euler-problem-73-solution/

from fractions import Fraction, gcd
from projecteuler import time_func

def main1():
    """Raise MemoryError"""
    max_d = 12000 # problem is 12000
    fracs = list() # fractions
    for d in xrange(1, max_d+1):
        for n in xrange(1, d):
            if gcd(n, d) == 1:
                fracs.append(Fraction(n, d))
    fracs.sort()
    min_index = fracs.index(Fraction(1, 3))
    max_index = fracs.index(Fraction(1, 2))
    #print min_index, max_index
    print max_index - min_index - 1

def main2():
    max_d = 12000
    cnt = 0
    for denominator in range(1, max_d+1):
        for numerator in range(denominator/3+1, (denominator-1)/2+1):
            if gcd(denominator, numerator) == 1:
                cnt += 1
    print cnt

if __name__ == '__main__':
    time_func(main2)
