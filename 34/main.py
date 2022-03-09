from matplotlib.pyplot import sci
import numpy as np
import scipy.linalg


def projection_matrix(x: np.ndarray) -> np.ndarray:
    """
    射影行列を求める関数
    """
    return x @ scipy.linalg.inv(x.T @ x) @ x.T


if __name__ == "__main__":
    A = np.array(
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1],
         [0, 0, 1]]
    )
    P = projection_matrix(A)

    v = np.array([[1, 1, 1, 1]]).T

    Pv = P@v

    print(P)
    print(Pv)
