import numpy as np
from scipy.linalg import norm
if __name__ == "__main__":
    # ユークリッドノルムの実装

    v = np.array(
        [1, 2, 3]
    )

    v_n = np.sqrt(
        np.sum(v**2)
    )
    print(v_n)

    v_n = norm(v_n)
    print(v_n)

    a = np.array(
        [[1, 2, 3],
         [4, 5, 6]]
    )
    # axisは適用する軸を指定するイメージ
    a_n = norm(a, axis=1)
    print(a_n)

    v = np.array(
        [1, 1]
    )
    u = v / norm(v)
    print(u)

    a = np.array(
        [[1, 2, 3],
         [4, 5, 6]]
    )

    a = a / norm(a, axis=1, keepdims=True)
    print(a)

    a_norm = norm(
        a, axis=1, keepdims=True
    )

    print(a_norm)
