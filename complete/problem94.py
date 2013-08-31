# Project Euler problem 94
# cf. http://d.hatena.ne.jp/Rion778/20100220/1266632427

from projecteuler import time_func

def main():
    max_perimeter = 10 ** 9
    x, y = 2, 1
    ans = 0

    while True:
        old_x = x
        old_y = y
        x = old_x * 2 + old_y * 3
        y = old_x + old_y * 2
        if x % 3 == 2:
            s = 2 * x - 2
        else:
            s = 2 * x + 2
        if s >= max_perimeter:
            break
        ans += s
    print ans


if __name__ == '__main__':
    time_func(main)
