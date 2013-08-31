# Project Euler problem 59

from projecteuler import flatten, time_func

def file_input():
    f = open("problem59.txt", 'r')
    numbers = list()
    for i in f:
        numbers.append(i.split(","))
    numbers = flatten(numbers)
    numbers = [int(x) for x in numbers]
    return numbers

def count(numbers):
    counts = {}
    for i in range(100):
        counts[i] = numbers.count(i)
    return counts

def decode(keys, numbers):
    key1, key2, key3 = keys[0], keys[1], keys[2]
    plain_num = list()
    for i in xrange(len(numbers)):
        if i % 3 == 0:
            plain_num.append(numbers[i] ^ key1)
        elif i % 3 == 1:
            plain_num.append(numbers[i] ^ key2)
        else:
            plain_num.append(numbers[i] ^ key3)
    return plain_num

def main():
    numbers = file_input()
    counts = count(numbers)
    #keys = [71, 79, 68]
    keys = [103, 111, 100]
    plain_num = decode(keys, numbers)
    print sum(plain_num) # answer
    plain_text_list = [chr(x) for x in plain_num]
    plain_text = ""
    # replace join
    for x in plain_text_list:
        plain_text += x
    #print plain_text


if __name__ == '__main__':
    time_func(main)