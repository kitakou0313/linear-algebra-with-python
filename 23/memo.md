# 行列の固有値と固有ベクトル

## 固有値と固有ベクトル
- 行列`A`, 0ではないベクトル`x`について
- `Ax = λx`を満たすスカラー`λ`を`固有値`、`x`を固有ベクトルと定義する
## 求め方
- 固有方程式を解く`λ`を求める
    - `det(A - λI) = 0`
    - `(A - λI)x = 0`から求める
        - `x`は0でない => `(A - λI)`の列ベクトルが線形写像 => `det`が0
 