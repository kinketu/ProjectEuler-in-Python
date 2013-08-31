# Project Euler problem 179
# cf. http://blog.dreamshire.com/
# 2012/04/10/project-euler-problem-179-solution/

from projecteuler import count_divisors, time_func

def main1():
    """bag exits
    end is 26 > cnt = 3"""
    end = 26 # 10 ** 7
    old = 1
    cnt = 0
    for i in range(2, end):
        new = count_divisors(i)
        if new == old:
            cnt += 1
        old = new
    print cnt

def main2():
    L = 10 ** 7 # 10 ** 7

    n = [0] * L
    for i in xrange(2, int(L/2)):
        for j in xrange(i*2, L, i):
            n[j] += 1

    cnt = 0
    for i in xrange(3, L):
        if n[i] == n[i-1]:
            cnt += 1
    print cnt
    

if __name__ == '__main__':
    time_func(main2)
