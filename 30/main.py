from importlib import import_module
import numpy as np
import scipy.linalg

if __name__ == "__main__":
    A = np.array(
        [[1, 2, 2, 4],
         [3, 10, 6, 20]]
    )
    ns = scipy.linalg.null_space(A)
    print(ns)

    print(A @ ns)

    K = 2*ns[:, 0:1] + 3*ns[:, 1:2]

    print(A @ K)
