from matplotlib.pyplot import sci
import numpy as np
import scipy.linalg


def hermitian(arr: np.ndarray) -> np.ndarray:
    """
    随伴行列を返す
    """
    return np.conjugate(arr.T)


if __name__ == "__main__":
    A = np.array(
        [[1, 1+1j],
         [1-1j, 1j]]
    )
    A_h = hermitian(A)
    print(A_h)

    A = np.array(
        [[1+2j, 1-1j],
         [2+3j, 2+1j]]
    )

    B = scipy.linalg.inv(hermitian(A))
    C = hermitian(scipy.linalg.inv(A))

    print(scipy.linalg.inv(A))
    print(np.linalg.inv(A))

    print(B)
    print(C)

    v = np.array([1+1j, 2-1j])
    w = np.array([2+5j, 1-1j])

    print(np.dot(hermitian(v), w))
    print(np.dot(hermitian(w), v))

    v = np.array([3+2j, 1-1j])
    v_norm = scipy.linalg.norm(v)
    print(v_norm)
