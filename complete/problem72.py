# Project Euler problem 72

from projecteuler import totient, time_func

def main():
    max_d = 10 ** 6
    print sum([totient(x) for x in range(1, max_d+1)]) - 1


if __name__ == '__main__':
    time_func(main)
