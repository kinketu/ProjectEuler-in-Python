# Project Euler problem 74
# very slow, over then 1000 sec

from math import factorial
from projecteuler import time_func

facts = [factorial(x) for x in range(10)]

def sum_digits_factorial1(num):
    """Return the sum of the factorial of its digits.
    ex)
    >>>sum_digits_factorial(145)
    >>>145
    """
    tmp = list(str(num))
    sum_fact = 0
    for i in tmp:
        sum_fact += factorial(int(i))
    return sum_fact

def sum_digits_factorial2(num):
    """Return the sum of the factorial of its digits.
    ex)
    >>>sum_digits_factorial(145)
    >>>145
    """
    tmp = list(str(num))
    sum_fact = 0
    for i in tmp:
        sum_fact += facts[int(i)]
    return sum_fact

def sub(num):
    numbers = set([num])
    while True:
        num = sum_digits_factorial2(num)
        #print num
        if num not in numbers:
            numbers.add(num)
        else:
            break
    return numbers
    
def main():
    cnt = 0
    for i in xrange(1, 1000000):
        #print i
        numbers = sub(i)
        if len(numbers) == 60:
            cnt += 1
    print cnt

if __name__ == '__main__':
    time_func(main)
