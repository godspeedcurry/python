# -*- coding: utf-8 -*

from PIL import Image
from pylab import *
import matplotlib.pyplot as plt
#读取图片,灰度化，并转为数组
# im = array(Image.open("1.png").convert('L'))
# im2 = 255 - im # 对图像进行反相处理

# im2.save('1.png','')
# img=Image.open('d:/dog.png')
im = array(Image.open('1.png'))
im2 = 255 - im
# 绘制图像
imshow(im2)
show()