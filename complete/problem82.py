# Project Euler problem 82

# Code3
def gen_neighbor(pt0):
    x, y = pt0
    if x < N - 1:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < N - 1:
        yield x, y + 1

def gen_not_arrived_neighbor(pt0):
    for pt in filter(lambda pt: pt not in exist, gen_neighbor(pt0)):
        yield pt

def insert(queue, s):
    pt, n = s
    for k in xrange(len(queue) - 1, -1, -1):
        if n > queue[k][1]:
            queue.insert(k + 1, s)
            return
    queue.insert(0, s)

def gen_min_path(s):
    pt0, sum_path = s
    for pt in gen_not_arrived_neighbor(pt0):
        s = sum_path + a[pt[1]][pt[0]]
        insert(queue, (pt, s))
        exist.add(pt)
        yield pt, s

def solve():
    while True:
        for pt, min_path in gen_min_path(queue.pop(0)):
            if pt[0] == N - 1:
                return min_path

file = open("problem82.txt")
a = map(lambda s: map(int, s.split(',')), file.readlines())
file.close()
N = len(a)
exist = set([ (0, y) for y in range(N) ])
queue = [ ((0, y), a[y][0]) for y in range(N) ]
queue.sort(key = lambda t: t[1])
print solve()
