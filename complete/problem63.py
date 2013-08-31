# Project Euler problem 63

from projecteuler import num_digits, time_func

def main():
    cnt = 0 # the number of n-digit integers whic are nth power
    for base in range(1, 10):
        for exp in range(1, 30):
            num = pow(base, exp)
            if num_digits(num) == exp:
                #print num
                cnt += 1
    print cnt


if __name__ == '__main__':
    time_func(main)
