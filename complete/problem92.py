# Project Euler problem 92

from projecteuler import num_split, time_func

def square_chain(num):
    numbers = num_split(num)
    return sum([i ** 2 for i in numbers])

def square_chains(num):
    while True:
        if num == 1 or num == 89:
            break
        num = square_chain(num)
    return num

def gen_square_chains(num):
    while True:
        yield num
        num = square_chain(num)

def main1():
    cnt = 0
    end = 10000000
    test_end = 100000
    for index in xrange(1, test_end):
        #print index, square_chains(index)
        if square_chains(index) == 89:
            cnt += 1
    print cnt

def main2():
    """generator version
    This function is as slow as main1."""
    cnt = 0
    end = 10000000
    test_end = 100000
    for num in xrange(1, test_end):
        for chain in gen_square_chains(num):
            if chain == 89:
                cnt += 1
                break
            elif chain == 1:
                break
    print cnt


def test():
    a = gen_square_chains(44)
    for i in range(6):
        print a.next()
    b = gen_square_chains(85)
    for i in range(10):
        print b.next()
        
if __name__ == '__main__':
    time_func(main1)

