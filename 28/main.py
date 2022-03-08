import numpy as np

if __name__ == "__main__":

    A = np.arange(1, 17).reshape(4, 4)

    L = np.tril(A)
    print(L)

    L = np.tri(4)
    print(L)

    U = np.triu(A)
    print(U)
