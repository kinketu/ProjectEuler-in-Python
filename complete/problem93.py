# Project Euler problem 93

from itertools import permutations, takewhile, \
                    product, izip, count, combinations
from projecteuler import time_func


def gen_number(a):
    if len(a) == 1:
        yield a[0]
    else:
        for k in range(1, len(a)):
            for m, n, op in product(gen_number(a[:k]),
                                    gen_number(a[k:]), operators):
                if n[0] != 0 or op != div:
                    yield op(m, n)

# x[0] and y[0] are numerator
def add(x, y): return (x[0] * y[1] + y[0] * x[1], x[1] * y[1])
def sub(x, y): return (x[0] * y[1] - y[0] * x[1], x[1] * y[1])
def mul(x, y): return (x[0] * y[0], x[1] * y[1])
def div(x, y):
    if y[0] < 0:
        y = (-y[0], -y[1])
    return (x[0] * y[1], x[1] * y[0])
operators = (add, sub, mul, div)

def last_of_consecutive_set(a):
    s = set(map(lambda f: f[0] / f[1],
            filter(lambda f: f[0] > 0 and f[0] % f[1] == 0,
                    (f for b in permutations(a) for f in gen_number(b)))))
    a = list(s)
    a.sort()
    return len(list(takewhile(lambda t: t[0] == t[1], izip(a, count(1)))))

def main():
    N = 4
    def longer(x, y): return x if x[1] >= y[1] else y
    a = reduce(longer, ((a, last_of_consecutive_set(a))
            for a in combinations(((n, 1) for n in range(1, 10)), N)))
    print reduce(lambda x, y: x * 10 + y[0], a[0], 0)


if __name__ == '__main__':
    time_func(main)
