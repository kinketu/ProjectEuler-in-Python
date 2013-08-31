# Project Euler problem 32
# cf. http://d.hatena.ne.jp/phero/20100112/1263316982

from projecteuler import time_func

def add_if_fulfilled(a, b):
    global numbers
    c = a * b
    s = str(a) + str(b) + str(c)
    if len(s) == 9 and not '0' in s and len(set(s)) == 9:
        numbers.add(c)


numbers = set() # fulfilled numbers

def main():
    for a in xrange(1, 10):
        for b in xrange(1000, 10000):
            add_if_fulfilled(a, b)
    for a in xrange(10, 100):
        for b in xrange(100, 1000):
            add_if_fulfilled(a, b)
    print sum(numbers)


if __name__ == '__main__':
    time_func(main)
