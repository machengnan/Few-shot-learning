# python3.7
# -*- coding: utf-8 -*-
"""
@author: machengnan
@contact:2624079968@qq.com
@version: 1.0.0
@file: dataread.py
@time: 2020/4/26 13:17
"""
from scipy.io import loadmat
dataMat=loadmat('aPaY/aPaY/apay_googlenet.mat')
# mat文件有很多不相关的keys，要找到目标的keys
print(dataMat.keys()) # 输出为dict_keys(['__header__', '__version__', '__globals__', 'data', 'label'])
features = dataMat['features']
image_name = dataMat['image_name']
image_bbox = dataMat['image_bbx']
class_test = dataMat['class_test']


