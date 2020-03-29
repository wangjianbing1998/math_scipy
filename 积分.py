# coding=gbk
import better_exceptions
from scipy import integrate, exp

better_exceptions.hook()

# 一重积分
import scipy.integrate

f = lambda x: exp(-x ** 2)
i = scipy.integrate.quad(f, 0, 5)
print(i)


# 带参数的一重积分
def f(x, a, b):
    return a * (x ** 2) + b


ret = integrate.quad(f, 0, 1, args=(3, 1))
print(ret)

# 二重积分

from math import sqrt

f = lambda x, y: 19 * x * y
g = lambda x: 0
h = lambda y: sqrt(1 - 4 * y ** 2)
i = integrate.dblquad(f, 0, 0.5, g, h)
print(i)

# 三重积分
f = lambda r, z: r * sqrt(r ** 2 + z ** 2) + r / (r ** 2 + z ** 2)
g = lambda z: (z ** 2) / 3
h = lambda z: z ** 2

print(integrate.dblquad(f, 0, 1, g, h))
