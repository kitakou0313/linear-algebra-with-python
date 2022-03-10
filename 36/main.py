import numpy as np
import scipy.linalg


def schmidt(arr: np.ndarray):
    """
    グラムシュミットによる正規直交基底を得る
    """
    arr = np.array(arr, dtype=np.float64)
    k = arr.shape[1]

    u = arr[:, [0]]
    q = u / scipy.linalg.norm(u)

    for j in range(1, k):
        u = arr[:, [j]]

        for i in range(j):
            u -= np.dot(q[:, i], arr[:, j]) * q[:, [i]]
        qi = u / scipy.linalg.norm(u)
        q = np.append(q, qi, axis=1)

    return q


if __name__ == "__main__":
    A = np.array(
        [[3, 1, 1],
         [1, 0, 1],
         [2, 5, 0]]
    )
    Q = schmidt(A)

    print(Q)

    # print(Q[:, 0] @ Q[:, 1])
    print(Q[:, [0]])
    print(Q[:, 0])

    v = np.array([1, 2, 3])

    Qv = np.dot(Q, v)

    print(scipy.linalg.norm(v), scipy.linalg.norm(Qv))
