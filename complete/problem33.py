# Project Euler problem 33

from projecteuler import time_func
from fractions import gcd

def main():
    mul_a, mul_b = 1, 1
    for a in xrange(10, 100):
        if a % 10 == 0 or a % 11 == 0:
            continue
        str_a = str(a)

        for b in xrange(a + 1, 100):
            if b % 10 == 0 or b % 11 == 0:
                continue
            str_b = str(b)

            for char_a in str_a:
                x = int(char_a)
                list_a = [int(c) for c in str_a]
                list_b = [int(c) for c in str_b]
                if not x in list_b:
                    continue

                list_a.remove(x)
                list_b.remove(x)
                if len(list_a) != 1 or len(list_b) != 1:
                    continue

                if a * list_b[0] == b * list_a[0]:
                    mul_a *= a
                    mul_b *= b

    divider = gcd(mul_a, mul_b)
    print mul_b / divider


if __name__ == '__main__':
    time_func(main)
