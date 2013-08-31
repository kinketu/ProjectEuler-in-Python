# Project Euler problem 18
# cf. http://realultimateprogramming.blogspot.jp/2009
# /08/project-euler-problems-18-and-67.html

from projecteuler import time_func

numbers = [[75],
           [95, 64],
           [17, 47, 82],
           [18, 35, 87, 10],
           [20, 04, 82, 47, 65],
           [19, 01, 23, 75, 03, 34],
           [88, 02, 77, 73, 07, 63, 67],
           [99, 65, 04, 28, 06, 16, 70, 92],
           [41, 41, 26, 56, 83, 40, 80, 70, 33],
           [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
           [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
           [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
           [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
           [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
           [04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]

def reduce_triangle(to_reduce):
    """
    Reduce ``to_reduce`` in place by rolling up the maximum path info one row.

    >>> test = [[3,], \
            [7, 5], \
            [2, 4, 6], \
            [8, 5, 9, 3]]
    >>> test = reduce_triangle(test)
    >>> test
    [[3], [7, 5], [10, 13, 15]]
    >>> test = reduce_triangle(test)
    >>> test
    [[3], [20, 20]]
    >>> test = reduce_triangle(test)
    >>> test
    [[23]]
    """
    last_row = to_reduce[-1]
    for index in xrange(len(to_reduce)-1):
        to_reduce[-2][index] += max(last_row[index:index+2])
    del to_reduce[-1]
    return to_reduce

def main():
    global numbers
    while len(numbers) > 1:
        numbers = reduce_triangle(numbers)
        #print numbers
    print numbers[0][0]

if __name__ == '__main__':
    time_func(main)

