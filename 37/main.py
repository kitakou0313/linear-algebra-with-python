import numpy as np
import scipy.linalg


if __name__ == "__main__":
    np.set_printoptions(precision=3, suppress=True)
    np.random.seed(0)

    A = np.random.randint(-9, 10, (4, 6))

    Q, R = np.linalg.qr(A)

    print(A)
    print(Q)
    print(R)
