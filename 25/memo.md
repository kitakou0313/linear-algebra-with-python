# 行列の累乗

## 定義
- 同じ行列をk回乗算すること
- `A^k`と表す

## 固有値との関連
- `A^k`の固有値は`λ^k`、固有ベクトルは`x`
    - `Ax = λx`を考える
    - `A(Ax) = λ(Ax)`
    - `A^2(x) = λ^2x`

## 対角化との関連
- 対角化により容易にk乗を求められる
    - `D = P^{-1}AP`
        - D...対角行列、P...対角化行列
    - `A = PDP^{-1}`
    - `A^2 = (PDP^{-1})(PDP^{-1}) = PD^2P^{-1}`
        - 同様にk乗も求められる
    - `A^k = PD^kP^{-1}`