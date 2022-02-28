import numpy as np
from scipy.linalg import det

# 行列式
if __name__ == "__main__":
    x = np.array(
        [[5, 2],
         [-3, 4]]
    )

    det_x = det(x)
    print(det_x)
