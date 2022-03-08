import numpy as np


def matrix_p(n, i=1, j=1) -> np.ndarray:
    """
    i行とj行の交換行列を生成
    """
    arr = np.eye(n)
    arr[[i-1, j-1]] = arr[[j-1, i-1]]

    return arr


def matrix_c(n, i=1, k=1) -> np.ndarray:
    """
    i行の定数倍行列
    """
    arr = np.eye(n)
    arr[i-1, i-1] = k
    return


def matrix_e(n, i=1, j=1, k=1) -> np.ndarray:
    """
    i行にj行のk倍を加える行列を生成
    """
    arr = np.eye(n)
    arr[i-1, j-1] = k
    return arr


if __name__ == "__main__":
    p = matrix_p(4, 2, 3)

    print(p)

    x = np.arange(1, 10).reshape(3, 3)

    x[2, :] = x[2, :] + x[0, :]*5
    print(x)

    x = np.arange(1, 10).reshape(3, 3)
    print(x[[1, 2]])
