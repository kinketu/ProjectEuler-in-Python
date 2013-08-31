# Project Euler problem 55

from projecteuler import num_reverse, time_func

def sub1(num):
    """num = 349, return 349 + 943 = 1292"""
    return num + num_reverse(num)

def is_palindrome(string):
    """Check the string is palindrome""" 
    r_string = string[::-1]
    cnt = 0
    while cnt < len(string):
        if string[cnt] == r_string[cnt]:
            cnt += 1
            continue
        else:
            return False
        #cnt += 1
    return True

def sub2(num):
    """Check whether the number becomes palindromic number less than 50"""
    for i in range(50):
        num = sub1(num)
        if is_palindrome(str(num)):
            return True
    return False

def main():
    cnt = 0
    for i in range(1, 10000):
        if sub2(i) == False:
            cnt += 1
    print cnt
 

if __name__ == '__main__':
    time_func(main)
