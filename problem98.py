# Project Euler problem 98

from projecteuler import time_func, is_palindrome, is_perm


def create_words():
    f = open("problem98.txt", "r")
    lines = list()
    for line in f:
        lines.append(line[:-1])
    line = lines[0]
    words = line.split(",")
    words = [x[1:-1] for x in words]
    return words

def create_perm_words():
    words = create_words()
    # remove palindrome words
    words = [x for x in words if not is_palindrome(x)]
    perm_words = set()
    for word1 in words:
        tmp = list()
        tmp.append(word1)
        for word2 in words:
            if is_perm(word1, word2) and word1 != word2:
                #perm_words.add((word1, word2))
                tmp.append(word2)
                #print "word2", word2
                #print "tmp", tmp
        #print "total tmp",  tmp
        if len(tmp) > 1:
            perm_words.add(tuple(tmp))
    return perm_words

def main():
    perm_words = create_perm_words()
    print perm_words

if __name__ == '__main__':
    main()
