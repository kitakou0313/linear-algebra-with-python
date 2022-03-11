import numpy as np
import scipy.linalg


np.set_printoptions(precision=3)


def hermitian(arr: np.ndarray) -> np.ndarray:
    """
    共役転置行列
    """
    return np.conjugate(arr.T)


def normalize(arr: np.ndarray, axis=0) -> np.ndarray:
    """
    各列ベクトルを正規化する
    """
    norm = scipy.linalg.norm(arr, axis=axis)
    print(norm)
    return arr / norm


if __name__ == "__main__":
    A = np.array([[-2, 1],
                  [1+1j, 1+1j]])

    U = normalize(A)

    print(hermitian(U) @ U)
    print(U @ hermitian(U))

    z = np.array([3+5j, 2-1j])

    Uz = U@z

    print(np.linalg.norm(z))
    print(np.linalg.norm(Uz))

    eigvals = scipy.linalg.eig(U)[0]
    print(np.abs(eigvals))
