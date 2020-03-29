# coding=gbk
import better_exceptions

better_exceptions.hook()

from scipy import ndimage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# ����ͼƬ
face = mpimg.imread('./face.png')

# ��ʾͼƬ
plt.imshow(face)
# plt.savefig('./img2-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()

# ����ͼƬ
face = mpimg.imread('./face.png')

# ��תͼƬ
rotate_face = ndimage.rotate(face, 45)

plt.imshow(rotate_face)
# plt.savefig('./img3-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()

# ����ͼƬ
face = mpimg.imread('./face.png')

# ����ͼƬ
face1 = ndimage.gaussian_filter(face, sigma=3)

# ��ʾͼƬ
plt.imshow(face1)
# plt.savefig('./img4-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()

import scipy.ndimage as nd
import numpy as np

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im[90:-90, 90:-90] = 2
im = nd.gaussian_filter(im, 8)

import matplotlib.pyplot as plt

plt.imshow(im)
# plt.savefig('./img5-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im[90:-90, 90:-90] = 2
im = nd.gaussian_filter(im, 8)

sx = nd.sobel(im, axis=0, mode='constant')
sy = nd.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

plt.imshow(sob)
# plt.savefig('./img6-1.png') # ����Ҫ��ʾ��ͼƬ
plt.show()
