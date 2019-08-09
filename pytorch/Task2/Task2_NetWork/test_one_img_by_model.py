# 加载模型，进行测试，完成图片分类

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

# cifar10 分类索引
classes = ('plane', 'car', 'bird', 'cat',
                   'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

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


'''
# 用于输出模型的结构和参数
# 1. 加载模型训练后的参数
model_dict = torch.load('./model.ckpt')

# model.eval(),失败的
# print(model_dict)

params = model_dict 
for k,v in params.items():
    print(k) # 打印网络中的变量名

print('\n')
print("输出conv1.0的weight")
print(params['conv1.0.weight'])
print("输出conv1.0的bias")
print(params['conv1.0.bias'])
'''



# 加载数据到我的模型
# 这里一定要实例化一个model，然后再往这个模型结构中，载入参数才ok
# TODO: 修改模型，并取模型中一小部分的数据，该如何操作
model = ConvNet()
model.load_state_dict(torch.load("./model.ckpt"))

# 1. 读取本地一张马匹的图片，完成测试（保存的图片大小不规则，不等于n*3*32*32，所以这里就给注释掉吧）

# srcPath = './testImg_Bruce_folder/output_29_1.png'
srcPath = './imgFromDataSet.png'
src = mpimg.imread(srcPath)
print(src.shape)

plt.imshow(src)
plt.axis('off') # 不显示坐标轴
# plt.show() # 这一行注释掉，则不会显示此图了

# 进行resize
newImg = misc.imresize(src, (32, 32))
plt.imshow(newImg)
plt.axis('off')
# plt.show() # 注释掉了就不用显示了
# 转换为（B,C,H,W）大小
imagebatch = newImg.reshape(-1,3,32,32)# 这里会报错，因为图片总共是4096个像素点，分不了若干个3*32*32个图片。
# 转换为torch tensor
image_tensor = torch.from_numpy(imagebatch)



# 2. 准备读取测试集的图片
# Bruce还是从Task1中，去得到了训练集中的图了，32*32 大小。
'''
data_iter = iter(test_loader)
images, labels = next(data_iter)
# 取batch中的一张图像，显示图像和真实label
idx = 10
image = images[idx].numpy
'''



# 调用模型进行评估
model.eval()
output = model(image_tensor)#.to(device))
_, predicted = torch.max(output.data, 1)
pre = predicted.cpu().numpy()
print(pre)
print(num_classes[pre[0]])


# 总结：为了能适应任意尺寸图片，是否要考虑哪种reshape方法会比较合理~


