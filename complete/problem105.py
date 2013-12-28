from itertools import chain, ifilter, imap
from operator import mul

def f(n):
    """factorial"""
    return reduce(mul, xrange(2, n+1), 1) 

def combination_count(n, k): 
    return f(n) / (f(n-k) * f(k))

def isubsum(seq, k): 
    """Generate all possible k-items sums in seq"""
    if k > 0: 
        for i in xrange( len( seq) - k + 1):
            for s in isubsum( seq[i+1:], k-1):            
                yield seq[i] + s
    else: yield 0

def isspecial(aset):                     
    # 2 > 1, 3 > 2, 4 > 3, ...  
    aset = sorted(aset)
    N = len(aset)
    for i in xrange(2, N - N/2 + 1): 
        if sum(aset[:i]) <= sum(aset[-i+1:]): 
            return False   
    # 1 != 1, 2 != 2, 3 != 3, ...
    C = combination_count
    for k in xrange(1, N/2 + 1): 
        if len(set(isubsum(aset, k))) != C(N, k):
            return False # there are equal sums exist           
    return True # given set is special

sets = (map(int, line.split(',')) for line in open('problem105.txt'))
print sum( imap( sum, ifilter( isspecial, sets)))
