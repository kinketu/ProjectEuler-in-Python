# Project Euler problem 5

from fractions import gcd
from projecteuler import time_func

def lcm(numbers):
    """This function is to return the LCM.
    This function contains recurrence algorithm.
    So maybe slower the other algorithm."""
    if len(numbers) == 2:
        num0 = numbers[0]
        num1 = numbers[1]
        return num0 * num1 / gcd(num0, num1)
    else:
        for i in range(len(numbers)):
            return lcm([numbers[0], lcm(numbers[1:])])

def main():
    print lcm([x for x in range(1, 21)])

if __name__ == '__main__':
    time_func(main)
