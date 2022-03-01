import numpy as np
from scipy.linalg import norm

if __name__ == "__main__":
    u = [3, 1, 0]
    v = [2, 5, 1]

    print(np.cross(u, v))
