# Project Euler problem 25

from projecteuler import time_func, fib_matrix


def main():
    i = 4500
    while True:
        if fib_matrix(i) < 10 ** 999:
            #print "i:", i, fib2(i)
            #print i
            i += 1
        else:
            break
    print i

if __name__ == '__main__':
    time_func(main)
