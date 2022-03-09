import numpy as np
import scipy.linalg


if __name__ == "__main__":
    A = np.array(
        [[0, 1, 1, 5],
         [1, 1, 2, 2],
         [2, 2, 4, 4]]
    )

    rank_A = np.linalg.matrix_rank(A)
    ker_A = scipy.linalg.null_space(A)

    ker_A_T = scipy.linalg.null_space(A.T)

    dim_ker_A = ker_A.shape[1]
    dim_ker_A_T = ker_A_T.shape[1]

    print(A.shape)
    print(rank_A)
    print(dim_ker_A)
