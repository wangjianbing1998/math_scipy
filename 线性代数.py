# coding=gbk
import better_exceptions

better_exceptions.hook()

# ����scipy��numpy��
from scipy import linalg
import numpy as np

# ����numpy����
a = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
b = np.array([10, 8, 3])

# ���
x = linalg.solve(a, b)

# �����ֵ
print(x)

# ����scipy��numpy��
from scipy import linalg
import numpy as np

# ����numpy����
A = np.array([[3, 4], [7, 8]])

# ��������ʽ
x = linalg.det(A)

# ������
print(x)
# ����scipy��numpy��
from scipy import linalg
import numpy as np

# ����numpy����
A = np.array([[3, 4], [7, 8]])

# ���
l, v = linalg.eig(A)

# ��ӡ����ֵ
print('����ֵ')
print(l)

# ��ӡ��������
print('��������')
print(v)
# ����scipy��numpy��
from scipy import linalg
import numpy as np

# ����numpy����
a = np.random.randn(3, 2) + 1.j * np.random.randn(3, 2)

# ���ԭ����
print('ԭ����')
print(a)

# ���
U, s, Vh = linalg.svd(a)

# ������
print('����ֵ�ֽ�')
print(U, "#U")
print(Vh, "#Vh")
print(s, "#s")
