# Project Euler problem 11

from projecteuler import time_func

def create_matrix():
    f = open('problem11.txt', 'r')
    lines = list()
    for line in f:
        lines.append(line[:-1:])
    f.close()
    mat2 = list()
    for line in lines:
        mat2.append(line.split(","))
    #print mat2
    mat3 = list()
    for line in mat2:
        line = [int(x.strip()) for x in line]
        mat3.append(line)
    return mat3
        
def main():
    mat = create_matrix()

    max_product = 0

    # Left and Right
    for i in range(20):
        for j in range(20-3):
            product = mat[i][j]*mat[i][j+1]*mat[i][j+2]*mat[i][j+3]
            if max_product < product:
                max_product = product

    # Upper and Lower
    for i in range(20-3):
        for j in range(20):
            product = mat[i][j]*mat[i+1][j]*mat[i+2][j]*mat[i+3][j]
            if max_product < product:
                max_product = product

    # Upper Right
    for i in range(19, 2, -1):
        for j in range(20-3):
            product = mat[i][j]*mat[i-1][j+1]*mat[i-2][j+2]*mat[i-3][j+3]
            if max_product < product:
                max_product = product

    # Upper Left
    for i in range(20-3):
        for j in range(20-3):
            product = mat[i][j]*mat[i+1][j+1]*mat[i+2][j+2]*mat[i+3][j+3]
            if max_product < product:
                max_product = product

    print max_product

if __name__ == '__main__':
    time_func(main)
