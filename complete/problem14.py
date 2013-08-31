# Project Euler problem 14

from projecteuler import time_func

def next_collatz(num):
    if num % 2 == 0:
        num /= 2
    else:
        num = 3 * num + 1
    return num

def collatz_generator(start):
    while start != 1:
        yield start
        if start > 1:
            if start % 2 == 0:
                start = start / 2
            else:
                start = start * 3 + 1
    yield 1

def main1():
    max_chain = 0
    end = 1000 # 1000000
    for start in xrange(1, end):
        num = start
        cnt = 1
        while num != 1:
            #print num,
            num = next_collatz(num)
            cnt += 1
        if cnt > max_chain:
            max_chain = cnt
            max_start = start
        
        #print 1, "cnt:", cnt, "\n"
    print "max_chain", max_chain, "max_start", max_start


def main2():
    """This function is faster than main1"""
    max_chain = 0
    end = 1000000 # 1000000
    for start in xrange(1, end):
        num = start
        cnt = 0
        for num in collatz_generator(start):
            cnt += 1
        if cnt > max_chain:
            max_chain = cnt
            max_start = start
        
        #print 1, "cnt:", cnt, "\n"
    #print "max_chain", max_chain, "max_start", max_start
    print max_start


if __name__ == '__main__':
    time_func(main2)
