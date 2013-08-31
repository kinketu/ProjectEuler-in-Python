# Project Euler problem 95

from projecteuler import sum_proper_divisors, is_perfect, time_func
from pyprimes import isprime
from pyprimes import primes_below as make_primes


def calc_period_old(num):
    """Return the period of amicable chain
    >>>calc_period(5)
    >>>0
    Todo: deficient number, abundant number"""
    if isprime(num):
        return 0
    chain = list()
    chain.append(num)
    while True:
        sum_prodiv = sum_proper_divisors(num) # sum of proper divisors
        if sum_prodiv not in chain:
            chain.append(sum_prodiv)
            num = sum_prodiv
        else:
            break
    return len(chain)

def calc_period(num):
    return len(create_sociable_numbers(num))

def is_amicable(n):
    if calc_period(n) == 2:
        return True
    else:
        return False

def create_sociable_numbers(num):
    """There are some bags in this function.
    >>>create_sociable_numbers(5)
    >>>[]"""
    if isprime(num):
        return list()
    chain = list()
    chain.append(num)
    while True:
        if isprime(num):
            return list()
        sum_prodiv = sum_proper_divisors(num) # sum of proper divisors
        if sum_prodiv not in chain:
            chain.append(sum_prodiv)
            #num = sum_prodiv
        else:
            break
        num = sum_prodiv
        if is_perfect(num):
            return list()
    return chain

# cf. http://d.hatena.ne.jp/inamori/20091113/p1
def calc_p_factor(n, p):
    m = 1
    while n % p == 0:
        m = 1 + m * p
        n /= p
    return m, n

def calc_sum_divs(max_n):
    a = range(max_n + 1)
    d = [ 1 ] * (max_n + 1)
    for p in primes:
        for k in xrange(p, max_n + 1, p):
            m, a[k] = calc_p_factor(a[k], p)
            d[k] *= m
    
    for k in xrange(2, max_n + 1):
        if a[k] != 1:
            d[k] *= (a[k] + 1)
        d[k] -= k
    
    return d

def print_social(n):
    a = [ n ]
    m = d[n]
    while m != n:
        a.append(m)
        m = d[m]
    print a

def find_social_number(n):
    s = set()
    m = n
    while m not in s:
        s.add(m)
        m = d[m]
        if m > N:
            return 0
    if m == n:
        a = list(s)
        a.sort()
        if a[0] == n:
            print_social(n)

def main():
    global d, N, primes
    N = 10 ** 6
    M = int(N ** 0.5 + 0.5)
    primes = make_primes(N)
    d = calc_sum_divs(N)
    for n in xrange(2, N + 1):
        find_social_number(n)  

if __name__ == '__main__':
    time_func(main)
