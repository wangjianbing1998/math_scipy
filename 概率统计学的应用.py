# coding=gbk
import better_exceptions

better_exceptions.hook()

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

samples = np.random.normal(size=1000)
bins = np.arange(-4, 5)

histogram = np.histogram(samples, bins=bins, normed=True)[0]
bins = 0.5 * (bins[1:] + bins[:-1])

from scipy import stats

pdf = stats.norm.pdf(bins)  # norm是一个分布对象

plt.plot(bins, histogram)
plt.plot(bins, pdf)

# plt.savefig('./st1-1.png') # 保存要显示的图片
plt.show()

loc, std = stats.norm.fit(samples)
print(loc, std)

# 统计检验
a = np.random.normal(0, 1, size=100)
b = np.random.normal(1, 1, size=10)
stats.ttest_ind(a, b)
