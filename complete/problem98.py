from itertools import ifilter, combinations
from math import sqrt

def digits(n):
    if n == 0:
        return [ ]
    else:
        a = digits(n / 10)
        a.append(n % 10)
        return a

def numerize(a):
    return reduce(lambda x, y: x * 10 + y, a)

def is_square(n):
    m = int(sqrt(n))
    return m * m == n

def not_duplicated(a):
    b = [ False ] * 10
    for e in a:
        if b[e]:
            return False
        else:
            b[e] = True
    return True

def make_dic(a):
    def sort(s):
        return "".join(sorted(s[k] for k in range(len(s))))
    
    def add(a, s):
        if a in m:
            m[a].append(s)
        else:
            m[a] = [s]
    
    m = { }
    for s in a:
        add(sort(s), s)
    return m

def index(a, n):
    t = ()
    for k in range(len(a)):
        t = t + (k,)
    return t

def is_match(s, a):
    c = [ ' ' for n in range(10) ]
    for k in range(len(s)):
        if c[a[k]] == ' ':
            c[a[k]] = s[k]
        elif c[a[k]] != s[k]:
            return False
    
    for k in range(1, len(s)):
        for l in range(k):
            if s[k] == s[l] and a[k] != a[l]:
                return False
    
    return True

def match_square(pair):
    s1, s2 = pair
    convert = [ s2.index(c) for c in s1 ]
    l = len(s1)
    begin = int(sqrt(10**(l-1)))
    end = int(sqrt(10**l-1))
    for a in ifilter(lambda a: is_match(s1, a),
                (digits(k * k) for k in xrange(end, begin, -1))):
        n = numerize(map(lambda k: a[convert[k]], range(l)))
        if n >= 10 ** (l-1) and is_square(n):
            return max(n, numerize(a))
    return 0

file = open("problem98.txt")
a = map(lambda s: s[1:-1], file.read().split(','))
file.close()
b = filter(lambda s: len(s) > 1, make_dic(a).itervalues())
print reduce(max, (match_square(d) for c in b for d in combinations(c, 2)))
