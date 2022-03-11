import numpy as np


def eig_diag(x: np.ndarray) -> np.ndarray:
    """
    対角化行列と固有値行列を返す
    """
    eig = np.linalg.eig(x)
    e = np.diag(eig[0])
    p = eig[1]

    return e, p


if __name__ == "__main__":
    H = np.array(
        [[2, 1-1j],
         [1+1j, 3]]
    )

    D, U = eig_diag(H)
    print(D)
    print(U)

    print(np.linalg.norm(U, axis=0))
