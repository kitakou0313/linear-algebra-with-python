from matplotlib.pyplot import axis
import numpy as np


def cofactor(a: np.array, i, j, minor=False):
    """
    余因子と小行列式
    """
    x = np.delete(a, i, axis=0)
    x = np.delete(x, j, axis=1)

    return np.linalg.det(x) if minor else (-1)**(i + j)*np.linalg.det(x)


if __name__ == "__main__":
    a = np.array(
        [[2, 7, 3],
         [5, 0, 9],
         [3, 1, 4]]
    )

    print(cofactor(a, 0, 1, minor=True))
    print(cofactor(a, 0, 1))

    a_ij = np.zeros((3, 3))

    for i in range(3):
        for j in range(3):
            a_ij[i, j] = cofactor(a, i, j)

    a_inv_1 = a_ij / np.linalg.det(a)
    a_inv_2 = np.linalg.inv(a)

    print(a_inv_1)
    print(a_inv_2)
