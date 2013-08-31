# Project Euler problem 40

from projecteuler import time_func

def int2irr_old(num):
    string = "0."
    for i in xrange(1, num+1):
        string += str(i)
    return string

def int2irr(num):
    """unknown function"""
    strings = ["0."]
    for i in xrange(1, num+1):
        strings.append(str(i))
    return "".join(strings)


def nth_decimal(num, index):
    return num[index+1]


def main():
    number = int2irr(1000000)
    product = 1
    for i in [10**x for x in range(7)]:
        product *= int(nth_decimal(number, i))
    print product

if __name__ == '__main__':
    time_func(main)
