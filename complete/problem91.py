# Project Euler problem 91
# cf. http://d.hatena.ne.jp/inamori/20100221/p1

from itertools import ifilter, product
from projecteuler import time_func

def sub1():
    """Original"""
    L = 2
    sum_triangle = L ** 2 + 2 * L **2
    print sum_triangle

    all_points = [[x, y] for x in range(0, L+1) for y in range(0, L+1)]
    print all_points

    points = list() # right angle points
    for x in xrange(0, L+1):
        for y in xrange(0, L+1):
            if x != 0 and y != 0:
                points.append([x, y])
    print points


def is_right_triangle(P, Q):
    if P[1] == 0 and Q[0] == 0:
        return True
    elif P[0] * (Q[0] - P[0]) == P[1] * (P[1] - Q[1]):
        return True
    elif Q[0] * (P[0] - Q[0]) == Q[1] * (Q[1] - P[1]):
        return True
    return False

def is_right_lower(P, Q):
    return P[0] * Q[1] - P[1] * Q[0] > 0

def main():
    L = 50
    counter = 0
    for P in product(range(L + 1), repeat = 2):
        for Q in product(range(L + 1), repeat = 2):
            if is_right_lower(P, Q) and is_right_triangle(P, Q):
                counter += 1
    print counter


if __name__ == '__main__':
    time_func(main)
