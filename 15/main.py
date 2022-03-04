import numpy as np
from libs import coordinate, pointer
import matplotlib.pyplot as plt


if __name__ == "__main__":
    fig: plt.figure = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)

    coordinate(ax, [-6, 6], [-6, 6])

    a = np.array(
        [[1, 0],
         [0, -1]]
    )
    p0 = np.array([3, 3])
    p1 = np.dot(a, p0)

    pointer(ax, p0[0], p0[1], "P0",
            pcolor="red", textsize=15)

    pointer(ax, p1[0], p1[1], "P1",
            pcolor="blue", textsize=15)

    plt.savefig("img.png")
