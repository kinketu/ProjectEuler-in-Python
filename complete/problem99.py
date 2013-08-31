# Project Euler problem 99

from math import log
from projecteuler import time_func

def main():
    f = open('problem99.txt', 'r')
    lines = list()
    for line in f:
        lines.append(line[:-1].split(","))
    f.close()
    #print lines[0]
    max = 0
    for i in range(len(lines)):
        base = int(lines[i][0])
        exp = int(lines[i][1])
        tmp = exp * log(base)
        if tmp > max:
            max = tmp
            max_index = i
    print max_index+1


if __name__ == '__main__':
    time_func(main)
