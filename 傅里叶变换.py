# coding=gbk
import better_exceptions

better_exceptions.hook()

import numpy as np
# ��fftpack�е���fft(���ٸ���Ҷ�仯)��ifft(���ٸ���Ҷ��任)����
from scipy.fftpack import fft, ifft

# ����һ�����ֵ����
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

# ���������ݽ��и���Ҷ�任
y = fft(x)
print('fft: ')
print(y)

# ���ٸ���Ҷ��任
yinv = ifft(y)
print('ifft: ')
print(yinv)

import numpy as np
from scipy.fftpack import fft

# ��������
N = 4000

# ����Ƶ�� (���ݲ�����������Ƶ�ʱ�������ź����Ƶ�ʵ�2�����źŲŲ���ʧ��)
Fs = 8000
x = np.linspace(0.0, N / Fs, N)

# ʱ���źţ�������ֱ���������1.0�����Ҳ�����Ƶ��100hz/���2.0, ���Ҳ�����Ƶ��150Hz/���0.5/��λnp.pi
y = 1.0 + 2.0 * np.sin(100.0 * 2.0 * np.pi * x) + 0.5 * np.sin(150.0 * 2.0 * np.pi * x + np.pi)

# ����fft�任
yf = fft(y)

# ��ȡ�����ȡ�����ľ���ֵ����������ģ
abs_yf = np.abs(yf)

# ��ȡ��λ��ȡ�����ĽǶ�
angle_y = np.angle(yf)

# ֱ���ź�
print('\nֱ���ź�')
print('���:', abs_yf[0] / N)  # ֱ������������Ŵ���N��

# 100hz�ź�
index_100hz = 100 * N // Fs  # ���ε�Ƶ�� = i * Fs / N�����Ƽ���������i = ����Ƶ�� * N / Fs
print('\n100hz����')
print('���:', abs_yf[index_100hz] * 2.0 / N)  # �Ҳ�����������Ŵ���N/2��
print('��λ:', angle_y[index_100hz])

# 150hz�ź�
index_150hz = 150 * N // Fs  # ���ε�Ƶ�� = i * Fs / N�����Ƽ���������i = ����Ƶ�� * N / Fs
print('\n150hz����')
print('���:', abs_yf[index_150hz] * 2.0 / N)  # �Ҳ�����������Ŵ���N/2��
print('��λ:', angle_y[index_150hz])
print('100hz��150hz��λ��:', angle_y[index_150hz] - angle_y[index_100hz])
print('\n')

# DCT�任

import numpy as np
from scipy.fftpack import dct, idct

y = dct(np.array([4., 3., 5., 10., 5., 3.]))
print(y)

import numpy as np
from scipy.fftpack import dct, idct

y = idct(np.array([4., 3., 5., 10., 5., 3.]))
print(y)
