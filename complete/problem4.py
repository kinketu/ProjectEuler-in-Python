# Project Euler problem 4

from projecteuler import time_func, num_reverse


def main():
    max_value = 0
    products = []

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if product == num_reverse(product):
                products.append(product)
                

    products.sort()
    print products[len(products)-1]


if __name__ == '__main__':
    time_func(main)
