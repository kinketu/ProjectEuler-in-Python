# Project Euler problem 125
# cf. http://www.mathblog.dk/project-euler-125-square-sums-palindromic/

from math import sqrt
from projecteuler import is_palindrome, time_func

def main():
    end = 10 ** 8 # 10 ** 8
    sqrt_end = int(sqrt(end))

    sum_num = 0
    lst = list()

    for i in xrange(1, sqrt_end+1):
        num = i * i
        for j in xrange(i+1, sqrt_end+1):
            num += j * j
            if num > end:
                break
            if is_palindrome(str(num)) and num not in lst:
                sum_num += num
                lst.append(num)
    print sum_num


if __name__ == '__main__':
    time_func(main)
