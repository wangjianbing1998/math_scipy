# coding=gbk
import better_exceptions

better_exceptions.hook()

import scipy.io as sio
import numpy as np

# ����mat�ļ�
vect = np.arange(20)
sio.savemat('array.mat', {'vect': vect})

# �����ļ�
mat_file_content = sio.loadmat('array.mat')
print(mat_file_content)
