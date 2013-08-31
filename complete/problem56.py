# Project Euler problem 56

from projecteuler import num_split, time_func

def sum_digits(num):
    nums = num_split(num)
    return sum(nums)

def main():
    max_digit_sum = 0 # maximum digital sum
    max_a, max_b = 0, 0
    for a in range(1, 100):
        for b in range(1, 100):
            num = sum_digits(a**b)
            if max_digit_sum < num:
                max_digit_sum = num
                max_a, max_b = a, b
    print max_digit_sum


if __name__ == '__main__':
    time_func(main)
