# Project Euler problem 28

from projecteuler import time_func

# numbers = [[3, 3, 5, 7, 9], [5, 13, 17, 21, 25], ...]

def sequence(side_length):
    """Return a list of numbers
    cf. problem 28, 58"""
    index = side_length
    numbers = []
    tmp1 = (index -1 ) / 2
    #numbers.append([side length, 3, 5, 7, 9])
    for i in range(tmp1):
        if i == 0:
            numbers.append([3, 3, 5, 7, 9])
        else:
            diff = (3+i*2) - 1
            tmp2 = numbers[i-1][4] + diff
            numbers.append([3+i*2, tmp2, tmp2+diff, tmp2+diff*2, tmp2+diff*3])
    return numbers

def main():
    numbers = sequence(1001)
    #print numbers
    all_sum = 0
    for num in numbers:
        all_sum += sum(num[1:])
    print all_sum + 1


if __name__ == '__main__':
    time_func(main)
