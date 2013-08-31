# Project Euler problem 76
# cf. http://blog.dreamshire.com/2009/03/31/project-euler-problem-76-solution/

from projecteuler import time_func, partition


def main():
    print partition(100) - 1

if __name__ == '__main__':
    time_func(main)
