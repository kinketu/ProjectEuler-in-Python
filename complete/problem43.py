# Project Euler problem 43
# cf. http://zacharydenton.com/project-euler-solutions/43/

from pyprimes import primes_below
from projecteuler import is_pandigital, time_func
from itertools import permutations


def check(number):
    """This function is judge whether number is pandigital or not.
    only 9 digits pandigital"""
    number = str(number)
    for i in range(7, 0, -1):
        print number[i:i+3], primes[i-1]
        if int(number[i:i+3]) % primes[i-1] == 0:
            #print number[i:i+3], pries[i-1]
            continue
        else:
            return False
    return True

def sub():
    primes = list(primes_below(17))

    print check(1406357289)

    below = 10 ** 9
    above = 10 ** 10
    for i in xrange(below, above):
        if check(i):
            print i

def gen_pandigitals(digit):
    """This function is very slow. expecially digit is over 5.
    If digit is 9, this function return Memmory Error."""
    pandigitals = []
    below = 10 ** (digit-1)
    above = 10 * below
    for i in range(below, above):
        if is_pandigital(i, s=digit):
            pandigitals.append(i)
    return pandigitals

def has_property(digits):
    primes = [1, 2, 3, 5, 7, 11, 13, 17]
    for i in range(1, len(digits)-2):
        if not int("".join(digits[i:i+3])) % primes[i] == 0:
            return False
    return True

def convert_list_to_int(lst):
    return int("".join(str(i) for i in lst))

def main():
    pandigitals = permutations((str(i) for i in range(10)))
    print sum(convert_list_to_int(p) for p in pandigitals \
              if has_property(p))
    

if __name__ == '__main__':
    time_func(main)

