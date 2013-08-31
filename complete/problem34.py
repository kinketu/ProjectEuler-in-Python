# Project Euler problem 34
# cf. http://www.s-anand.net/euler.html

from projecteuler import time_func

def sum_of_digits_factorial(num):
    fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
    sum_fct = 0
    while num > 0:
        digit = num % 10
        sum_fct += fact[digit]
        num /= 10
    return sum_fct

def main1():
    end = 10000000
    # the sum of all numbers which are equal
    # to the sum of the factorial of their digits.
    sum_num = 0
    for num in xrange(10, end):
        sum_fct = sum_of_digits_factorial(num)
        if sum_fct == num:
            sum_num += num
    print sum_num

def main2():
    print sum(n for n in xrange(10, 100000) if n == sum_of_digits_factorial(n))

if __name__ == '__main__':
    time_func(main2)
