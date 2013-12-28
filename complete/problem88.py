from itertools import count, imap, ifilter, takewhile

def head(a):
    for e in a:
        return e

def gen_sum_product(begin, end, s = 0, p = 1, limit = 2):
    for n in xrange(limit, end):
        if s:
            yield s + n - 1, p * n
        for s1, p1 in gen_sum_product((begin - 1) / n + 1,
                        (end - 1) / n + 1, s + n - 1, p * n, n):
            yield s1, p1

def calc_k(N):
    def is_full():
        return all(a[k] != 0 for k in xrange(N, 1, -1))
    
    a = [ 0 ] * (N + 1)
    begin, end = 1, 2
    while not is_full():
        for s, n in gen_sum_product(begin, end):
            k = n - s
            if k <= N and (a[k] == 0 or a[k] > n):
                a[k] = n
        begin, end = end, end * 2
    
    return a

N = 12 * 10 ** 3
primes = [ 2 ]
print sum(set(calc_k(N)))
