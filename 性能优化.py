# coding=gbk
import better_exceptions

better_exceptions.hook()
from scipy import optimize

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


# ���庯��
def f(x):
    return x ** 2 + 2 * x + 9


# xȡֵ��-10��10֮�䣬���0.1
x = np.arange(-10, 10, 0.1)

# ������������
plt.plot(x, f(x))
# plt.savefig('./opt2-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()


# ���庯��
def f(x):
    return x ** 2 + 2 * x + 9


# xȡֵ��-10��10֮�䣬���0.1
x = np.arange(-10, 10, 0.1)

# ������������
plt.plot(x, f(x))

# ��һ�������Ǻ��������ڶ����������ݶ��½�����㡣����ֵ�Ǻ�����Сֵ��xֵ(ndarray����)
xopt = optimize.fmin_bfgs(f, 0)

xmin = xopt[0]  # xֵ
ymin = f(xmin)  # yֵ����������Сֵ
print('xmin: ', xmin)
print('ymin: ', ymin)

# ������Сֵ�ĵ�, s=20���õ�Ĵ�С��c='r'���õ����ɫ
plt.scatter(xmin, ymin, s=20, c='r')

# plt.savefig('./opt3-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


# ���庯��
def g(x):
    return x ** 2 + 20 * np.sin(x)


# xȡֵ��-10��10֮�䣬���0.1
x = np.arange(-10, 10, 0.1)

# ������������
plt.plot(x, g(x))
# plt.savefig('./opt4-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()


# ���庯��
def g(x):
    return x ** 2 + 20 * np.sin(x)


# xȡֵ��-10��10֮�䣬���0.1
x = np.arange(-10, 10, 0.1)

# ������������
plt.plot(x, g(x))

# ��һ�������Ǻ��������ڶ����������ݶ��½�����㡣����ֵ�Ǻ�����Сֵ��xֵ(ndarray����)
# ���Կ���5.0�����и��ֲ���С���ѳ�ʼֵ����Ϊ7, ���ص�Ӧ��������ֲ���Сֵ��
xopt = optimize.fmin_bfgs(g, 7)

xmin = xopt[0]  # xֵ
ymin = g(xmin)  # yֵ����������Сֵ
print('xmin: ', xmin)
print('ymin: ', ymin)

# ������Сֵ�ĵ�, s=20���õ�Ĵ�С��c='r'���õ����ɫ
plt.scatter(xmin, ymin, s=20, c='r')

# plt.savefig('./opt5-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()


# ���庯��
def g(x):
    return x ** 2 + 20 * np.sin(x)


# ��ȡ��Сֵ����ʼֵΪ7
ret = optimize.basinhopping(g, 7)

print(ret)
