# Project Euler problem 22

from projecteuler import time_func

def alpha_number(alpha):
    if alpha.isupper() == False:
        num = ord(alpha) - 96
        return num
    elif alpha.isupper() == True:
        num = ord(alpha) - 64
        return num

def main():
    f = open('problem22.txt', 'r')
    lines = []
    for line in f:
        lines.append(line[:-1])
    f.close()
    
    lines.sort()

    sum = 0
    score = 0
    for i in range(len(lines)):
        name = lines[i]
        for j in name:
            sum += alpha_number(j)
        score += (i+1) * sum
        sum = 0

    print score


if __name__ == '__main__':
    time_func(main)
