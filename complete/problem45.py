# Project Euler problem 45
# cf. http://alphacentauri32.wordpress.com/2011/05/05/
# project-euler-problem-45-solved-with-python/


from projecteuler import time_func

def main():
    """Main Program"""
    T = set((n * (n + 1) / 2) for n in range(2, 180000))
    P = set((n * ((3 * n) - 1) / 2) for n in range(2, 180000))
    H = set((n * ((2 * n) - 1)) for n in range(2, 180000))
    for i in T:
        if i in P and i in H and i != 40755:
            print i
            break
        else:
            continue
 
if __name__ == '__main__':
    time_func(main)
