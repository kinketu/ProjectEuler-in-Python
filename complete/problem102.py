# Project Euler problem 102
# cf. http://www.mathblog.dk/project-euler-102-triangles-contain-origin/

from math import fabs
from projecteuler import time_func


def calc_area(a, b, c):
    return 1 / 2. * fabs((a[0] - c[0]) * (b[1] - a[1]) - \
                         (a[0] - b[0]) * (c[1] - a[1]))

def is_origin_inside(a, b, c, origin):
    if calc_area(a, b, c) == calc_area(a, b, origin) \
       + calc_area(a, origin, c) + calc_area(origin, b, c):
        return True
    else:
        return False

def create_coords():
    f = open('problem102.txt', 'r')
    lines = list()
    for line in f:
        lines.append(line[:-1])
    #print lines
    coords = list()
    for line in lines:
        coords.append([int(x) for x in line.split(",")])
    return coords

def main():
    coords = create_coords()
    origin = [0, 0]
    cnt = 0
    for coord in coords:
        a = coord[0:2]
        b = coord[2:4]
        c = coord[4:6]
        if is_origin_inside(a, b, c, origin):
            cnt += 1
    print cnt

if __name__ == '__main__':
    time_func(main)
