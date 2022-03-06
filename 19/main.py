import numpy as np
from libs import coordinate
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig, ax = plt.subplots(2, 1, sharex="all")
    coordinate(ax[0], [-6, 6], [-6, 6], xlabel="")
    coordinate(ax[1], [-6, 6], [-6, 6])

    x = np.arange(-10, 10)
    y = np.arange(-10, 10)

    X, Y = np.meshgrid(x, y)
    X = X.reshape(-1)
    Y = Y.reshape(-1)

    p0 = np.vstack((X, Y))

    a = np.array([[2, 1],
                  [3, 5]])

    p1 = np.dot(a, p0)
    ax[0].scatter(X, Y, color="blue")
    ax[1].scatter(p1[0], p1[1], color="red")

    plt.savefig("1.png")

    # det(a) = 0のケース
    fig, ax = plt.subplots(2, 1, sharex="all", figsize=(5, 10))
    coordinate(ax[0], [-6, 6], [-6, 6], xlabel="")
    coordinate(ax[1], [-6, 6], [-6, 6])

    x = np.linspace(-10, 10, 500)
    y = np.linspace(-10, 10, 500)
    X, Y = np.meshgrid(x, y)
    X = X.reshape(-1)
    Y = Y.reshape(-1)
    p0 = np.vstack((X, Y))

    a = np.array(
        [[1, 2],
         [2, 4]]
    )
    p1 = np.dot(a, p0)
    ax[0].scatter(X, Y)
    ax[1].scatter(p1[0], p1[1], s=3)

    plt.savefig("2.png")

    # rankの計算

    np.random.seed(9)

    for i in range(100):
        a = np.random.randint(0, 10, (4, 4))
        rank = np.linalg.matrix_rank(a)
        if rank < 4:
            print(rank)
            print(a)
