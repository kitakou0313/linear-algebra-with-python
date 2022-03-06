import numpy as np

if __name__ == "__main__":
    np.random.seed(15)

    a = np.random.randint(0, 10, (3, 3))
    b = np.random.randint(0, 10, (3, 3))

    ab = np.dot(a, b)
    ba = np.dot(b, a)

    tr_ab = np.trace(ab)
    tr_ba = np.trace(ba)

    print(ab)
    print(ba)

    print(tr_ab)
    print(tr_ba)
