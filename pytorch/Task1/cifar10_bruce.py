# aims   : cifar10完成分类
# time   : 20190807
# author : Bruce


import torch

import torchvision as tv
import torchvision.transforms as transforms
from   torchvision.transforms import ToPILImage
show = ToPILImage() # 可以把Tensor转为Image，便于可视化

import numpy as np
import cv2 as cv

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from scipy import misc



# 数据增广方法
transform = transforms.Compose([
    transforms.ToTensor(), # 转Tensor格式
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),# 归一化
    ])

# 训练集
trainset = tv.datasets.CIFAR10(
        #虽然Bruce已经手动下载了cifar-10-batches-py文件夹，但是没用
        #然后是选定了名为 cifar-10-batches-py 的文件夹的地址。所以，是文件名的区别？很奇怪哦~
        #root = '/home/bruce/Downloads/git/dataWhaleWithBruce/pytorch/Task1/cifar-10-batches-py/',
        #root = '~/Downloads/cifar-10-python.tar.gz',
        root = 'DataSet/',
        train = True,
        download = False,
        transform = transform)

# 生成train的数据加载器
trainloader = torch.utils.data.DataLoader(
        trainset,
        batch_size = 4,
        shuffle = True,
        num_workers = 2)

# 测试集
testset = tv.datasets.CIFAR10(
        #'/home/bruce/Downloads/git/dataWhaleWithBruce/pytorch/Task1/cifar-10-batches-py/test_batch',
        #'~/Downloads',
        'DataSet/',
        train = False,
        download = False,
        transform = transform)


# 生成test的数据加载器
testloader = torch.utils.data.DataLoader(
        testset,
        batch_size=4,
        shuffle=False,
        num_workers=2)

# 分类索引。这里是classes 而不是class
classes = ('plane','car','bird','cat','deer','dog','frog','horse','ship','truck')

'''
# 输出数据库的内容, 验证数据集的格式
(data, label) = trainset[100]
print(classes[label]) # 这里的label是数字标记
# (data + 1)/2 是为了还原被归一化的数据
show((data + 1) / 2).resize((100, 100))
'''

# 查看数据，取一组batch
data_iter = iter(testloader)
images, labels = next(data_iter)
# 取batch中的一张图像
idx = 1
image = images[idx].numpy()
image = np.transpose(image, (1, 2, 0)) 
plt.imshow(image)
classes[labels[idx].numpy()]

'''
Mat one = trainset[100].numpy()
cv.imshow(one)
'''

