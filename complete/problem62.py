# Project Euler problem 62
# cf. http://alphacentauri32.wordpress.com/
# 2011/06/16/project-euler-problem-62-solved-with-python/

from itertools import permutations as pers
from projecteuler import num_digits, time_func

def create_cubes():
    """Create a set of cubes"""
    L = []
    for c in range(1, 20000):
        cube = pow(c, 3)
        L.append(cube)
    return set(L)

def main():
    """Main program"""
    cubes = create_cubes()
    for n in cubes:
        cube1 = str(n)
        cube1 = sorted(list(cube1))
        L = []
        for m in cubes:
            cube2 = str(m)
            cube2 = sorted(list(cube2))
            if cube2 == cube1:
                L.append(m)
        if len(L) == 5:
            L.sort()
            break
        else:
            continue
    print L[0]

        
if __name__ == '__main__':
    time_func(main)
