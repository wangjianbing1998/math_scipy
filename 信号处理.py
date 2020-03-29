# coding=gbk
import better_exceptions

better_exceptions.hook()

import numpy as np

t = np.linspace(0, 5, 100)
x = np.sin(t)

from scipy import signal

x_resampled = signal.resample(x, 25)

import matplotlib.pyplot as plt

plt.plot(t, x)
plt.plot(t[::4], x_resampled, 'ko')

# plt.savefig('./sig1-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()

# �������ź���ȥ����������
t = np.linspace(0, 5, 100)
x = t + np.random.normal(size=100)

from scipy import signal

x_detrended = signal.detrend(x)

import matplotlib.pyplot as plt

plt.plot(t, x)
plt.plot(t, x_detrended)

# plt.savefig('./sig2-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()
