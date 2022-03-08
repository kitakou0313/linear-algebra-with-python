import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

if __name__ == "__main__":
    np.random.seed(10)

    A = np.random.randint(1, 10, (3, 3))
    P, L, U = lu(A)

    print(A)
    print(P)
    print(L)
    print(U)

    np.random.seed(0)
    A = np.random.randint(-4, 4, (3, 3))
    LU, piv = lu_factor(A)
    # L+Uが足されて返却される(互いに下三角、上三角なので干渉しない+Lの対角成分はすべて1なのでUの値として問題ない)

    print(A)
    print(LU)
    print(piv)

    A = np.random.randint(-6, 6, (10, 10))
    b = np.random.randint(0, 10, 10)

    x = lu_solve(lu_factor(A), b)

    print(A)
    print(b)
    print(x)
