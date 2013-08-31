import time
from math import factorial, log10
from projecteuler import fib_recursive, fib_recursive_faster, time_func
from projecteuler import fib_matrix, fib_linear
from itertools import permutations as pers1
from projecteuler import permutations as pers2
from fibonacci import fibo

start = time.clock()

def main1(limit):
    sum = 0
    num = limit
    for a in range(num):
        for b in range(num):
            for c in range(num):
                sum += a + b + c
    return sum

def main2(limit):
    answer = sum([a+b+c for a in range(limit) for b in range(limit) \
         for c in range(limit)])
    return answer

def main3(limit):
    sum_digits = 0
    for i in range(1, limit+1):
        digits = len(str(i))
        sum_digits += digits
    print sum_digits

def main4(limit):
    sum_digits = 0
    for i in range(1, limit+1):
        digits = int(log10(i)+1)
        sum_digits += digits
    print sum_digits
    
def three_for_roop_test():
    """3 for roops and list comprehension
    """
    limit = 200
    
    start1 = time.clock()
    sum1 = main1(limit)
    elapsed1 = time.clock() - start1
    print sum1
    print elapsed1, "ms"

    start2 = time.clock()
    sum2 = main2(limit)
    elapsed2 = time.clock() - start2
    print sum2
    print elapsed2, "ms"

def test2():
    start3 = time.clock()
    factorial(10000)
    elapsed3 = time.clock() - start3
    print elapsed3, "ms"

def test3():
    limit = 10000
    start4 = time.clock()
    main3(limit)
    elapsed4 = time.clock() - start4
    print elapsed4, "ms"

    start5 = time.clock()
    main4(limit)
    elapsed5 = time.clock() - start5
    print elapsed5, "ms"

def fibonacci_test():
    """test of fibonacci generator functions"""
    term = 10000000
    print term

    def time_fib(function):
        start = time.clock()
        fib_num = function(term)
        elapsed = time.clock() - start
        #print fib_num
        print elapsed * 1000, "ms"

    # term < 40
    #print "method 1"
    #time_fib(fib_recursive)

    # term < 100000
    #print "method 2: fib_recursive_faster"
    #time_fib(fib_recursive_faster)

    # term < 10000 memory error
    #print "method 3: recursive fibonacci function with memorization"
    __fib_cache = {}
    def fib3(n):
        if n in __fib_cache:
            return __fib_cache[n]
        else:
            if n < 2:
                __fib_cache[n] = n
            else:
                __fib_cache[n] = fib3(n-2) + fib3(n-1)
            return __fib_cache[n]
    #time_fib(fib3)

    # term < 1000000
    #print "method 4: fibonacci module"
    #time_fib(fibo)

    # term < 10000000
    print "method 5: fib_matrix"
    time_fib(fib_matrix)

    # term < 1000000
    #print "method 6: fib_linear"
    #time_fib(fib_linear)
    
def permutation_test():
    """test of permutations functions"""
    numbers = [x for x in xrange(1, 9)]

    start1 = time.clock()
    list1 = list(pers1(numbers))
    elapsed1 = time.clock() - start1
    print elapsed1, "ms"

    start2 = time.clock()
    list2 = list(pers2(numbers))
    elapsed2 = time.clock() - start2
    print elapsed2, "ms"

def partition_test():
    from ProjectEuler import partition_slow, partition
    end = 60
    def test1():
        print "partition_slow"
        for i in range(0, end):
            print partition_slow(i)
    def test2():
        print "partition"
        for i in range(0, end):
            print partition(i)
    time_func(test1)
    time_func(test2)

def cntfrac_test():
    from cntfrac import CFraction
    from math import sqrt
    cf = CFraction(sqrt(2), maxterms=10)
    print cf
    for t in xrange(len(cf)):
        print cf.fraction(t)

def string_reverse_test():
    from projecteuler import str_reverse

    L = list()
    for i in range(100000):
        L.append(str(i))
    string = "".join(L)

    def test1():
        str_reverse(string)
    time_func(test1)

    def test2():
        string[::-1]
    time_func(test2)

    def str_reverse3(string):
        tmp = list(string)
        tmp.reverse()
        return "".join(tmp)
    def test3():
        str_reverse3(string)
    time_func(test3)

if __name__ == '__main__':
    string_reverse_test()
