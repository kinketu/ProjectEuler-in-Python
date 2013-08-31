# Project Euler problem 81
# cf. http://blog.dreamshire.com/
# 2009/04/16/project-euler-problem-81-solution/

from projecteuler import time_func

test_numbers1 = [[131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331]]

def reduce_matrix(matrix):
    num = len(matrix)
    for i in range(num):
        for j in range(num):
            pass

def sub1():
    test_numbers = [[131, 673], [201, 96]]
    test2 = test_numbers
    print test2
    test2[0][1] += test2[1][1]
    test2[1][0] += test2[1][1]
    del test2[1][1]
    print test2

    test2[0][0] += min(test2[0][1], test2[1][0])
    del test2[0][1], test2[1][0]
    print test2

def sub2():
    numbers = [[131, 673, 234], [201, 96, 342], [630, 803, 746]]
    print numbers
    numbers[2][1] += numbers[2][2]
    numbers[1][2] += numbers[2][2]
    del numbers[2][2]
    print numbers

    # Method 1
    i, j = 1, 1
    numbers[i][j] += min(numbers[i][j+1], numbers[i+1][j])
    numbers[i+1][j-1] += numbers[i+1][j]
    numbers[i-1][j+1] += numbers[i][j+1]
    del numbers[i+1][j], numbers[i][j+1]

    """
    # Method 2
    numbers[1][1] += max(numbers[1][2], numbers[2][1])
    numbers[2][0] += numbers[2][1]
    numbers[0][2] += numbers[1][2]
    del numbers[2][1]
    del numbers[1][2]
    """
    print numbers

    # Method 1
    i, j = 1, 0
    numbers[i][j] += min(numbers[i+1][j], numbers[i][j+1])
    numbers[j][i] += min(numbers[j][i+1], numbers[j+1][i])
    del numbers[j][i+1], numbers[i+1][j], numbers[i][j+1]

    # Method 2
    #numbers[1][0] += max(numbers[2][0], numbers[1][1])
    #numbers[0][1] += max(numbers[0][2], numbers[1][1])
    #del numbers[2][0]
    #del numbers[1][1]
    #del numbers[0][2]
    print numbers

def main():
    rows = [[int(n) for n in s.split(",")] \
            for s in open("problem81.txt").readlines()]
    nrows = len(rows) - 1

    for i in range(nrows, -1, -1):
        for j in range(nrows, -1, -1):
            if i == nrows and j == nrows:
                continue
            if j == nrows:
                minx = rows[i+1][j]
            elif i == nrows:
                minx = rows[i][j+1]
            else:
                minx = min(rows[i+1][j], rows[i][j+1])
            rows[i][j] += minx

    print rows[0][0]

if __name__ == '__main__':
    time_func(main)
