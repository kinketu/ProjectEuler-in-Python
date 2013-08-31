# Project Euler problem 42

from projecteuler import alpha_number, time_func

def word_value(word):
    """Return the word value for the word"""
    return sum([int(alpha_number(i)) for i in word])

def main():
    f = open('problem42.txt', 'r')
    words = []
    for line in f:
        words.append(line[1:-2])    

    T = set((n * (n + 1) / 2) for n in range(1, 400))
    
    tri_words = []
    tri_numbers = []
    values = []
    for word in words:
        value = word_value(word)
        #print word, value
        values.append(value)
        if value in T:
            tri_words.append(word)
            tri_numbers.append(value)
    #print "There are %d triangle words exist." % len(tri_words)
    print len(tri_words)
        
if __name__ == '__main__':
    time_func(main)
