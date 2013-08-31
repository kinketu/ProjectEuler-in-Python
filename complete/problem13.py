# Project Euler problem 13

from projecteuler import time_func

def main():
    f = open('problem13.txt', 'r')
    lines = []
    for line in f:
        lines.append(line[0:50])
    f.close()


    lines = [int(line) for line in lines]

    print str(sum(lines))[:10]


if __name__ == '__main__':
    time_func(main)
