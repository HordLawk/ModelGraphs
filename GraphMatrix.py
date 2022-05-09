import random

n = int(input())
p = float(input())

def newM(n_, p_):
    if (p_ < 0) or (p_ > 1):
        print("p must be between 0 and 1")
        return []
    m = [[None for x in range(n_)] for y in range(n_)]
    for i in range(n_):
        for k in range(i, n_):
            m[i][k] = m[k][i] = int(random.random() > p_)
    return m

m = newM(n, p)

for i in range(len(m)):
    print(m[i])