# coding=gbk
import better_exceptions

better_exceptions.hook()

import scipy
# 导入pi常量
from scipy.constants import pi

print("sciPy - pi = %.16f" % pi)

from scipy.constants import find, physical_constants

res = scipy.constants.find("boltzmann")
print(res)

print(scipy.constants.physical_constants['Boltzmann constant'])
