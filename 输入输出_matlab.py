# coding=gbk
import better_exceptions

better_exceptions.hook()

import scipy.io as sio
import numpy as np

# 保存mat文件
vect = np.arange(20)
sio.savemat('array.mat', {'vect': vect})

# 加载文件
mat_file_content = sio.loadmat('array.mat')
print(mat_file_content)
