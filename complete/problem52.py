# Project Euler problem 52

from projecteuler import num_split, time_func


def membership(old_nums, new_nums):
    if old_nums >= new_nums:
        return True
    else:
        return False

def main():
    num = 1
    while True:
        old_nums = set(num_split(num))
        products = [num*x for x in range(2, 7)]
        tmp = [membership(old_nums, set(num_split(x))) for x in products]
        #print num, tmp, products
        if False not in tmp:
            break
        num += 1

    #print num
    print num

if __name__ == '__main__':
    time_func(main)
