# coding=gbk
import better_exceptions

better_exceptions.hook()

# 导入scipy和numpy包
from scipy import linalg
import numpy as np

# 声明numpy数组
a = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
b = np.array([10, 8, 3])

# 求解
x = linalg.solve(a, b)

# 输出解值
print(x)

# 导入scipy和numpy包
from scipy import linalg
import numpy as np

# 声明numpy数组
A = np.array([[3, 4], [7, 8]])

# 计算行列式
x = linalg.det(A)

# 输出结果
print(x)
# 导入scipy和numpy包
from scipy import linalg
import numpy as np

# 声明numpy数组
A = np.array([[3, 4], [7, 8]])

# 求解
l, v = linalg.eig(A)

# 打印特征值
print('特征值')
print(l)

# 打印特征向量
print('特征向量')
print(v)
# 导入scipy和numpy包
from scipy import linalg
import numpy as np

# 声明numpy数组
a = np.random.randn(3, 2) + 1.j * np.random.randn(3, 2)

# 输出原矩阵
print('原矩阵')
print(a)

# 求解
U, s, Vh = linalg.svd(a)

# 输出结果
print('奇异值分解')
print(U, "#U")
print(Vh, "#Vh")
print(s, "#s")
