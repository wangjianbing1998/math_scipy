# coding=gbk
import better_exceptions

better_exceptions.hook()

from scipy.cluster.vq import kmeans, vq, whiten

from numpy import vstack, array
from numpy.random import rand

# ����3������ֵ��������������
data = vstack((rand(100, 3) + array([.5, .5, .5]), rand(100, 3)))

# �׻�����
data = whiten(data)
# ���� K = 3 ʱ�����ĵ�
centroids, _ = kmeans(data, 3)
print(centroids)
# �����������е�ÿ��ֵ�����һ�����ĵ㣬�γ�3�����ࡣ
# ����ֵclx����˶�Ӧ���������ľ��࣬dist��ʾ��Ӧ����������������ĵľ��롣
clx, dist = vq(data, centroids)
# ��ӡ����
print(clx)
