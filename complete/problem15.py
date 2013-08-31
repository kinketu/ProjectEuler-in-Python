# Project Euler problem 15

from math import factorial
from projecteuler import time_func

def main():
    fct = factorial
    print fct(40)/(fct(20)*fct(20))


if __name__ == '__main__':
    time_func(main)
