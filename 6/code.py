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

    # 行列の転置普遍性
    x = np.array(
        [[5, 9, 2, 7],
         [1, 3, 9, 5],
         [6, 2, 0, 4],
         [2, 6, 3, 3]]
    )
    print(det(x))
    print(det(x.T))
