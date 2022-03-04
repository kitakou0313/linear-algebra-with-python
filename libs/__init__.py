from sympy import Symbol, var, init_printing
from sympy.matrices import Matrix
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2D座標設定関数


def coordinate(axes, range_x, range_y, grid=True,
               xyline=True, xlabel="x", ylabel="y"):
    axes.set_xlabel(xlabel, fontsize=16)
    axes.set_ylabel(ylabel, fontsize=16)
    axes.set_xlim(range_x[0], range_x[1])
    axes.set_ylim(range_y[0], range_y[1])
    if grid == True:
        axes.grid()
    if xyline == True:
        axes.axhline(0, color="gray")
        axes.axvline(0, color="gray")

# 3D座標設定関数


def coordinate_3d(axes, range_x, range_y, range_z, grid=True):
    axes.set_xlabel("x", fontsize=16)
    axes.set_ylabel("y", fontsize=16)
    axes.set_zlabel("z", fontsize=16)
    axes.set_xlim(range_x[0], range_x[1])
    axes.set_ylim(range_y[0], range_y[1])
    axes.set_zlim(range_z[0], range_z[1])
    if grid == True:
        axes.grid()


# 2Dベクトル描画関数


def visual_vector(axes, loc, vector, color="red"):
    axes.quiver(loc[0], loc[1],
                vector[0], vector[1], color=color,
                angles='xy', scale_units='xy', scale=1)

# 3Dベクトル描画関数


def visual_vector_3d(axes, loc, vector, color="red"):
    axes.quiver(loc[0], loc[1], loc[2],
                vector[0], vector[1], vector[2],
                color=color, length=1,
                arrow_length_ratio=0.2)


# ラベル付きポイント関数


def pointer(axes, x, y, text, angle=45,
            textsize=12, textcolor="black", pad=0.2,
            psize=None, pcolor=None, marker=None,
            cmap=None, norm=None, alpha=None,
            linewidths=None, edgecolors=None):

    # 点をプロット
    axes.scatter(x, y, s=psize, c=pcolor,
                 marker=marker, cmap=cmap, norm=norm,
                 alpha=alpha, linewidths=linewidths,
                 edgecolors=edgecolors)

    # 数学関数モジュールをインポート
    import math

    # テキストの配置角度をラジアンに変換
    text_angle = angle * math.pi / 180

    # テキストの位置を計算
    loc_x = x + pad * math.cos(text_angle)
    loc_y = y + pad * math.sin(text_angle)

    # テキストを配置
    axes.text(loc_x, loc_y, text,
              fontsize=textsize, color=textcolor)


init_printing()

# 添字付一般表記行列生成関数


def general_matrix(m, n, s):
    Symbol(s)
    def elements(i, j): return var('{}{}{}'.format(s, i+1, j+1))
    return Matrix(m, n, elements)
