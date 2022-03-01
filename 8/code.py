import numpy as np

if __name__ == "__main__":
    A = np.array(
        [[5, -1],
         [2, 3]]
    )
    x = np.array(
        [2, 1]
    )
    Ax = np.dot(A, x)
    print(Ax)

    a = np.array([[-1, 5],
                  [7, 0]])
    b = np.array([[3, 1],
                  [-2, 6]])

    ab = np.dot(a, b)
    print(ab)

    a = np.array(
        [[3, 0],
         [1, 2]]
    )
    b = np.array(
        [[0, -1],
         [5, 1]]
    )
    c = np.array(
        [[1, 4],
         [-3, 1]]
    )

    abc = np.linalg.multi_dot(
        [a, b, c]
    )
    print(abc)
