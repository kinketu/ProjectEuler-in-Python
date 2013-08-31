# Project Euler problem 38
# cf.http://blog.dreamshire.com/2009/03/26/project-euler-problem-38-solution/

from projecteuler import is_pandigital, time_func

def main():
    for n in xrange(9876, 9123, -1):
        p = str(n*1) + str(n*2)
        if is_pandigital(p):
            print p
            break

if __name__ == '__main__':
    time_func(main)
