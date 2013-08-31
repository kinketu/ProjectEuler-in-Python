# Project Euler problem 85
# cf. http://keyzero.wordpress.com/2010/05/14/project-euler-problem-85/

from projecteuler import time_func
from math import fabs

def sum_terms(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

def test():
    perimeter = 1
    while True:
        tmp = sum_terms(perimeter) ** 2
        if tmp > 2000000:
            break
        perimeter += 1
    print tmp, perimeter

def main():
    app = 2047761 # approximation
    for i in range(30, 101):
        for j in range(10, 101):
            tmp = sum_terms(i) * sum_terms(j)
            diff = 2000000 - tmp
            #print tmp, i, j, diff
            if fabs(diff) < fabs(2000000 - app):
                app = tmp
                app_i, app_j = i, j
    #print app, app_i, app_j, "answer", app_i * app_j
    print app_i * app_j

if __name__ == '__main__':
    time_func(main)
