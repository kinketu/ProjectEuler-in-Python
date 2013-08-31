# Project Euler problme 29

import time


def main():
    numbers = set()
    for i in range(2, 101):
        for j in range(2, 101):
            numbers.add(i**j)
            numbers.add(j**i)
    print len(numbers)

if __name__ == '__main__':
    start = time.clock()
    main()
    elapsed = time.clock() - start
    print elapsed, "sec"
