from cmath import atan
import numpy as np
if __name__ == "__main__":
    np.random.seed(12)

    a = np.random.randint(1, 10, (3, 5))
    a_t = np.transpose(a)

    print(a)
    print(a_t)
    print(a.T)
