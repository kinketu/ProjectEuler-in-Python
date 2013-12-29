from itertools import *
from fractions import Fraction

def add(f, g):
    if len(f) < len(g):
        return add(g, f)
    else:
        return [ p + q for p, q in izip(f, chain(g, (0 for _ in count()))) ]

def mul(f, g):
    n = len(f) + len(g) - 1
    h = [ 0 ] * n
    for k in xrange(len(f)):
        for l in xrange(len(g)):
            h[k+l] += f[k] * g[l]
    return h

def value(f, x):
    return reduce(lambda p, q: p * x + q, reversed(f), 0)

def OP(k, u):
    def f(i):
        g = reduce(lambda x, j: mul(x, [ -xs[j], 1 ]),
                        (j for j in xrange(k) if j != i), [ 1 ])
        a = reduce(lambda x, j: x / (xs[i] - xs[j]),
                        (j for j in xrange(k) if j != i), Fraction(ys[i]))
        return mul(g, [ a ])
    
    xs = range(1, k + 1)
    ys = map(u, xs)
    return reduce(add, map(f, xrange(k)), [ 0 ])

def BOP(k, u):
    return value(OP(k, u), k + 1)

N = 10
u = lambda n: reduce(lambda x, y: 1 - x * n, xrange(N), 1)
print sum(BOP(k, u) for k in xrange(1, N + 1))
