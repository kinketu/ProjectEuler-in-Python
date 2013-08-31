# Project Euler problem 79

from projecteuler import time_func

def sub(keys):
    first, second, third = set(), set(), set()
    for key in keys:
        if len(key) == 3:
            first.add(key[0])
            second.add(key[1])
            third.add(key[2])
        elif len(key) == 2:
            first.add(key[0])
            second.add(key[1])
        elif len(key) == 1:
            first.add(key[0])
        else:
            pass
    #head = ""
    for i in first:
        if i not in second and i not in third:
            head = i
    tmp = []
    for key in keys:
        if head in key:
            tmp.append(key[1:])
        else:
            tmp.append(key)
    keys = tmp
    return keys, head

def main():
    f = open('problem79.txt', 'r')
    keys = []
    for line in f:
        keys.append(line[:-1])
    f.close()
    #print keys

    answer = ""
    for i in range(8):
        keys, head = sub(keys)
        answer += head
    #print keys
    print answer

if __name__ == '__main__':
    time_func(main)
