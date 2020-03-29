# coding=gbk
import better_exceptions

better_exceptions.hook()

from scipy.cluster.vq import kmeans, vq, whiten

from numpy import vstack, array
from numpy.random import rand

# 具有3个特征值的样本数据生成
data = vstack((rand(100, 3) + array([.5, .5, .5]), rand(100, 3)))

# 白化数据
data = whiten(data)
# 计算 K = 3 时的中心点
centroids, _ = kmeans(data, 3)
print(centroids)
# 将样本数据中的每个值分配给一个中心点，形成3个聚类。
# 返回值clx标出了对应索引样本的聚类，dist表示对应索引样本与聚类中心的距离。
clx, dist = vq(data, centroids)
# 打印聚类
print(clx)
