# Project Euler problem 82

from numpy import zeros, array

def next(b, c):
    def min_path(k):
        def sum_path(l):
            if l <= k:
                return sum(c[l:k+1]) + b[l]
            else:
                return sum(c[k:l+1]) + b[l]

        return reduce(min, map(sum_path, range(N)))

    return map(min_path, range(N))

def main1():
    f = open('problem82.txt', 'r')
    mat = map(lambda s: map(int, s.split(',')), f.readlines())
    #print mat
    f.close()
    N = len(mat)
    #print [[e[c] for e in mat] for c in range(N)]
    print min(reduce(next, ([e[c] for e in mat] for c in range(N))))

def create_test_matrix():
    mat = array([[131, 673, 234, 103, 18], \
                 [201, 96, 342, 965, 150], \
                 [630, 803, 746, 422, 111], \
                 [537, 699, 497, 121, 956], \
                 [805, 732, 524, 37, 331]])
    return mat

def main2():
    mat = create_test_matrix()
    N = mat.shape[0]
    print mat
    min_mat = zeros((N, N))
    #print min_mat
    for i in range(N):
        for j in range(N):
            if j == 0:
                min_mat[i, j] = mat[i, j]
    print min_mat
    


if __name__ == '__main__':
    main2()
