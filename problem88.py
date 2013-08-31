from operator import mul
FACTORS = {}

def factorings(n,k=2):
  if n in FACTORS.keys():
    for f in FACTORS[n]:
      yield f
  else:
    result = []
    while k*k <= n:
      if n%k == 0:
        for f in factorings(n/k, k):
          result.append([k]+f)
          yield [k]+f
      k += 1
    FACTORS[n] = result + [[n]]
    yield [n]

def min_psn(n=2, k=2):
  ret = False

  while True:
    for f in factorings(n):

      if len(f) > k:
        continue

      s = sum(f) + (k-len(f))
      p = reduce(mul, f)

      if s==p:
        return n

    n += 1

s = set()
n = 2
for k in range(2,12001):
  n = min_psn(k,k)
  s.add(n)

print "Answer: %i" % sum(s)
