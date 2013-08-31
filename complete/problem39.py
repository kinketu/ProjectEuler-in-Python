# Project Euler problem 39

import time
from projecteuler import time_func

def right_triangle(p):
    numbers = []
    for a in range(1, p/3):
        for b in range(a, p-a):
            c = p - a - b
            if a < b+c and b < c+a and c < a+b and a**2+b**2 == c**2:
                numbers.append([a, b, c])
    return numbers

def main():
    max_p = 0
    index_p = 0
    for p in range(1, 1001):
        p_len = len(right_triangle(p))
        if max_p < p_len:
            max_p = p_len
            index_p = p
    print index_p

if __name__ == '__main__':
    time_func(main)
