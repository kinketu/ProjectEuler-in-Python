# Project Euler problem 206
# cf. http://zacharydenton.com/project-euler-solutions/206/

from projecteuler import time_func

def is_concealed(n):
    digits = str(n)
    template = "1_2_3_4_5_6_7_8_9_0"

    if len(digits) != len(template):
        return False

    return all(digits[i] == template[i] for i in range(0, len(digits), 2))

def main():
    print (n for n in xrange(1000000000, 1390000000, 10)
           if (n % 100 == 30 or n % 100 == 70) and is_concealed(n*n)).next()


if __name__ == '__main__':
    time_func(main)
