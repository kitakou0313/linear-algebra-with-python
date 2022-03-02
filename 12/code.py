import numpy as np
from scipy import linalg

if __name__ == "__main__":
    a = np.array(
        [[5, -1],
         [2, 3]]
    )
    b = np.array(
        [9, 7]
    )
    a_inv = np.linalg.inv(a)
    print(np.dot(a_inv, b))
    print(np.dot(b, a_inv))
