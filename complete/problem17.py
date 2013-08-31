# Project Euler problem 17

from projecteuler import time_func

list1 = ["", "one", "two", "three", "four", "five", "six", "seven", \
         "eight", "nine", "ten", "eleven", "twelve", "thirteen",\
         "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",\
         "nineteen"]

list2 = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty",\
         "seventy", "eighty", "ninety"]

def count_under_twenty(num):
    return len(list1[num])

def count(num):
    snt = ""
    if num < 20:
        return len(list1[num]), list1[num]
    elif num >= 20 and num < 100:
        digit10 = num / 10
        digit1 = num % 10
        return len(list2[digit10]) + len(list1[digit1]),\
               list2[digit10] + " " + list1[digit1]
    elif num >= 100 and num < 1000:
        digit100 = num / 100
        digit10 = num / 10 % 10
        digit1 = num % 10
        if num % 100 == 0:
            return len(list1[digit100]) + len("hundred"),\
                   list1[digit100] + " " + "hundred"
        if num % 100 < 20:
            return len(list1[digit100]) + len("hundred")+ len("and")\
                   + len(list1[num%100]),\
                   list1[digit100] + " " + "hundred " + "and "\
                   + list1[num%100]

        else:
            return len(list1[digit100]) + len("hundred")+ len("and")\
                   + len(list2[digit10]) + len(list1[digit1]),\
                   list1[digit100] + " " + "hundred " + "and "\
                   + list2[digit10] + " " + list1[digit1]
    elif num == 1000:
        return len("one") + len("thousand"), "one thousand"


def main():
    sum = 0
    for num in range(1, 1001):
        sum += count(num)[0]
        #print num, ":", count(num)
    print sum

if __name__ == '__main__':
    time_func(main)

    
