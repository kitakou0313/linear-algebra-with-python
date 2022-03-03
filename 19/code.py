import numpy as np

if __name__ == "__main__":
    x = np.arange(-10, 10)
    y = np.arange(-10, 10)

    X, Y = np.meshgrid(x, y)
    X = X.reshape(-1)
    Y = Y.reshape(-1)

    p0 = np.vstack((X, Y))

    a = np.array([[2, 1],
                  [3, 5]])

    p1 = np.dot(a, p0)
