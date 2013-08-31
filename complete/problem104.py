# Project Euler problem 104
# cf. http://blog.dreamshire.com/2009/06/04/project-euler-problem-104-solution/

from projecteuler import is_pandigital, time_func


def test():
    a = fibo(541)
    a = str(a)
    print is_pandigital(a[-9:])
    print a[-9:]
    b = fibo(2749)
    b = str(b)
    print is_pandigital(b[:9])
    print b[:10]

def main1():
    """very slow"""
    cnt = 329300
    while True:
        fib = fibo(cnt)
        if is_pandigital(str(fib)[-9:]) and is_pandigital(str(fib)[:9]):
            break
        else:
            print cnt
            cnt += 1
    print cnt

def top_digits(n):
    # t = n * log10(phi) + log10((1/sqrt(5))
    t = n * 0.20898764024997873 + (-0.3494850021680094)
    t = int((pow(10, t - int(t) + 8)))
    return t

def main2():
    fn, f0, f1 = 2, 1, 1
    while not is_pandigital(f1) or not is_pandigital(top_digits(fn)):
        f0, f1 = f1, (f1 + f0) % 10 ** 9
        fn += 1
    print fn

if __name__ == '__main__':
    time_func(main2)
