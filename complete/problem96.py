def solve(mat):
    tcan = [] # list of candidates
    i = 0
    mmin = immin = jmmin = 10  # item with least > 1 candidates
    while (i < 9):
        j = 0
        while (j < 9):
            if mat[i][j] == 0:
                t = list(set(range(1,10))- set(mat[i/3*3][j/3*3:j/3*3+3] + mat[i/3*3+1][j/3*3:j/3*3+3] + mat[i/3*3+2][j/3*3:j/3*3+3] + mat[i] + [mat[a][j] for a in range(9)]))
                if t == []: # can't find a candidate
                    return False
                if len(t) == 1:
                    if immin == i and jmmin == j: # replacing current least
                        mmin = immin = jmmin = 10
                    mat[i][j] = t[0]
                    i = -1
                    break
                if len(t) < mmin: # saving shortest candidate list
                    tcan, mmin, immin, jmmin = t, len(t), i, j
            j += 1
        i += 1
    if mmin == 10:
        return mat
    else:
        for test in tcan:
            mtest=[r[:] for r in mat] # copy without reference
            mtest[immin][jmmin] = test
            mtry = solve(mtest)
            if not mtry == False:
                return mtry
    return False

a = file('problem96.txt','r').readlines()
mt = []
count = 0
for x in a:
    if x[0] == 'G':
        mt = []
        print x
    else:
        mt.append (map(int, list(x)[0:9]))
        if len(mt)==9:
            m = solve(mt)
            for r in m:
                print r
            i = int(''.join(map(str,m[0][0:3])))
            count += i
print count
