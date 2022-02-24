import numpy as np

if __name__ == "__main__":
    v = np.array(
        [10, 20, 30]
    )
    w = np.array(
        [2, 4, 6]
    )

    print(v+w)
    print(v-w)

    # 内積ではない
    print(v * w)

    v = np.array(
        [1, 2, 3]
    )

    print(10 * v)
    # ブロードキャスト機能
    print(v + 100)

    # numpyのvectorは厳密には1階のテンソルとして定義されている
