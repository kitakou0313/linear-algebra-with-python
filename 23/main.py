import numpy as np
from scipy import linalg

if __name__ == "__main__":

    a = np.array(
        [[3, 1],
         [2, 4]]
    )
    a_eig = np.linalg.eig(a)

    x = a_eig[1][:, 0]
    l = a_eig[0][0]
    print(l, x)

    print(np.dot(a, x))
    print(l * x)

    x_1 = np.array(
        [2, 5]
    )

    print(x_1*a)
