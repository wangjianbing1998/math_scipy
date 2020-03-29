# coding=gbk
import better_exceptions

better_exceptions.hook()

from scipy import linalg as lg

import numpy as np

arr = np.array([[1, 2], [3, 4]])  # ������� #
print("Det:", lg.det(arr))  # ������ʽ #
print("Inv:", lg.inv(arr))  # ������� #
b = np.array([6, 14])
print("Sol:", lg.solve(arr, b))  # �ⷽ����#
print("Eig:", lg.eig(arr))  # ������ֵ#
print("LU:", lg.lu(arr))  # LU�ֽ�
print("QR:", lg.qr(arr))  # RQ�ֽ�
print("SVD:", lg.svd(arr))  # SVD�ֽ�
print("Schur:", lg.schur(arr))  # Schur����
