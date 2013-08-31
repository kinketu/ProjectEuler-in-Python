# Project Euler problem 67

from projecteuler import reduce_triangle, time_func

def main():
    f = open('problem67.txt', 'r')
    triangle = []
    for line in f:
        line = line[:-1].split(",")
        line = [x.lstrip() for x in line]
        line = [int(x) for x in line]
        triangle.append(line)
    f.close()
    #print triangle

    
    while len(triangle) > 1:
        triangle = reduce_triangle(triangle)
    print triangle[0][0]

if __name__ == '__main__':
    time_func(main)
