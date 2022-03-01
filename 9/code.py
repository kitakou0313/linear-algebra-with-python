import numpy as np
from scipy import linalg

# 単位行列、逆行列、正則行列（逆行列を持つ行列）
if __name__ == "__main__":
    I = np.identity(
        2, dtype=np.int8
    )
    A = np.array(
        [[3, 7],
         [9, 5]]
    )

    AI = np.dot(A, I)
    print(AI)

    a = np.array(
        [[1, 2],
         [3, 4]]
    )
    a_inv = np.linalg.inv(a)
    b = np.dot(a, a_inv)

    print(a_inv)
    print(b)

    a_inv_scipy = linalg.inv(a)

    print(a_inv_scipy)
    print(np.dot(a, a_inv_scipy))
