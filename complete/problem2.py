# Project Euler problem 2

from projecteuler import fib_matrix, time_func

def main():
    end = 4000000
    sum_fib = 0
    i = 0
    while True:
        fib = fib_matrix(i)
        if fib < end:
            #print "i:", i, fib
            if fib % 2 == 0:
                sum_fib += fib
            i += 1
        else:
            break
      
    print sum_fib


if __name__ == "__main__":
    time_func(main)
