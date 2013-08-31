# Project Euler problem 100
# cf. http://d.hatena.ne.jp/k_operafan/20120529/1338253334

from projecteuler import time_func

def main():
    x0, y0 = 3, 2
    x, y = 41, 29
    while True:
        x, y = x0 * x + 2 * y0 * y, x0 * y + y0 * x
        if x % 2 == 1 and y % 2 == 1:
            num_blue = (x + 1) / 2
            num_sum = (y + 1) / 2
            if num_blue > 10 ** 12:
                print num_sum
                break


if __name__ == '__main__':
    time_func(main)
