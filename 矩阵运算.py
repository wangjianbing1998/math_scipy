# coding=gbk
import better_exceptions

better_exceptions.hook()

from scipy import linalg as lg

import numpy as np

arr = np.array([[1, 2], [3, 4]])  # 定义矩阵 #
print("Det:", lg.det(arr))  # 求行列式 #
print("Inv:", lg.inv(arr))  # 求逆矩阵 #
b = np.array([6, 14])
print("Sol:", lg.solve(arr, b))  # 解方程组#
print("Eig:", lg.eig(arr))  # 求特征值#
print("LU:", lg.lu(arr))  # LU分解
print("QR:", lg.qr(arr))  # RQ分解
print("SVD:", lg.svd(arr))  # SVD分解
print("Schur:", lg.schur(arr))  # Schur矩阵
