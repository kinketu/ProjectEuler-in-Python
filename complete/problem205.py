# Project Euler problem 205
# cf. http://blog.dreamshire.com/2012/12/26/project-euler-problem-205-solution/

from projecteuler import time_func


def main():
    #number of ways of rolling a total of n using 9 four-sided dice (pyramidal)
    p = [0, 0,  0,  1,   9,  45, 165, 486, 1206, 2598, 4950, 8451, \
         13051, 18351, 23607, 27876, 30276, 30276, 27876, 23607, \
         18351, 13051, 8451, 4950, 2598, 1206, 486, 165, 45, 9, 1]
    #number of ways of rolling a total of n using 6 six-sided dice (cubic)
    c = [1, 6, 21, 56, 126, 252, 456, 756, 1161, 1666, 2247, 2856, \
         3431, 3906, 4221, 4332, 4221, 3906, 3431, 2856, 2247, 1666, \
         1161, 756, 456, 252, 126, 56, 21, 6, 1]
 
    ways = 0
    total = (4**9) * (6**6.)
    for C in range(0, 31):
        for P in range (C+1, 31):
            ways += p[P]*c[C]
 
    print round(ways/total,7)

if __name__ == '__main__':
    time_func(main)
