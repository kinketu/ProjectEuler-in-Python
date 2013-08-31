# Project Euler problem 75
# cf. http://blog.san-ss.com.ar/
# 2011/03/project-euler-problem-75-solved.html

from fractions import gcd
from itertools import count, takewhile
from projecteuler import time_func

def is_right_triangle(sides):
    sides.sort()
    if sides[2]**2 == sides[0] ** 2 + sides[1] ** 2:
        return True
    else:
        return False

def create_right_triangles():
    """There are some bags in this function."""
    triangles = set([]) # right triangles
    length = 12
    for a in range(1, length/3):
        #print a
        for b in range(1, length/2):
            #print a, b
            c = length - a - b
            if is_right_triangle([a, b, c]):
                triangles.add((a, b, c))
    return triangles
    #print a

def main():
    LIMIT = 1500000
    found_per = set()
    rep_per = set()
    generator = ((n, m) for n in count(3, 2) for m in range(1, n, 2) \
                 if gcd(m, n) == 1)
    for n, m in generator:
        a = m * n
        b = (n ** 2 - m ** 2) //2
        c = (n ** 2 + m ** 2) //2
        perimeter = a + b + c
        if m == 1 and perimeter > LIMIT:
            break
        for per in takewhile(lambda x: x <= LIMIT, \
                             (perimeter * i for i in count(1))):
            if per in found_per:
                rep_per.add(per)
            else:
                found_per.add(per)
    print len(found_per - rep_per)

if __name__ == '__main__':
    time_func(main)
