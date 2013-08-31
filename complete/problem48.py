# Project Euler problem 48

from projecteuler import time_func

def main():
    sum_num = sum([i ** i for i in range(1, 1001)])
    print str(sum_num)[-10:]



if __name__ == '__main__':
    time_func(main)
