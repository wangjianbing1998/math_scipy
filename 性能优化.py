# coding=gbk
import better_exceptions

better_exceptions.hook()
from scipy import optimize

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


# 定义函数
def f(x):
    return x ** 2 + 2 * x + 9


# x取值：-10到10之间，间隔0.1
x = np.arange(-10, 10, 0.1)

# 画出函数曲线
plt.plot(x, f(x))
# plt.savefig('./opt2-1.png') # 保存要显示的图片
plt.show()


# 定义函数
def f(x):
    return x ** 2 + 2 * x + 9


# x取值：-10到10之间，间隔0.1
x = np.arange(-10, 10, 0.1)

# 画出函数曲线
plt.plot(x, f(x))

# 第一个参数是函数名，第二个参数是梯度下降的起点。返回值是函数最小值的x值(ndarray数组)
xopt = optimize.fmin_bfgs(f, 0)

xmin = xopt[0]  # x值
ymin = f(xmin)  # y值，即函数最小值
print('xmin: ', xmin)
print('ymin: ', ymin)

# 画出最小值的点, s=20设置点的大小，c='r'设置点的颜色
plt.scatter(xmin, ymin, s=20, c='r')

# plt.savefig('./opt3-1.png') # 保存要显示的图片
plt.show()

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


# 定义函数
def g(x):
    return x ** 2 + 20 * np.sin(x)


# x取值：-10到10之间，间隔0.1
x = np.arange(-10, 10, 0.1)

# 画出函数曲线
plt.plot(x, g(x))
# plt.savefig('./opt4-1.png') # 保存要显示的图片
plt.show()


# 定义函数
def g(x):
    return x ** 2 + 20 * np.sin(x)


# x取值：-10到10之间，间隔0.1
x = np.arange(-10, 10, 0.1)

# 画出函数曲线
plt.plot(x, g(x))

# 第一个参数是函数名，第二个参数是梯度下降的起点。返回值是函数最小值的x值(ndarray数组)
# 可以看到5.0附近有个局部最小，把初始值设置为7, 返回的应该是这个局部最小值。
xopt = optimize.fmin_bfgs(g, 7)

xmin = xopt[0]  # x值
ymin = g(xmin)  # y值，即函数最小值
print('xmin: ', xmin)
print('ymin: ', ymin)

# 画出最小值的点, s=20设置点的大小，c='r'设置点的颜色
plt.scatter(xmin, ymin, s=20, c='r')

# plt.savefig('./opt5-1.png') # 保存要显示的图片
plt.show()


# 定义函数
def g(x):
    return x ** 2 + 20 * np.sin(x)


# 求取最小值，初始值为7
ret = optimize.basinhopping(g, 7)

print(ret)
