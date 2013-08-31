# Project Euler problem 112
# cf. http://zacharydenton.com/project-euler-solutions/112/

from itertools import tee, izip
from projecteuler import time_func

def pairwise(iterable):
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def digits(n):
    return map(int, str(n))

def is_increasing(n):
    return all(prev <= curr for prev, curr in pairwise(digits(n)))

def is_decreasing(n):
    return all(prev >= curr for prev, curr in pairwise(digits(n)))

def is_bouncy(n):
    return not is_increasing(n) and not is_decreasing(n)

def test():
    num_bouncy = 0 # number of bouncy numbers
    for i in range(1, 1001):
        if is_bouncy(i):
            num_bouncy += 1
    print num_bouncy

def main():
    num_bouncy = 0 # number of bouncy numbers
    ratio = 0
    cnt = 1
    while True:
        if is_bouncy(cnt):
            num_bouncy += 1
        ratio = num_bouncy / float(cnt)
        #print cnt, ratio
        if ratio >= 0.99:
            break
        cnt += 1
    print cnt

if __name__ == '__main__':
    time_func(main)
