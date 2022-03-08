import numpy as np


def eig_diag(x):
    """
    対角行列、対角化行列を求める
    """
    eig = np.linalg.eig(x)
    e = np.diag(eig[0])
    p = eig[1]
    return e, p


if __name__ == "__main__":
    a = np.arange(1, 10).reshape(3, 3)
    a_5 = np.linalg.matrix_power(a, 5)

    print(a_5)

    d, p = eig_diag(a)
    p_inv = np.linalg.inv(p)

    a_5_manual = p @ (d ** 5) @ p_inv

    print(a_5_manual)
