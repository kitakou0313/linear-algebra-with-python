import numpy as np
from scipy.linalg import norm

if __name__ == "__main__":
    v = np.array(
        [2, 3]
    )
    w = np.array(
        [2, 5]
    )

    a = np.abs(np.dot(v, w))
    b = norm(v)*norm(w)

    # コーシーシュワルツ |v*w| <= |v|*|w|
    print(b-a)

    # 三角不等式 ||v + w|| <= ||v|| + ||w||
    a = norm(v + w)
    b = norm(v)+norm(w)

    print(b-a)
