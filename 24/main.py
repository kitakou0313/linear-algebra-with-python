import numpy as np


def eig_diag(x: np.array):
    """
    固有値を対角化行列の形で返す
    """
    eig = np.linalg.eig(x)
    e = np.diag(eig[0])
    p = eig[1]
    return e, p


if __name__ == "__main__":
    a = np.array(
        [[3, 1],
         [2, 4]]
    )

    det_a = np.linalg.det(a)
    print(det_a)

    e = eig_diag(a)

    print(e[0])
    print(e[1])
    p = e[1]

    p_inv = np.linalg.inv(p)
    d2 = p_inv @ a @ p
    print(d2)

    a = np.arange(1, 101).reshape(10, 10)
    det_a = np.linalg.det(a)

    e = eig_diag(a)
    d = e[0]

    tr_a = np.trace(a)
    tr_d = np.trace(d)

    print(tr_a, tr_d)

    det_d = np.linalg.det(a)

    print(det_a, det_d)
