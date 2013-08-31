# Project Euler problem 9

from projecteuler import time_func

def main():
    for a in range(1, 1000/3):
        for b in range(1, 1000-a):
            c = 1000-a-b
            if a**2 + b**2 == c**2:
                print a * b * c
                break


if __name__ == '__main__':
    time_func(main)
