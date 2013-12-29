from Queue import PriorityQueue
import time

def gen_sorted(init, nexts):
    pq = PriorityQueue()
    pq.put(init)
    while not pq.empty():
        e = pq.get()
        yield e
        for e1 in nexts(e):
            pq.put(e1)

def make_pair(a, b):
    return ((a + b) * 0.5, (a, b), (0, a, b, a + b))

# (5, 7, 8, 9) -> 10
# (3, 6, 7) -> 8
def limit_addition(sss):
    if len(sss) % 2 == 0:
        return sum(sss[:len(sss)/2+1]) - sum(sss[len(sss)/2+1:]) - 1
    else:
        return sum(sss[:len(sss)/2+1]) - sum(sss[len(sss)/2+2:]) - 1

def merge(a, b):
    k, l = 0, 0
    p, q = a[0], b[0]
    while True:
        if p == q:
            return
        elif p < q:
            yield p
            k += 1
            if k == len(a):
                for l1 in xrange(l, len(b)):
                    yield b[l1]
                return
            p = a[k]
        else:
            yield q
            l += 1
            if l == len(b):
                for k1 in xrange(k, len(a)):
                    yield a[k1]
                return
            q = b[l]

def nexts((mean, sss, sums)):
    if len(sss) == 2:
        a, b = sss
        yield make_pair(a, b + 1)
        if a == b - 1:
            yield make_pair(a + 1, b + 1)
    
    for e in xrange(sss[-1] + 1, limit_addition(sss) + 1):
        sums_new = tuple(merge(sums, tuple(s + e for s in sums)))
        if len(sums_new) == len(sums) * 2:
            yield (float(sums_new[-1]) / (len(sss) + 1), sss + (e,), sums_new)

def gen_SSS():
    return gen_sorted(make_pair(1, 2), nexts)

t0 = time.clock()
N = 7
sss = next(sss for mean, sss, sums in gen_SSS() if len(sss) == N)
print "".join(map(str, sss))
print time.clock() - t0
