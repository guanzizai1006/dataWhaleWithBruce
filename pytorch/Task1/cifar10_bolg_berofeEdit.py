# 这里我把训练代码给注释了，用于从数据集中提取图片出来。

# 导入包
# basic
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np

#resize功能
from scipy import misc

# opencv功能
import cv2 as cv
import PIL  # PIL.Image是可以的

# pytorch
import torch 
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
# 设备设置
# torch.cuda.set_device(1) # 这句用来设置pytorch在哪块GPU上运行，pytorch-cpu版本不需要运行这句
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# 超参数设置
num_epochs = 5
num_classes = 10
batch_size = 16
learning_rate = 0.001

# cifar10 分类索引
classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
# 数据增广方法
transform = transforms.Compose([
    # +4填充至36x36
    transforms.Pad(4),
    # 随机水平翻转
    transforms.RandomHorizontalFlip(), 
    # 随机裁剪至32x32
    transforms.RandomCrop(32), 
    # 转换至Tensor
    transforms.ToTensor(),
    #  归一化
#     transforms.Normalize(mean=(0.5, 0.5, 0.5),   # 3 for RGB channels
#                                      std=(0.5, 0.5, 0.5))
    ])

# cifar10路径
# cifar10Path = './cifar'
cifar10Path = '~/Downloads/git/dataWhaleWithBruce/pytorch/Task1/DataSet/cifar-10-batches-py'



#  训练数据集
train_dataset = torchvision.datasets.CIFAR10(root=cifar10Path,
                                             train=True, 
                                             transform=transform,
                                             download=True)

# 测试数据集
test_dataset = torchvision.datasets.CIFAR10(root=cifar10Path,
                                            train=False, 
                                            transform=transform)

# 生成数据加载器
# 训练数据加载器
train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size, 
                                           shuffle=True)
# 测试数据加载器
test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size, 
                                          shuffle=False)

'''
# 查看数据,取一组batch
data_iter = iter(test_loader)
images, labels = next(data_iter)


# 取batch中的一张图像, plt 显示
idx = 15
image_numpy = images[idx].numpy()
image_plt = np.transpose(image_numpy, (1,2,0))
plt.imshow(image_plt)
print(classes[labels[idx].numpy()])

# numpy格式转为opencv image去显示
# image_cv = cv.fromarray(image_numpy)
# img123 = PIL.Image.fromarray(image_numpy)
# cv.imshow("demo", img123)

# 成功的显示方式。要转换成uint8才ok
cv.imshow("img",np.uint8(image_plt))
# cv.waitKey()

'''

# 网络模型设计和训练
class ConvNet(nn.Module): 
    # nn.Module，这里要是Module而不是module
    def __init__(self, num_classes = 10):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Sequential(
                # 卷积层计算
                nn.Conv2d(3, 16, kernel_size = 5, stride = 1, padding =2),
                # 批归一化
                nn.BatchNorm2d(16),
                # ReLu
                nn.ReLU(),
                nn.MaxPool2d(kernel_size = 2, stride = 2))
        self.conv2 = nn.Sequential(
                nn.Conv2d(16, 32, kernel_size = 5, stride = 1, padding = 2),
                nn.BatchNorm2d(32),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size = 2, stride =2))
        self.fc = nn.Linear(8*8*32, num_classes)

        #定义前向传播顺序
        def forward(self, x):
            out = self.conv1(x)
            out = self.conv2(out)
            out = out.reshape(out.size(0), -1)
            out = self.fc(out)
            return out


# 实例化模型，这里Bruce并不迁移到GPU中了；因为没有检测到GPU
model = ConvNet(num_classes).to(device)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)
"""
total_step = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        # 模型在哪，数据也要在哪里(也就是，同在cpu或者gpu)
        images = images.to(device)
        labels = labels.to(device)

        # 前向传播
        outputs = model(images)
        loss = criterion(outputs, labels)

        # 反向传播和优化
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (i+1) % 100 == 0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, i+1, total_step, loss.item()))
"""


# 保存数据集的图片到本地，供Task2中完成测试
data_iter = iter(train_loader)
images, labels = next(data_iter)
# 取batch中的一张图像
idx = 11
image = images[idx].numpy()
image = np.transpose(image, (1, 2, 0))
plt.imshow(image)
classes[labels[idx].numpy()]
cv.imwrite("../Task2/imgFromDataSet.png", image)

