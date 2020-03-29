# coding=gbk
import better_exceptions

better_exceptions.hook()

from scipy.special import cbrt

res = cbrt([1000, 27, 8, 23])  # 解立方根
print(res)
