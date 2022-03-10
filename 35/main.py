import numpy as np
import scipy.linalg


if __name__ == "__main__":
    X = np.array(
        [[1, -1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    )
    print(scipy.linalg.det(X))

    x = np.sqrt(2)/2

    Q = np.array(
        [[x, x, 0],
         [-x, x, 0],
         [0, 0, 1]]
    )

    print(Q @ Q.T)

    print(Q)
    print(Q.T)

    print(Q.T @ Q)

    Q = np.array(
        [[x, 0],
         [x, 0],
         [0, 1]]
    )

    print(Q.T @ Q)
    print(Q @ Q.T)
