# coding=gbk
import better_exceptions
from scipy import integrate, exp

better_exceptions.hook()

# һ�ػ���
import scipy.integrate

f = lambda x: exp(-x ** 2)
i = scipy.integrate.quad(f, 0, 5)
print(i)


# ��������һ�ػ���
def f(x, a, b):
    return a * (x ** 2) + b


ret = integrate.quad(f, 0, 1, args=(3, 1))
print(ret)

# ���ػ���

from math import sqrt

f = lambda x, y: 19 * x * y
g = lambda x: 0
h = lambda y: sqrt(1 - 4 * y ** 2)
i = integrate.dblquad(f, 0, 0.5, g, h)
print(i)

# ���ػ���
f = lambda r, z: r * sqrt(r ** 2 + z ** 2) + r / (r ** 2 + z ** 2)
g = lambda z: (z ** 2) / 3
h = lambda z: z ** 2

print(integrate.dblquad(f, 0, 1, g, h))
