# Project Euler problem 68
# cf. http://d.hatena.ne.jp/trex5/20100222/p1

from itertools import permutations
from projecteuler import time_func

def main():
    answer = list()
    for outs in permutations(range(7, 11)):
        outs = [6] + list(outs)
        for ins in permutations(range(1, 6)):
            ins = list(ins)
            if len(set([sum([outs[i]] + ins[i:i+2]) \
                    for i in xrange(len(outs) - 1)] \
                    + [outs[-1] + ins[0] + ins[-1]])) == 1:
                da = [[outs[i]] + ins[i:i+2] \
                        for i in xrange(len(outs)-1)] \
                        + [[outs[-1]] + [ins[-1]] + [ins[0]]]
                answer.append(int("".join(["".join(map(str, da[k])) \
                        for k in xrange(len(outs))])))
    print max(answer)


if __name__ == '__main__':
    time_func(main)
