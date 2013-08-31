# Project Euler problem 3

from projecteuler import time_func

def main():
    number = 600851475143
    i = 2
    while i * i < number:
        while number % i == 0:
            number = number / i
        i = i + 1

    print number


if __name__ == '__main__':
    time_func(main)
