# coding=gbk
import better_exceptions

better_exceptions.hook()

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(0, 4, 12)
y = np.cos(x ** 2 / 3 + 4)
print(x)
print(y)

plt.plot(x, y, 'o')
plt.show()

from scipy import interpolate as intp

f1 = intp.interp1d(x, y, kind='linear')
f2 = intp.interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 4, 30)

plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')

plt.legend(['data', 'linear', 'cubic', 'nearest'], loc='best')

plt.show()

# 噪声数据插值
from scipy.interpolate import UnivariateSpline

x = np.linspace(-3, 3, 50)
y = np.exp(-x ** 2) + 0.1 * np.random.randn(50)  # 通过random方法添加噪声数据
plt.plot(x, y, 'ro', ms=5)

# 平滑参数使用默认值
spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'b', lw=3)  # 蓝色曲线

# 设置平滑参数
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'g', lw=3)  # 绿色曲线

# 设置平滑参数为0
spl.set_smoothing_factor(0)
plt.plot(xs, spl(xs), 'yellow', lw=3)  # 黄色曲线

plt.show()
