# Project Euler problem 30

from projecteuler import time_func

def fifth_power(num):
    numbers = list(str(num))
    return sum([int(x)**5 for x in numbers])

def main():
    numbers = []
    for i in range(1, 360000):
        if i == fifth_power(i):
            numbers.append(i)
    numbers = numbers[1:]
    #print numbers

    print sum(numbers)
        

if __name__ == '__main__':
    time_func(main)
