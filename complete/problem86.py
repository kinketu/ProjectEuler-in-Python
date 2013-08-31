# Project Euler problem 86

from math import sqrt
from projecteuler import time_func

def solution(M):
    solution = set()
    for A in range(1, M+1):
        for B in range(A, M+1):
            for C in range(B, M+1):
                if sqrt((A+B)**2+C**2)%1==0:
                    solution.add(tuple(sorted([A,B,C])))
    return len(solution)
  
    print "%i - %i"%(M, len(solution))

def main():
    M = 1800
    s = 986995

    while s < 1000000:
        M += 1
        s = solution(M)

    print M

if __name__ == '__main__':
    time_func(main)
