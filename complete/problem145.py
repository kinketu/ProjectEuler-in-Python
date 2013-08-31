# Project Euler problem 145
# cf. http://d.hatena.ne.jp/Rion778/20100519/1274204124

from projecteuler import num_reverse, time_func

def is_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

def is_all_odd(n):
    nums = [int(x) for x in list(str(n))]
    return all([is_odd(x) for x in nums])

def is_reversible(n):
    sum_num = n + num_reverse(n)
    if list(str(n))[0] == "0" or list(str(n))[-1] == "0":
        return False
    elif is_all_odd(sum_num):
        return True
    else:
        return False
            
def main1():
    """O(n), 30000 sec"""
    cnt = 0
    end = 10000 # end is 10 ** 9
    for i in xrange(1, end):
        if is_reversible(i):
            print i
            cnt += 1
    print cnt

def main2():
    ans = 20 + 20 * 30 + 20 * 30 ** 2 + 20 * 30 ** 3 + 20 * 5 + \
          20 * 20 * 25 * 5
    print ans

if __name__ == '__main__':
    time_func(main2)
