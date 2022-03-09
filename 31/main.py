import numpy as np
import scipy.linalg

if __name__ == "__main__":
    A = np.array(
        [[2, 0, 0],
         [0, 3, 1],
         [0, 0, 0]]
    )
    CA = scipy.linalg.orth(A)
    print(CA)

    CA_T = scipy.linalg.orth(A.T)
    print(CA_T)
