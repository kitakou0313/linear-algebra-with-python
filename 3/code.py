import numpy as np


def v_angle(v1: np.array, v2: np.array, deg=False):
    """
    v1, v2のなす角度を求める
    """
    v1_n = np.linalg.norm(v1)
    v2_n = np.linalg.norm(v2)

    v1_v2_dot = np.dot(v1, v2)

    cos_theta = v1_v2_dot / (v1_n * v2_n)
    theta = np.arccos(cos_theta)

    return np.degrees(theta) if deg else theta


if __name__ == "__main__":
    v = np.array(
        [3, 2, 6]
    )
    w = np.array(
        [4, 7, 2]
    )

    ip = np.dot(v, w)
    print(ip)

    print(v.dot(w))

    print(np.vdot(v, w))

    a = np.array(
        [
            [1, 4],
            [3, 5]
        ]
    )
    b = np.array(
        [[3, 7],
         [4, 9]]
    )
    print(np.vdot(a, b))

    print(np.inner(v, w))

    v = np.array([1, 0])
    w = np.array([1, np.sqrt(3)])
    theta = v_angle(v, w, deg=True)

    print(theta)
